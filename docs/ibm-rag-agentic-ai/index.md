# IBM RAG & Agentic AI

## What This Covers

This program moves from basic generative AI applications to retrieval augmented generation, vector search, multimodal applications, tool-using agents, and multi-agent orchestration. The local materials include notebooks, readings, cheat sheets, labs, Python scripts, SQL assets, and application folders.

## Core Ideas

- LLM applications become more useful when connected to prompts, tools, data stores, and user interfaces.
- RAG reduces hallucination risk by retrieving relevant context before generation.
- Vector databases store embeddings so semantically similar content can be found efficiently.
- Advanced retrievers improve retrieval quality through filtering, reranking, chunking strategies, and hybrid approaches.
- Multimodal systems combine text, image, audio, video, and speech workflows.
- Agents use tools, structured outputs, state, and orchestration to solve multi-step tasks.
- Multi-agent systems split work among specialized agents and coordinate their outputs.

## Important Formulas

Cosine similarity measures whether two embedding vectors point in a similar direction.

\[
\text{cosine similarity}(a,b) = \frac{a \cdot b}{\|a\| \|b\|}
\]

Where:

- \(a\) and \(b\) are embedding vectors.
- \(a \cdot b\) is their dot product.
- \(\|a\|\) and \(\|b\|\) are vector lengths.
- Higher values mean more similar semantic meaning.

Retrieval precision means: among retrieved documents, how many were relevant.

\[
\text{Precision} = \frac{\text{relevant retrieved documents}}{\text{all retrieved documents}}
\]

Retrieval recall means: among all relevant documents, how many were retrieved.

\[
\text{Recall} = \frac{\text{relevant retrieved documents}}{\text{all relevant documents}}
\]

## Human-Readable Explanation

The program starts with simple LLM calls and prompt templates, then builds toward systems where the model can search private data, respond through interfaces, call functions, use tools, and collaborate with other agents. RAG is the central bridge: it connects model reasoning to external knowledge by retrieving context before generation.

Vector databases make RAG practical by storing dense numerical representations of text, images, or other objects. Agent frameworks then add control flow: which tool should be used, what state should be remembered, whether another agent should verify the answer, and when the workflow should stop.

## Key Code Patterns

Basic RAG flow:

```python
documents = loader.load()
chunks = splitter.split_documents(documents)
vectorstore = VectorStore.from_documents(chunks, embedding_model)
retriever = vectorstore.as_retriever()
answer = chain.invoke({"question": user_question})
```

Agent flow:

```python
tools = [search_tool, calculator_tool]
agent = create_agent(llm=llm, tools=tools)
response = agent.invoke({"input": user_request})
```

## Common Mistakes

- Passing too much context instead of retrieving the most relevant chunks.
- Treating vector similarity as the same thing as factual correctness.
- Building agents without tool schemas or termination conditions.
- Skipping evaluation of retrieval quality.
- Letting multi-agent systems duplicate work without clear roles.

## Takeaways

The track is about building LLM systems, not just prompting models. The recurring pattern is: structure the input, retrieve or compute supporting context, constrain the model with tools or schemas, and verify the result.
