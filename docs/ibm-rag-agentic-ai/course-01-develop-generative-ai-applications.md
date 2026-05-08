# Course 1 - Develop Generative AI Applications

<span class="track-badge rag">IBM RAG & Agentic AI</span>

## What This Covers

This course introduces prompt engineering, in-context learning, LangChain basics, and Flask-style application scaffolding. The local materials include an in-context learning notebook, a LangChain notebook, Flask readings, deployment cheat sheets, and a model-selection lab with Python files such as `app.py`, `model.py`, `config.py`, and `llm_test.py`.

## Core Ideas

- Prompt templates make prompts reusable and easier to maintain.
- In-context learning guides model behavior through examples included in the prompt.
- LangChain provides abstractions for models, prompts, chains, and application wiring.
- Flask can expose a generative AI workflow as a web application.
- Model selection depends on task type, cost, latency, context length, and output quality.

## Important Formulas

There are no central mathematical formulas in this course. The practical decision rule is a tradeoff score: choose the smallest model that satisfies quality, latency, and cost requirements.

\[
\text{Model fit} = \text{quality need} + \text{latency need} + \text{cost constraint} + \text{context need}
\]

Where:

- Quality need is how accurate or fluent the answer must be.
- Latency need is how quickly the application must respond.
- Cost constraint is the budget per request or per user.
- Context need is how much source text the model must consider.

## Human-Readable Explanation

The course starts with direct model use: provide instructions, include examples, and inspect output quality. Prompt templates turn these instructions into maintainable building blocks, especially when applications need to insert user questions, context, or formatting instructions.

LangChain adds structure around the model call. Instead of hand-building every prompt and parser, an application can compose model objects, prompt templates, chains, and output handlers. Flask then wraps that workflow in routes so users can interact with it through a web app.

## Key Code Patterns

Use a prompt template:

```python
prompt = PromptTemplate.from_template(
    "Answer the question using this context:\n{context}\n\nQuestion: {question}"
)
```

Separate configuration from model logic:

```python
model = load_model(config.MODEL_ID)
response = model.invoke(user_prompt)
```

Expose an app route:

```python
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", response=response)
```

## Common Mistakes

- Hard-coding model settings throughout the app instead of keeping them in configuration.
- Writing prompts that are too vague to be reused safely.
- Choosing a large model before testing whether a smaller model meets the task.
- Mixing UI, model configuration, and business logic in one file.

## Takeaways

The first course establishes the application pattern: prompts and examples shape model behavior, LangChain organizes model calls, and Flask turns the workflow into a usable service.
