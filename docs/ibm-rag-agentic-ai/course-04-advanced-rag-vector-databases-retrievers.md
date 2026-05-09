# Course 4 - Advanced RAG with Vector Databases and Retrievers

<span class="track-badge rag">IBM RAG & Agentic AI</span>

## What This Covers

This course expands basic RAG with advanced retrievers, LlamaIndex retrieval patterns, LangChain context retrieval, FAISS, HNSW concepts, and a YouTube summarizer and QA tool. The local materials include notebooks, cheat sheets, readings, and a `ytbot.py` lab script.

## Core Ideas

- Better RAG often means better retrieval, not just a stronger LLM.
- Retrievers can use chunking strategies, similarity search, metadata filters, reranking, and query transformation.
- FAISS provides efficient similarity search for dense vectors.
- HNSW approximates nearest-neighbor search using a navigable graph.
- Summarization and QA can share the same retrieval foundation but require different prompting.

## Important Formulas

Top-\(k\) retrieval means selecting the \(k\) highest-scoring candidates.

\[
\text{Top-}k = \operatorname*{arg\,max}_{k} \; s(q, d)
\]

Where:

- \(q\) is the query.
- \(d\) is a candidate document chunk.
- \(s(q,d)\) is the similarity score.
- \(k\) is the number of chunks returned.

Reranking means retrieving a broad candidate set first, then applying a stronger scoring function.

\[
\text{final rank} = \operatorname{sort}(r(q,d_1), r(q,d_2), \ldots, r(q,d_n))
\]

Where:

- \(r(q,d)\) is the reranker score for query \(q\) and document \(d\).
- \(n\) is the number of initially retrieved candidates.

## Human-Readable Explanation

Basic RAG can fail when the correct answer is split across chunks, when the query is phrased differently from the source, or when the retrieved chunks are semantically similar but not actually useful. Advanced retrievers try to reduce those failures.

The FAISS and HNSW materials focus on speed and scale. Instead of comparing a query against every stored vector, approximate nearest-neighbor methods search an index structure that is much faster while usually returning close matches.

The YouTube summarizer and QA lab shows a complete applied pattern: ingest transcript text, create searchable chunks, retrieve context for user questions, and generate answers or summaries grounded in the transcript.

## Key Code Patterns

Create a retriever from a vector store:

```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
docs = retriever.get_relevant_documents(question)
```

Use retrieved transcript chunks for QA:

```python
context = "\n\n".join(doc.page_content for doc in docs)
answer = llm.invoke(f"Use this transcript context:\n{context}\n\nQuestion: {question}")
```

## Detailed Study Notes

Advanced retrieval improves the evidence before generation. A common pattern is multi-stage retrieval: first retrieve a larger candidate set cheaply, then filter, compress, or rerank it before sending a smaller context to the LLM. This reduces missed evidence without flooding the prompt.

A practical retrieval chain can look like this:

```python
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 12})
candidate_docs = base_retriever.invoke(question)

reranked_docs = reranker.rank(question, candidate_docs)
final_docs = reranked_docs[:4]

context = "\n\n".join(doc.page_content for doc in final_docs)
answer = llm.invoke(f"Use the context below.\n\n{context}\n\nQuestion: {question}")
```

Query transformation helps when the user's wording does not match the source. The system can rewrite the question, generate multiple query variants, or expand acronyms before retrieval. This is helpful for transcripts, support docs, or course PDFs where the same idea may be phrased several ways.

HNSW-style search trades exactness for speed. It builds a graph where vectors connect to nearby vectors. Search walks the graph toward better neighbors instead of comparing against every vector. The result is fast approximate nearest-neighbor retrieval, but quality still needs evaluation with real questions.

For summarization, retrieval should preserve coverage. For QA, retrieval should preserve answer specificity. A transcript summarizer may need representative chunks from the whole video, while a QA bot needs the few chunks that answer the exact question.

## Common Mistakes

- Increasing `k` without checking whether the extra chunks add noise.
- Summarizing long content without preserving source boundaries.
- Using approximate search without validating retrieval quality.
- Forgetting that reranking can improve quality but adds latency.

## Takeaways

Course 4 is about retrieval quality. The best generated answer starts with the right evidence, in the right amount, with the right ranking.
