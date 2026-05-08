# Course 8 - Agentic AI with LangGraph, CrewAI, AutoGen, and BeeAI

## What This Covers

This course compares and applies agent orchestration frameworks. Local materials include LangGraph workflow pattern notebooks, CrewAI readings and labs, a nutrition coach app, a structured meal and grocery planner, AG2 AutoGen tutorials, a healthcare multi-agent chatbot, and BeeAI framework materials.

## Core Ideas

- Workflow patterns define how tasks move through agents, tools, and validation steps.
- CrewAI organizes agents around roles, goals, tools, and tasks.
- AG2/AutoGen focuses on conversational multi-agent collaboration.
- BeeAI provides another framework for building agentic systems and coordinating components.
- Multi-agent design should specify roles, communication flow, stopping conditions, and tool boundaries.
- Healthcare and nutrition examples require extra care because outputs can affect user decisions.

## Important Formulas

Task delegation can be represented as assigning each task to the best available role.

\[
\operatorname{assign}(t_i) = \operatorname*{arg\,max}_{a_j} \; \text{fit}(a_j, t_i)
\]

Where:

- \(t_i\) is task \(i\).
- \(a_j\) is agent \(j\).
- \(\text{fit}(a_j,t_i)\) is how well the agent role matches the task.

Conversation rounds limit how long a multi-agent chat can continue.

\[
\text{total messages} \leq \text{number of agents} \times \text{max rounds}
\]

Where:

- Number of agents is the count of participating agents.
- Max rounds is the configured conversation limit.

## Human-Readable Explanation

CrewAI frames agentic work as a team with roles and tasks. For example, a nutrition coach can use separate roles for analyzing dietary needs, planning meals, and producing a shopping guide. The structure makes the output easier to reason about than one large prompt.

AutoGen frames multi-agent work as conversation. Agents speak to each other, critique, refine, and hand off tasks. The healthcare chatbot notebooks use agents with different responsibilities, such as diagnosis-style reasoning, pharmacy-style advice, and consultation summaries. In real applications, these outputs would need strong safety disclaimers and expert review.

BeeAI and LangGraph materials reinforce the same principle: orchestration matters. A useful agentic app is not just many agents; it is a controlled workflow with clear roles, tools, state, and termination behavior.

## Key Code Patterns

CrewAI role and task structure:

```python
researcher = Agent(role="Researcher", goal="Find relevant information")
writer = Agent(role="Writer", goal="Create a clear final response")
task = Task(description="Prepare a meal plan", agent=writer)
crew = Crew(agents=[researcher, writer], tasks=[task])
```

AutoGen group chat pattern:

```python
groupchat = GroupChat(
    agents=[diagnosis_agent, pharmacy_agent, consultation_agent],
    max_round=5,
    speaker_selection_method="round_robin",
)
manager = GroupChatManager(groupchat=groupchat)
```

Structured output pattern:

```python
class NutritionPlan(BaseModel):
    meals: list[str]
    grocery_items: list[str]
    cautions: list[str]
```

## Common Mistakes

- Adding agents when one well-designed workflow would be simpler.
- Letting agents talk indefinitely without a termination condition.
- Giving agents overlapping roles that create repeated answers.
- Treating generated healthcare or nutrition output as professional advice.
- Skipping structured output when downstream code expects predictable fields.

## Takeaways

Course 8 compares orchestration styles. CrewAI emphasizes teams and tasks, AutoGen emphasizes agent conversations, LangGraph emphasizes explicit workflow state, and BeeAI broadens the agentic framework toolkit.
