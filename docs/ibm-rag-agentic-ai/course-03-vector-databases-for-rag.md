# Course 3 - Vector Databases for RAG

<span class="track-badge rag">IBM RAG & Agentic AI</span>

## What This Covers

This course focuses on embeddings, similarity search, Chroma DB, filters, and recommendation-style retrieval. Local materials include notebooks for similarity search by hand, readings on vector databases and HNSW-style search, Chroma filtering notes, text search labs, employee record search, and a food recommendation practice project.

## Core Ideas

- Embeddings convert text or records into numerical vectors.
- Similarity search retrieves items whose vectors are close to a query vector.
- Vector databases manage storage, indexing, metadata, and fast nearest-neighbor search.
- Metadata filters narrow the candidate set before or during retrieval.
- Recommendation systems can use similarity search to match user preferences with items.

## Important Formulas

Euclidean distance measures straight-line distance between two vectors.

\[
d(a,b) = \sqrt{\sum_i (a_i - b_i)^2}
\]

Where:

- \(a_i\) and \(b_i\) are the values in dimension \(i\).
- Smaller distance means the vectors are closer.

Cosine similarity measures direction rather than magnitude.

\[
\text{cosine similarity}(a,b) = \frac{\sum_i a_i b_i}{\sqrt{\sum_i a_i^2}\sqrt{\sum_i b_i^2}}
\]

Where:

- The numerator compares matching dimensions.
- The denominator normalizes by vector length.
- A value closer to 1 usually means stronger semantic similarity.

## Human-Readable Explanation

The course shows why vector search is different from keyword search. Keyword search looks for literal terms; vector search looks for meaning represented in embedding space. This allows a query such as "healthy dinner with vegetables" to match records that may not use exactly those words.

Chroma DB is used as a practical vector database. It stores embeddings plus metadata, supports similarity queries, and can filter by structured fields. The food recommendation project demonstrates how retrieval can be improved by adding constraints such as calories, cuisine, or dietary preference.

## Key Code Patterns

Create and query a Chroma collection:

```python
collection.add(
    documents=texts,
    metadatas=metadata,
    ids=ids
)

results = collection.query(
    query_texts=[user_query],
    n_results=5,
    where={"category": "healthy"}
)
```

Limit and filter retrieved results:

```python
filtered = [item for item in results if item["calories"] <= max_calories]
```

## Common Mistakes

- Comparing raw vectors without normalizing when the metric expects normalized vectors.
- Ignoring metadata that could remove irrelevant candidates.
- Retrieving too many results and overwhelming the generation step.
- Treating vector search as exact search.

## Takeaways

Course 3 explains the retrieval engine underneath many RAG systems. Embeddings provide semantic matching, while metadata and result limiting make the search usable.
