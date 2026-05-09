# Course 7 - Agentic AI with LangChain and LangGraph

<span class="track-badge rag">IBM RAG & Agentic AI</span>

## What This Covers

This course focuses on LangGraph, stateful workflows, ReAct-style reasoning, Reflexion agents, structured tool calls, and multi-agent RAG. Local materials include readings on LangGraph architecture, LangGraph versus LangChain, agentic AI, Pydantic tool calls, Reflexion labs, ReAct agents, and a DocChat multi-agent RAG project.

## Core Ideas

- LangChain is useful for chains and tool use; LangGraph is useful for explicit stateful workflows.
- Graph nodes represent steps such as retrieve, research, verify, or answer.
- Edges define control flow, including conditional routing.
- Reflexion patterns let an agent critique and improve its own output.
- ReAct combines reasoning and acting: think, choose tool, observe, continue.
- Multi-agent RAG can separate retrieval, relevance checking, research, and verification.

## Important Formulas

A graph workflow is a set of nodes and edges.

\[
G = (V, E)
\]

Where:

- \(G\) is the workflow graph.
- \(V\) is the set of nodes.
- \(E\) is the set of directed edges between nodes.

State transition means a node reads state and returns an updated state.

\[
s' = f_{\text{node}}(s)
\]

Where:

- \(s\) is the incoming workflow state.
- \(f_{\text{node}}\) is the node function.
- \(s'\) is the updated state passed to the next node.

## Explanation

LangGraph makes the control flow visible. Instead of letting an agent loop implicitly, the developer defines states, nodes, and transitions. This is useful when a workflow needs predictable steps, retries, branching, or human review.

The DocChat project shows a practical multi-agent RAG architecture. A document processor prepares files, a retriever finds candidate context, a relevance checker filters it, a research agent forms an answer, and a verification agent reviews the answer. This division makes each agent's job clearer.

## Key Code Patterns

Define a graph node as a state transformer:

```python
def retrieve_node(state):
    docs = retriever.invoke(state["question"])
    return {"documents": docs}
```

Add conditional workflow routing:

```python
workflow.add_conditional_edges(
    "check_relevance",
    route_after_relevance,
    {"research": "research", "retrieve": "retrieve"}
)
```

Use Pydantic to structure tool arguments:

```python
class SearchInput(BaseModel):
    query: str
    max_results: int = 5
```

## Detailed Study Notes

LangGraph makes state explicit. A graph state is the shared record that moves through the workflow. Each node reads part of the state and returns updates. This is different from a hidden agent loop because the workflow structure is visible in code.

Example state design:

```python
class GraphState(TypedDict):
    question: str
    documents: list
    answer: str
    needs_retry: bool
```

Each node should do one job:

```python
def retrieve(state):
    docs = retriever.invoke(state["question"])
    return {"documents": docs}

def answer(state):
    context = "\n\n".join(doc.page_content for doc in state["documents"])
    response = llm.invoke(f"Context:\n{context}\n\nQuestion: {state['question']}")
    return {"answer": response}
```

Conditional edges turn validation into control flow:

```python
def route_after_check(state):
    if state["needs_retry"]:
        return "retrieve"
    return "final"

workflow.add_conditional_edges("check_answer", route_after_check)
```

Multi-agent RAG benefits from role separation when each role has a measurable purpose: retrieval gets evidence, relevance checking removes weak evidence, research writes the answer, and verification checks whether the answer is supported. If two agents have the same job, they usually add latency without adding reliability.

## Common Mistakes

- Storing important workflow data outside the graph state.
- Creating too many agents without clear responsibilities.
- Skipping verification in RAG answers that cite documents.
- Making routing conditions ambiguous.
- Confusing reflection with guaranteed correctness.

## Takeaways

Course 7 moves from flexible chains to explicit agent workflows. LangGraph is valuable when control flow, state, and verification matter.
