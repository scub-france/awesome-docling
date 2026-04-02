#!/usr/bin/env python3
"""
Discover new Docling-related projects on GitHub.

This script:
1. Searches GitHub for repositories with the 'docling' topic
2. Searches for new repositories in the docling-project organization
3. Filters based on star count and creation date
4. Compares with existing entries in README.md
5. Outputs new projects to new-projects.json
"""

import os
import re
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Set

# Configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
MIN_STARS = 5  # Minimum stars for a project to be considered
DAYS_BACK = 90  # Check for projects created in the last N days
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def extract_existing_repos(readme_path: str = 'README.md') -> Set[str]:
    """Extract GitHub repository names already listed in README.md"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match GitHub URLs in format: github.com/owner/repo
    pattern = r'github\.com/([^/\s\)]+)/([^/\s\)]+)'
    matches = re.findall(pattern, content)

    repos = set()
    for owner, repo in matches:
        # Clean up repo name (remove .git, trailing slashes, etc.)
        repo_clean = repo.rstrip('/').replace('.git', '')
        repos.add(f"{owner}/{repo_clean}".lower())

    print(f"📋 Found {len(repos)} existing repositories in README.md")
    return repos

def search_github_topic(topic: str = 'docling', days_back: int = DAYS_BACK) -> List[Dict]:
    """Search GitHub for repositories with a specific topic"""
    since_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')

    # Search query: topic + created date filter
    query = f'topic:{topic} created:>{since_date} stars:>={MIN_STARS}'

    url = 'https://api.github.com/search/repositories'
    params = {
        'q': query,
        'sort': 'stars',
        'order': 'desc',
        'per_page': 100
    }

    print(f"🔍 Searching GitHub: {query}")
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()

    data = response.json()
    print(f"   Found {data['total_count']} repositories with topic '{topic}'")

    return data.get('items', [])

def search_docling_org_repos(days_back: int = DAYS_BACK) -> List[Dict]:
    """Search for new repositories in the docling-project organization"""
    url = 'https://api.github.com/orgs/docling-project/repos'
    params = {
        'type': 'public',
        'sort': 'created',
        'direction': 'desc',
        'per_page': 100
    }

    print(f"🔍 Fetching repositories from docling-project organization")
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()

    repos = response.json()

    # Filter by creation date
    cutoff_date = datetime.now() - timedelta(days=days_back)
    recent_repos = [
        repo for repo in repos
        if datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ') > cutoff_date
    ]

    print(f"   Found {len(recent_repos)} new repositories in docling-project")
    return recent_repos

def filter_new_projects(all_projects: List[Dict], existing_repos: Set[str]) -> List[Dict]:
    """Filter projects to only include those not already in README"""
    new_projects = []

    for project in all_projects:
        full_name = project['full_name'].lower()

        # Skip if already in README
        if full_name in existing_repos:
            continue

        # Skip forks unless they have significant stars
        if project.get('fork') and project['stargazers_count'] < MIN_STARS * 2:
            continue

        new_projects.append({
            'full_name': project['full_name'],
            'html_url': project['html_url'],
            'description': project.get('description', ''),
            'stargazers_count': project['stargazers_count'],
            'language': project.get('language'),
            'topics': project.get('topics', []),
            'created_at': project['created_at'],
            'updated_at': project['updated_at'],
            'is_fork': project.get('fork', False),
            'archived': project.get('archived', False)
        })

    return new_projects

def main():
    """Main discovery workflow"""
    print("=" * 60)
    print("🚀 Docling Project Discovery")
    print("=" * 60)

    # Extract existing repositories from README
    existing_repos = extract_existing_repos()

    # Search for new projects
    all_projects = []

    # 1. Search by topic
    try:
        topic_projects = search_github_topic('docling', DAYS_BACK)
        all_projects.extend(topic_projects)
    except Exception as e:
        print(f"⚠️  Error searching topic 'docling': {e}")

    # 2. Search docling-project organization
    try:
        org_projects = search_docling_org_repos(DAYS_BACK)
        all_projects.extend(org_projects)
    except Exception as e:
        print(f"⚠️  Error searching docling-project org: {e}")

    # Remove duplicates (by full_name)
    unique_projects = {p['full_name']: p for p in all_projects}.values()

    # Filter to only new projects
    new_projects = filter_new_projects(list(unique_projects), existing_repos)

    # Sort by stars (descending)
    new_projects.sort(key=lambda x: x['stargazers_count'], reverse=True)

    print("\n" + "=" * 60)
    print(f"✨ Discovery complete: {len(new_projects)} new project(s) found")
    print("=" * 60)

    if new_projects:
        print("\n📦 New Projects:")
        for project in new_projects:
            print(f"   - {project['full_name']} ({project['stargazers_count']} ⭐)")

    # Write results to JSON file
    with open('new-projects.json', 'w', encoding='utf-8') as f:
        json.dump(new_projects, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Results saved to new-projects.json")

if __name__ == '__main__':
    main()
