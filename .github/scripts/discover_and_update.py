#!/usr/bin/env python3
"""
Discover new Docling projects and automatically update README.md

This script:
1. Discovers new Docling-related projects on GitHub
2. Categorizes them based on keywords and topics
3. Updates README.md with new entries in appropriate sections
4. Maintains existing formatting and sorts by stars
"""

import os
import re
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Set, Tuple

# Configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
MIN_STARS = 5
DAYS_BACK = 90
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Category keywords for auto-classification
CATEGORIES = {
    'framework_integrations': {
        'keywords': ['langchain', 'llamaindex', 'haystack', 'crewai', 'langgraph'],
        'section': '### RAG & Orchestration'
    },
    'ui_tools': {
        'keywords': ['ui', 'visualizer', 'streamlit', 'gradio', 'interface', 'viewer', 'studio'],
        'section': '### Visual Inspection & UI'
    },
    'rag_systems': {
        'keywords': ['rag', 'retrieval', 'vector', 'search', 'embedding', 'index'],
        'section': '### RAG Systems'
    },
    'ocr_plugins': {
        'keywords': ['ocr', 'optical', 'recognition', 'tesseract', 'onnx'],
        'section': '### OCR Plugins'
    }
}

def extract_existing_repos(readme_path: str = 'README.md') -> Set[str]:
    """Extract GitHub repository names already listed in README.md"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'github\.com/([^/\s\)]+)/([^/\s\)]+)'
    matches = re.findall(pattern, content)

    repos = set()
    for owner, repo in matches:
        repo_clean = repo.rstrip('/').replace('.git', '')
        repos.add(f"{owner}/{repo_clean}".lower())

    print(f"📋 Found {len(repos)} existing repositories in README.md")
    return repos

def search_github_topic(topic: str = 'docling', days_back: int = DAYS_BACK) -> List[Dict]:
    """Search GitHub for repositories with a specific topic"""
    since_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
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
    cutoff_date = datetime.now() - timedelta(days=days_back)
    recent_repos = [
        repo for repo in repos
        if datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ') > cutoff_date
    ]

    print(f"   Found {len(recent_repos)} new repositories in docling-project")
    return recent_repos

def categorize_project(project: Dict) -> str:
    """Determine the best category for a project based on its metadata"""
    full_name = project['full_name'].lower()
    description = (project.get('description') or '').lower()
    topics = ' '.join(project.get('topics', [])).lower()
    search_text = f"{full_name} {description} {topics}"

    # Official ecosystem projects
    if full_name.startswith('docling-project/'):
        return 'official'

    # Check each category
    for category, config in CATEGORIES.items():
        for keyword in config['keywords']:
            if keyword in search_text:
                return category

    # Default to community tools
    return 'community_tools'

def format_table_row(project: Dict) -> str:
    """Format a project as a table row"""
    stars_badge = f"![]({project['stars_badge']})"
    project_link = f"[**{project['name']}**]({project['html_url']})"
    description = project.get('description', 'No description provided')

    return f"| {stars_badge} | {project_link} | {description} |"

def insert_into_section(content: str, section_header: str, new_rows: List[str]) -> str:
    """Insert new rows into a specific section, maintaining star-based sorting"""
    if not new_rows:
        return content

    # Find the section header
    header_pattern = re.escape(section_header) + r'\n'
    header_match = re.search(header_pattern, content)

    if not header_match:
        print(f"⚠️  Section '{section_header}' not found")
        return content

    # Find the table after the header
    # Look for the table starting from the header position
    search_start = header_match.end()
    remaining_content = content[search_start:]

    # Match the table header and separator, then capture all rows until we hit a blank line or new section
    table_pattern = r'(\| Stars \| Project \| Description \|\n\|-------|---------|-------------\|\n)((?:\|.+\|\n)*)'
    table_match = re.search(table_pattern, remaining_content)

    if not table_match:
        print(f"⚠️  No table found after section '{section_header}'")
        return content

    # Calculate absolute positions
    table_start = search_start + table_match.start()
    table_header = table_match.group(1)
    table_rows_text = table_match.group(2)

    # Extract existing rows
    existing_rows = [row.strip() for row in table_rows_text.split('\n') if row.strip() and row.strip().startswith('|')]

    # Add new rows
    all_rows = existing_rows + new_rows

    # Rebuild table
    new_table = table_header + '\n'.join(all_rows) + '\n'

    # Calculate where the table ends
    table_end = search_start + table_match.end()

    # Replace old table with new one
    return content[:table_start] + new_table + content[table_end:]

def update_readme(new_projects: List[Dict], readme_path: str = 'README.md') -> bool:
    """Update README.md with new projects"""
    if not new_projects:
        print("✅ No new projects to add")
        return False

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Group projects by category
    categorized = {
        'official': [],
        'framework_integrations': [],
        'ui_tools': [],
        'rag_systems': [],
        'ocr_plugins': [],
        'community_tools': []
    }

    for project in new_projects:
        category = categorize_project(project)

        # Format project data
        formatted = {
            'name': project['name'],
            'html_url': project['html_url'],
            'description': project.get('description', 'No description provided'),
            'stars_badge': f"https://img.shields.io/github/stars/{project['full_name']}?style=flat-square&label=%E2%AD%90"
        }

        categorized[category].append(formatted)

    # Update each section
    updates_made = False

    # Official Ecosystem
    if categorized['official']:
        rows = [format_table_row(p) for p in categorized['official']]
        content = insert_into_section(content, '## Official Ecosystem', rows)
        updates_made = True
        print(f"✅ Added {len(rows)} project(s) to Official Ecosystem")

    # Framework Integrations - RAG & Orchestration
    if categorized['framework_integrations']:
        rows = [format_table_row(p) for p in categorized['framework_integrations']]
        content = insert_into_section(content, '### RAG & Orchestration', rows)
        updates_made = True
        print(f"✅ Added {len(rows)} project(s) to Framework Integrations")

    # Community Tools sections
    if categorized['ui_tools']:
        rows = [format_table_row(p) for p in categorized['ui_tools']]
        content = insert_into_section(content, '### Visual Inspection & UI', rows)
        updates_made = True
        print(f"✅ Added {len(rows)} project(s) to Visual Inspection & UI")

    if categorized['rag_systems']:
        rows = [format_table_row(p) for p in categorized['rag_systems']]
        content = insert_into_section(content, '### RAG Systems', rows)
        updates_made = True
        print(f"✅ Added {len(rows)} project(s) to RAG Systems")

    if categorized['ocr_plugins']:
        rows = [format_table_row(p) for p in categorized['ocr_plugins']]
        content = insert_into_section(content, '### OCR Plugins', rows)
        updates_made = True
        print(f"✅ Added {len(rows)} project(s) to OCR Plugins")

    # Generic community tools (no specific category)
    if categorized['community_tools']:
        # Add to the first community tools section we can find
        rows = [format_table_row(p) for p in categorized['community_tools']]
        content = insert_into_section(content, '### Visual Inspection & UI', rows)
        updates_made = True
        print(f"✅ Added {len(rows)} project(s) to Community Tools")

    if updates_made:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n💾 README.md updated successfully")

    return updates_made

def main():
    """Main discovery and update workflow"""
    print("=" * 60)
    print("🚀 Docling Project Discovery & Update")
    print("=" * 60)

    existing_repos = extract_existing_repos()

    # Search for new projects
    all_projects = []

    try:
        topic_projects = search_github_topic('docling', DAYS_BACK)
        all_projects.extend(topic_projects)
    except Exception as e:
        print(f"⚠️  Error searching topic: {e}")

    try:
        org_projects = search_docling_org_repos(DAYS_BACK)
        all_projects.extend(org_projects)
    except Exception as e:
        print(f"⚠️  Error searching org: {e}")

    # Remove duplicates
    unique_projects = {p['full_name']: p for p in all_projects}.values()

    # Filter new projects
    new_projects = []
    for project in unique_projects:
        full_name = project['full_name'].lower()

        if full_name in existing_repos:
            continue

        if project.get('fork') and project['stargazers_count'] < MIN_STARS * 2:
            continue

        new_projects.append({
            'full_name': project['full_name'],
            'name': project['name'],
            'html_url': project['html_url'],
            'description': project.get('description', ''),
            'stargazers_count': project['stargazers_count'],
            'language': project.get('language'),
            'topics': project.get('topics', []),
            'created_at': project['created_at'],
        })

    new_projects.sort(key=lambda x: x['stargazers_count'], reverse=True)

    print("\n" + "=" * 60)
    print(f"✨ Found {len(new_projects)} new project(s)")
    print("=" * 60)

    if new_projects:
        print("\n📦 New Projects:")
        for project in new_projects:
            category = categorize_project(project)
            print(f"   - {project['full_name']} ({project['stargazers_count']} ⭐) → {category}")

        # Update README
        updated = update_readme(new_projects)

        if updated:
            print("\n✅ README.md has been updated!")
        else:
            print("\n⚠️  No updates were made to README.md")
    else:
        print("\n✨ No new projects to add")

if __name__ == '__main__':
    main()
