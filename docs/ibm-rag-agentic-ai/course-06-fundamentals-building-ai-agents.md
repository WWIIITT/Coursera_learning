# Course 6 - Fundamentals of Building AI Agents

<span class="track-badge rag">IBM RAG & Agentic AI</span>

## What This Covers

This course introduces tools, function calling, LangChain built-in tools, LCEL, manual tool-calling agents, structured outputs, data science agents, visualization agents, and natural-language SQL agents. Local materials include notebooks, readings, cheat sheets, Python scripts, and the Chinook SQL database file.

## Core Ideas

- Agents use an LLM to decide what action to take next.
- Tools expose external capabilities such as search, math, SQL, plotting, or APIs.
- Function calling requires clear schemas so the model can produce structured tool arguments.
- LCEL composes prompts, models, parsers, and functions into pipelines.
- SQL agents convert natural-language questions into database queries, execute them, and explain results.
- Agent systems need guardrails because tool use can create real side effects.

## Important Formulas

Agent loops can be understood as repeated state updates.

\[
s_{t+1} = \operatorname{Update}(s_t, a_t, o_t)
\]

Where:

- \(s_t\) is the current state at step \(t\).
- \(a_t\) is the action chosen by the agent.
- \(o_t\) is the observation returned by the tool.
- \(s_{t+1}\) is the next state.

For SQL aggregation, count returns the number of rows in a group.

\[
\operatorname{COUNT}(*) = \text{number of rows matching the query}
\]

Where:

- The query defines which table, filters, and joins are included.
- The result may be grouped by columns when `GROUP BY` is used.

## Human-Readable Explanation

The course separates plain LLM calls from agentic workflows. A plain LLM responds directly. An agent can inspect the request, choose a tool, observe the result, and continue. This is powerful for tasks where the model needs facts, calculations, database access, or generated charts.

The natural-language SQL agent is a concrete example. It connects a Watsonx Granite model through LangChain to a MySQL Chinook database. The user asks a plain-English question such as "Describe the PlaylistTrack table," and the agent selects SQL inspection or query tools to answer.

## Key Code Patterns

Create a Watsonx-backed LangChain LLM:

```python
model = ModelInference(
    model_id="ibm/granite-3-2-8b-instruct",
    params=parameters,
    credentials=credentials,
    project_id=project_id,
)
llm = WatsonxLLM(model=model)
```

Create a SQL database connection:

```python
mysql_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
db = SQLDatabase.from_uri(mysql_uri)
```

Create a SQL agent:

```python
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,
    handle_parsing_errors=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)
```

## Common Mistakes

- Giving tools vague names or unclear argument schemas.
- Letting agents execute database queries without understanding permissions.
- Hard-coding credentials in scripts.
- Assuming the generated SQL is correct without inspecting verbose traces.
- Creating a multi-step agent when a simple deterministic chain would work.

## Takeaways

Course 6 introduces the agent pattern: the model reasons about which tool to use, tools provide external capability, and observations guide the next step.
