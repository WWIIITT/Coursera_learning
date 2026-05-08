# Coursera Learning Notes

This site turns the local course materials in this repository into organized study notes. It is written course by course, then week by week or module by module, so that each page can be read as a focused review rather than as a raw notebook export.

## Course Catalog

<div class="course-grid" markdown="1">

<div class="course-card medical" markdown="1">
<span class="course-meta">Medical AI Track</span>
### [AI for Medical Diagnosis](ai-for-medical-diagnosis/index.md)
Week 1 and Week 2 notes for chest X-ray classification, leakage prevention, weighted loss, DenseNet, and diagnostic model metrics.
</div>

<div class="course-card rag" markdown="1">
<span class="course-meta">RAG and Agents Track</span>
### [IBM RAG & Agentic AI](ibm-rag-agentic-ai/index.md)
Eight-course path covering generative AI apps, RAG, vector databases, multimodal AI, tool use, LangGraph, CrewAI, AutoGen, and BeeAI.
</div>

<div class="course-card fullstack" markdown="1">
<span class="course-meta">Web Foundation Track</span>
### [IBM Full Stack Software Developer](ibm-full-stack-software-developer/index.md)
HTML, CSS, and JavaScript module notes focused on semantic structure, common tags, forms, fieldsets, and legends.
</div>

</div>

## Current Coverage Summary

The notes summarize notebooks, PDFs, Python scripts, SQL files, and existing markdown that are available locally in the repo. Generated folders, virtual environments, model weights, datasets, and built site artifacts are intentionally not summarized.

The largest track is IBM RAG & Agentic AI. It progresses from basic generative AI application patterns to retrieval augmented generation, vector search, multimodal systems, tool calling, and multi-agent orchestration. The medical diagnosis track focuses on an end-to-end chest X-ray classification workflow and then evaluates predictions with human-readable diagnostic metrics.

## How to Read Formulas

Every important formula is written in three parts:

1. A plain-language sentence that says what the formula measures.
2. A displayed equation using readable mathematical notation.
3. A short symbol list that defines each term.

For example, sensitivity means: among cases that are truly positive, how many did the model correctly call positive?

\[
\text{Sensitivity} = \frac{TP}{TP + FN}
\]

Where:

- \(TP\) means true positives.
- \(FN\) means false negatives.
- \(TP + FN\) means all actually positive cases.

## How to Read Code Snippets

Code snippets are short patterns, not complete lab copies. They show the shape of the solution, the important API calls, and the reasoning behind the implementation. Use the original notebooks and scripts in the repository when you need complete runnable examples.

## Main Concepts by Track

AI for Medical Diagnosis emphasizes data discipline. The key ideas are avoiding patient overlap, using training statistics correctly, handling class imbalance, building a multi-label classifier, and reading medical metrics without confusing accuracy with clinical usefulness.

IBM RAG & Agentic AI emphasizes system design. The key ideas are connecting LLMs to external data, retrieving relevant context, indexing embeddings, using tools and function calls, adding orchestration, and splitting complex workflows across specialized agents.

IBM Full Stack Software Developer introduces the browser foundation. The key ideas are using semantic HTML, structuring pages clearly, and choosing form elements that communicate meaning to users and assistive technology.
