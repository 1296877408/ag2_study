import json

from pydantic import BaseModel

from autogen import ConversableAgent, LLMConfig

# 1. Define our lesson plan structure, a lesson with a number of objectives
class LearningObjective(BaseModel):
    title: str
    description: str

class LessonPlan(BaseModel):
    title: str
    learning_objectives: list[LearningObjective]
    script: str

# 2. Add our lesson plan structure to the LLM configuration
llm_config = LLMConfig(
    api_type="openai",
    model="gpt-4o-mini",
    api_key="sk-eiQ4kuFQCV83365trDk6nzOHpiXJSXiIY2mWDzUnCwhqc04q",
    base_url="https://api.openai-proxy.org/v1",
    response_format=LessonPlan,
)

# 3. The agent's system message doesn't need any formatting instructions
system_message = """You are a classroom lesson agent.
Given a topic, write a lesson plan for a fourth grade class.
"""

with llm_config:
    my_agent = ConversableAgent(
        name="lesson_agent",
        system_message=system_message
    )

# 4. Chat directly with our agent
response = my_agent.run(message="In one sentence, what's the big deal about AI?")

# 5. Iterate through the chat automatically with console output
response.process()

# 6. Get and print our lesson plan
lesson_plan_json = json.loads(response.messages[-1]["content"])
print(json.dumps(lesson_plan_json, indent=2))