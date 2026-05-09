# Course 2 - Build RAG Applications

<span class="track-badge rag">IBM RAG & Agentic AI</span>

## What This Covers

This course introduces retrieval augmented generation, document question answering, Gradio interfaces, and the difference between LangChain and LlamaIndex. The local files include RAG cheat sheets, readings, a private-document summarization notebook, QA bot scripts, and Gradio demos for text and chat interfaces.

## Core Ideas

- RAG gives an LLM external context before it answers.
- Documents should be loaded, chunked, embedded, indexed, retrieved, and then passed into the prompt.
- Gradio provides quick interfaces for testing text, chat, and common input types.
- LangChain is often used for broad workflow composition; LlamaIndex is often used for data indexing and retrieval workflows.
- Good RAG answers depend on both retrieval quality and prompt design.

## Important Formulas

Chunk overlap means consecutive chunks share some text so important context is less likely to be split away.

\[
\text{new chunk start} = \text{previous chunk start} + \text{chunk size} - \text{overlap}
\]

Where:

- Chunk size is the maximum amount of text in one chunk.
- Overlap is the amount of text repeated between neighboring chunks.
- Larger overlap preserves continuity but increases index size.

Retrieval precision means the retrieved set contains mostly useful chunks.

\[
\text{Precision} = \frac{\text{useful chunks retrieved}}{\text{total chunks retrieved}}
\]

## Explanation

RAG is useful when the answer should be grounded in private or changing documents. The system first prepares documents for search. It splits them into chunks, embeds each chunk into a vector, stores the vectors, retrieves relevant chunks for a user question, and asks the LLM to answer using that retrieved context.

The course also introduces Gradio as a fast way to make these workflows interactive. A simple Gradio interface can expose a text prompt, chat history, file upload, or combined input without building a full frontend.

## Key Code Patterns

Minimal document QA shape:

```python
docs = loader.load()
chunks = text_splitter.split_documents(docs)
index = vectorstore.from_documents(chunks, embeddings)
retriever = index.as_retriever()
answer = qa_chain.invoke({"query": question})
```

Simple Gradio interface:

```python
demo = gr.Interface(fn=respond, inputs="text", outputs="text")
demo.launch()
```

## Detailed Study Notes

RAG has two separate phases. The indexing phase prepares the knowledge base before a user asks a question. The query phase retrieves relevant chunks at runtime and asks the model to answer using those chunks. Keeping those phases separate makes debugging much easier because retrieval can be evaluated without involving the LLM.

The indexing phase usually follows this shape:

```python
documents = loader.load()
chunks = splitter.split_documents(documents)
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./chroma_index"
)
vectorstore.persist()
```

The query phase should inspect retrieved context before trusting the final answer:

```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
docs = retriever.invoke(question)

for i, doc in enumerate(docs):
    print(i, doc.metadata, doc.page_content[:300])

context = "\n\n".join(doc.page_content for doc in docs)
answer = llm.invoke(f"Answer only from this context:\n{context}\n\nQuestion: {question}")
```

Chunk size is a design choice. Small chunks improve precision because each result is focused, but they can lose surrounding context. Large chunks preserve context but can bury the answer inside irrelevant text. Overlap reduces the chance that an answer is split at a boundary, but it increases storage and retrieval duplication.

Gradio is useful after the retrieval loop works. A good development order is: load one document, split it, print chunks, run retrieval, inspect retrieved chunks, generate an answer, then expose the function through Gradio.

## Common Mistakes

- Chunking documents without checking whether answers span chunk boundaries.
- Assuming retrieved text is relevant just because it has high vector similarity.
- Letting the model answer from prior knowledge when retrieved context is missing.
- Building a UI before validating the retrieval pipeline.

## Takeaways

Course 2 turns LLM apps into grounded document systems. The key habit is to inspect retrieved context before trusting the generated answer.
