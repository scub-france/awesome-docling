<p align="center">
  <a href="https://github.com/docling-project/docling">
    <img src="https://raw.githubusercontent.com/docling-project/docling/main/logo.png" alt="Docling" width="200">
  </a>
</p>

<h1 align="center">Awesome Docling</h1>

<p align="center">
  A curated list of tools, integrations, articles, and resources for <a href="https://github.com/docling-project/docling">Docling</a> — the open-source document processing toolkit by IBM Research, hosted by the <a href="https://lfaidata.foundation/">LF AI & Data Foundation</a>.
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/docling-project/docling?style=flat-square&label=docling%20%E2%AD%90&color=2b2b2b" alt="Stars">
  <img src="https://img.shields.io/github/license/docling-project/docling?style=flat-square&color=2b2b2b" alt="License">
</p>

---

## Contents

- [Getting Started](#getting-started)
- [Official Ecosystem](#official-ecosystem)
- [Models](#models)
- [Framework Integrations](#framework-integrations)
- [Community Tools](#community-tools)
- [Articles & Tutorials](#articles--tutorials)
- [Papers](#papers)
- [Community](#community)

## Getting Started

| Resource | Description |
|----------|-------------|
| [📖 Documentation](https://docling-project.github.io/docling/) | Installation, quickstart, concepts, and API reference |
| [🧑‍🍳 Examples & Recipes](https://docling-project.github.io/docling/examples/) | End-to-end workflows: conversion, RAG, VLM pipelines, audio, XBRL |
| [🤗 Hugging Face Space](https://huggingface.co/spaces/ds4sd/docling) | Try Docling in the browser — no install required |
| [📓 Workshops](https://github.com/docling-project/docling-workshops) | Official Jupyter notebooks for hands-on learning |

## Official Ecosystem

Core repositories maintained by [docling-project](https://github.com/docling-project).

| Stars | Project | Description |
|-------|---------|-------------|
| ![](https://img.shields.io/github/stars/docling-project/docling?style=flat-square&label=%E2%AD%90) | [**docling**](https://github.com/docling-project/docling) | Main library. Parse PDF, DOCX, PPTX, XLSX, HTML, images, audio into unified DoclingDocument |
| ![](https://img.shields.io/github/stars/docling-project/docling-core?style=flat-square&label=%E2%AD%90) | [**docling-core**](https://github.com/docling-project/docling-core) | Core data types, transforms, serializers, chunking & profiling APIs. DoclingDocument Pydantic model |
| ![](https://img.shields.io/github/stars/docling-project/docling-serve?style=flat-square&label=%E2%AD%90) | [**docling-serve**](https://github.com/docling-project/docling-serve) | FastAPI REST server. Container images for CPU, CUDA 12.8/13.0, ROCm 6.3 |
| ![](https://img.shields.io/github/stars/docling-project/docling-mcp?style=flat-square&label=%E2%AD%90) | [**docling-mcp**](https://github.com/docling-project/docling-mcp) | MCP server for document conversion & generation agents. Claude Desktop, LM Studio compatible |
| ![](https://img.shields.io/github/stars/docling-project/docling-parse?style=flat-square&label=%E2%AD%90) | [**docling-parse**](https://github.com/docling-project/docling-parse) | Backend PDF parser used by Docling |
| ![](https://img.shields.io/github/stars/docling-project/docling-ibm-models?style=flat-square&label=%E2%AD%90) | [**docling-ibm-models**](https://github.com/docling-project/docling-ibm-models) | AI models: layout analysis (RT-DETR / DocLayNet), table structure (TableFormer), Heron |
| ![](https://img.shields.io/github/stars/docling-project/docling-sdg?style=flat-square&label=%E2%AD%90) | [**docling-sdg**](https://github.com/docling-project/docling-sdg) | Synthetic data generation from documents for RAG evaluation and LLM fine-tuning |
| ![](https://img.shields.io/github/stars/docling-project/docling-eval?style=flat-square&label=%E2%AD%90) | [**docling-eval**](https://github.com/docling-project/docling-eval) | Evaluation framework for document processing models and services |
| ![](https://img.shields.io/github/stars/docling-project/docling-graph?style=flat-square&label=%E2%AD%90) | [**docling-graph**](https://github.com/docling-project/docling-graph) | Transform documents into validated, queryable knowledge graphs |
| ![](https://img.shields.io/github/stars/docling-project/docling-jobkit?style=flat-square&label=%E2%AD%90) | [**docling-jobkit**](https://github.com/docling-project/docling-jobkit) | Distributed batch processing with multiprocessing & Kubeflow Pipelines |
| ![](https://img.shields.io/github/stars/docling-project/docling-java?style=flat-square&label=%E2%AD%90) | [**docling-java**](https://github.com/docling-project/docling-java) | Java API via docling-serve REST |
| ![](https://img.shields.io/github/stars/docling-project/docling-ts?style=flat-square&label=%E2%AD%90) | [**docling-ts**](https://github.com/docling-project/docling-ts) | Official TypeScript/JS library and web components for Docling JSON output |
| ![](https://img.shields.io/github/stars/docling-project/docling-metrics?style=flat-square&label=%E2%AD%90) | [**docling-metrics**](https://github.com/docling-project/docling-metrics) | Core package for type and interface definitions of docling metric implementations |
| ![](https://img.shields.io/github/stars/docling-project/docling-cvat-tools?style=flat-square&label=%E2%AD%90) | [**docling-cvat-tools**](https://github.com/docling-project/docling-cvat-tools) | Collection of CVAT parsing and campaign utilities for Docling |
| ![](https://img.shields.io/github/stars/docling-project/docling.rs?style=flat-square&label=%E2%AD%90) | [**docling.rs**](https://github.com/docling-project/docling.rs) | Full Rust port of Python docling |

## Models

### Vision Language Models

| Model | Params | Description |
|-------|--------|-------------|
| [granite-docling-258M](https://huggingface.co/ibm-granite/granite-docling-258M) | 258M | Production-ready VLM. DocTags output, tables, equations, code. Experimental CJK + Arabic. MLX variant for Apple Silicon. Apache 2.0 |
| [SmolDocling-256M-preview](https://huggingface.co/ds4sd/SmolDocling-256M-preview) | 256M | Research preview predecessor to Granite-Docling (IBM Research & Hugging Face, Mar 2025) |

### Pipeline Models (in docling-ibm-models)

| Model | Purpose |
|-------|---------|
| **Layout Analysis** | RT-DETR trained on [DocLayNet](https://github.com/DS4SD/DocLayNet) — page element detection |
| **TableFormer** | Table structure recognition — rows, columns, spanning cells |
| **Heron** | Newer default layout model for faster PDF parsing (Docling v2.80+) |

## Framework Integrations

### RAG & Orchestration

| Framework | Integration | Links |
|---------| ![](https://img.shields.io/github/stars/GiovanniPasq/chunky?style=flat-square&label=%E2%AD%90) | [**chunky**](https://github.com/GiovanniPasq/chunky) | Your RAG pipeline is broken and you don't know it. Chunky lets you validate your Markdown and choose the best chunking strategy before indexing. |
| ![](https://img.shields.io/github/stars/ENDEVSOLS/LongParser?style=flat-square&label=%E2%AD%90) | [**LongParser**](https://github.com/ENDEVSOLS/LongParser) | Privacy-first document intelligence engine — parse PDFs, DOCX, PPTX, XLSX & CSV into AI-ready chunks for RAG pipelines. Includes HITL review, 3-layer memory chat, and a production FastAPI server. |
--|-------------|-------|
| **LangChain** | `langchain-docling` — `DoclingLoader` with `DOC_CHUNKS` / `MARKDOWN` export | [PyPI](https://pypi.org/project/langchain-docling/) · [example](https://docling-project.github.io/docling/examples/rag_langchain/) |
| **LlamaIndex** | `DoclingReader` + `DoclingNodeParser` with hierarchical chunking | [PyPI](https://pypi.org/project/llama-index-readers-docling/) · [example](https://docling-project.github.io/docling/examples/rag_llamaindex/) |
| **Haystack** | Pipeline integration for retrieval and generation workflows | [example](https://docling-project.github.io/docling/examples/rag_haystack/) |
| **Crew AI** | Agent-ready document processing for multi-agent systems | [example](https://docling-project.github.io/docling/examples/rag_crewai/) |

### Vector Stores

Official RAG examples with **Milvus**, **Weaviate**, **Qdrant**, and **OpenSearch** — see the [examples page](https://docling-project.github.io/docling/examples/).

### Java / JVM

| Stars | Project | Description |
|-------|---------|-------------|
| ![](https://img.shields.io/github/stars/quarkiverse/quarkus-docling?style=flat-square&label=%E2%AD%90) | [**quarkus-docling**](https://github.com/quarkiverse/quarkus-docling) | Quarkus extension with Dev Service/UI. Goal: unify DoclingDocument with LangChain4j |

### TypeScript / JavaScript

| Stars | Project | Description |
|-------|---------|-------------|
| ![](https://img.shields.io/github/stars/docling-project/docling-ts?style=flat-square&label=%E2%AD%90) | [**docling-ts**](https://github.com/docling-project/docling-ts) | Official TS/JS types mirroring docling-core + web components |
| ![](https://img.shields.io/github/stars/btwld/docling-sdk?style=flat-square&label=%E2%AD%90) | [**docling-sdk**](https://github.com/btwld/docling-sdk) | Community SDK wrapping CLI + REST API. Type-safe, WebSocket, S3 integration ([npm](https://www.npmjs.com/package/docling-sdk)) |

## Community Tools

### Visual Inspection & UI

| Stars | Project | Description |
|-------|---------|-------------|
| ![](https://img.shields.io/github/stars/scub-france/SmolDocling-visualizer?style=flat-square&label=%E2%AD%90) | [**Docling Studio**](https://github.com/scub-france/SmolDocling-visualizer) | Visual inspection layer — side-by-side source vs. DoclingDocument comparison *(SCUB)* |
| ![](https://img.shields.io/github/stars/hparreao/doclingconverter?style=flat-square&label=%E2%AD%90) | [**DoclingConverter**](https://github.com/hparreao/doclingconverter) | Streamlit UI for converting documents to Markdown, JSON, or YAML |
| ![](https://img.shields.io/github/stars/captv89/OpenDA?style=flat-square&label=%E2%AD%90) | [**OpenDA**](https://github.com/captv89/OpenDA) | Open-source Human-in-the-Loop AI platform for maritime port agency cost validation. |

### RAG Systems

| Stars | Project | Description |
|-------|---------|-------------|
| ![](https://img.shields.io/github/stars/ggozad/haiku.rag?style=flat-square&label=%E2%AD%90) | [**haiku.rag**](https://github.com/ggozad/haiku.rag) | Agentic RAG on LanceDB + Pydantic AI + Docling. Hybrid search, research agents, MCP server, chat TUI |
| ![](https://img.shields.io/github/stars/HaileyTQuach/docchat-docling?style=flat-square&label=%E2%AD%90) | [**DocChat**](https://github.com/HaileyTQuach/docchat-docling) | Multi-agent RAG with BM25 + vector search, fact-checking loop, Gradio UI |
| ![](https://img.shields.io/github/stars/stevereiner/flexible-graphrag?style=flat-square&label=%E2%AD%90) | [**Flexible GraphRAG**](https://github.com/stevereiner/flexible-graphrag) | 8 graph DBs, 10 vector DBs, hybrid search. React/Vue/Angular frontends, MCP server |
| ![](https://img.shields.io/github/stars/royjoydeep348/docling-rag-agent?style=flat-square&label=%E2%AD%90) | [**docling-rag-agent**](https://github.com/royjoydeep348/docling-rag-agent) | CLI RAG agent with PostgreSQL/pgvector, streaming responses, Docling tutorials included |
| ![](https://img.shields.io/github/stars/LeDat98/NexusRAG?style=flat-square&label=%E2%AD%90) | [**NexusRAG**](https://github.com/LeDat98/NexusRAG) | Hybrid RAG system combining vector search, knowledge graph (LightRAG), and cross-encoder reranking — with Docling document parsing, visual intelligence (image/table captioning), agentic streaming chat, and inline citations. Powered by Gemini or local Ollama models. |
| ![](https://img.shields.io/github/stars/NameetP/pdfmux?style=flat-square&label=%E2%AD%90) | [**pdfmux**](https://github.com/NameetP/pdfmux) | PDF extraction that checks its own work. #2 reading order accuracy — zero AI, zero GPU, zero cost. |
| ![](https://img.shields.io/github/stars/Sqhao-O/dsh-docs?style=flat-square&label=%E2%AD%90) | [**dsh-docs**](https://github.com/Sqhao-O/dsh-docs) | Fully local document intelligence for DeepSeek Harness. Parse PDF, Office files, images, and scanned documents with offline OCR. | DeepSeek Harness 全本地文档智能插件，支持 PDF、Office、图片与离线 OCR |
| ![](https://img.shields.io/github/stars/686f6c61/Hermes-Research-PRISMA?style=flat-square&label=%E2%AD%90) | [**Hermes-Research-PRISMA**](https://github.com/686f6c61/Hermes-Research-PRISMA) | A reproducible Hermes Agent research runtime for systematic literature reviews, full-text evidence extraction, methodological routing, and auditable publication artifacts. |
| ![](https://img.shields.io/github/stars/anishmoncivarghese/docsift?style=flat-square&label=%E2%AD%90) | [**docsift**](https://github.com/anishmoncivarghese/docsift) | Convert documents once. Give agents only what they need — PDFs and Office files to clean Markdown, chunks and local search. |

### OCR Plugins

| Stars | Project | Description |
|-------|---------|-------------|
| ![](https://img.shields.io/github/stars/felixdittrich92/docling-OCR-OnnxTR?style=flat-square&label=%E2%AD%90) | [**docling-OCR-OnnxTR**](https://github.com/felixdittrich92/docling-OCR-OnnxTR) | OnnxTR (ONNX Runtime) OCR plugin. CPU, CUDA, OpenVINO. Multilingual |
| ![](https://img.shields.io/github/stars/DCC-BS/docling-glm-ocr?style=flat-square&label=%E2%AD%90) | [**docling-glm-ocr**](https://github.com/DCC-BS/docling-glm-ocr) | A docling plugin to integrate a remote hosted GLM-OCR OCR model into docling |
| ![](https://img.shields.io/github/stars/heripo-lab/heripo-engine?style=flat-square&label=%E2%AD%90) | [**heripo-engine**](https://github.com/heripo-lab/heripo-engine) | TypeScript library for extracting structured data from archaeological excavation report PDFs using Docling SDK and LLM-powered analysis |
| ![](https://img.shields.io/github/stars/daxueren666/exam-review-helper?style=flat-square&label=%E2%AD%90) | [**exam-review-helper**](https://github.com/daxueren666/exam-review-helper) | 把 PDF/Word/TXT/Markdown 教材浓缩成交互式 HTML 复习文档的 Claude Code / Codex CLI Skill。自动识别文科/理工科模式，5-pass 深度提取，原生支持扫描版 PDF OCR。v1.2 用 pdfium 后端修复 docling std::bad_alloc 崩溃，大 PDF 稳定提取。 |

## Articles & Tutorials

### Official

| Source | Article |
|--------|---------|
| 🐣 Docling Blog | [Chart Value Extraction](https://www.docling.ai/blog/) (Feb 2026) · [LaTeX Backend](https://www.docling.ai/blog/) (Mar 2026) |
| IBM | [Granite-Docling Announcement](https://www.ibm.com/new/announcements/granite-docling-end-to-end-document-conversion) (Jan 2026) · [Model Documentation](https://www.ibm.com/granite/docs/models/docling) |

### Community

| Source | Article | Date |
|--------|---------|------|
| Towards Data Science | [Docling: The Document Alchemist](https://towardsdatascience.com/docling-the-document-alchemist/) — table extraction, practical examples | Sep 2025 |
| InfoWorld | [Open-Source Tool Kit for Advanced Document Processing](https://www.infoworld.com/article/3997240/docling-an-open-source-tool-kit-for-advanced-document-processing.html) — technical overview | Feb 2026 |
| Niklas Heidloff | [Introduction to Docling](https://heidloff.net/article/docling/) — core concepts, classic vs. VLM pipelines | Sep 2025 |
| Medium | [Granite-Docling: RAG 2.0 Pipeline](https://medium.com/@visrow/ibm-granite-docling-super-charge-your-rag-2-0-pipeline-32ac102ffa40) — architecture deep dive | Sep 2025 |
| Medium | [Document Extraction with Docling](https://medium.com/@animakit/document-extraction-with-docling-514496f77d31) — receipt extraction | Nov 2025 |
| Medium | [RAG Pipeline 2026: Docling + Qdrant](https://medium.com/@yohanesegipratama/build-a-modern-rag-pipeline-in-2026-docling-qdrant-hybrid-bm25-dense-ai-agent-2e9ac3ccc990) — hybrid RAG with AI Agent | Jan 2026 |
| DEV Community | [Docling + OpenSearch RAG](https://dev.to/aairom/beyond-basic-chunks-supercharge-your-rag-with-docling-and-opensearch-294b) — code walkthrough | Oct 2025 |
| WordPress | [Document Intelligence Guide](https://atalupadhyay.wordpress.com/2025/08/07/document-intelligence-guide-to-docling-for-ai-ready-data-processing/) — pipeline internals | Aug 2025 |

## Papers

| Paper | Venue | Date |
|-------|-------|------|
| [Docling Technical Report](https://arxiv.org/abs/2408.09869) | arXiv | Aug 2024 |
| [Docling v2: Efficient AI-driven Document Conversion](https://arxiv.org/abs/2501.17887) | arXiv | Jan 2025 |
| [Know Your RAG: Dataset Taxonomy & Generation](https://aclanthology.org/2025.coling-industry.4/) | COLING 2025 Industry | Jan 2025 |

## Community

| Channel | Link |
|---------|------|
| 💬 Discussions | [GitHub Discussions](https://github.com/docling-project/docling/discussions) |
| 💻 Discord | [discord.gg/docling](https://discord.gg/docling) |
| 🔗 LinkedIn | [Docling Project](https://www.linkedin.com/company/docling-project/) |
| 🌐 Website | [docling.ai](https://www.docling.ai/) |
| 🏷️ GitHub Topic | [#docling](https://github.com/topics/docling) — discover community projects |

---

## Contributing

Contributions welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a PR.

## Maintainers

This list is maintained by [SCUB](https://github.com/scub-france), a French IT services company contributing to the Docling ecosystem through [Docling Studio](https://github.com/scub-france/SmolDocling-visualizer).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is released under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
