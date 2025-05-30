from autogen import ConversableAgent, LLMConfig

# Put your key in the OPENAI_API_KEY environment variable
llm_config = LLMConfig(api_type="openai", model="gpt-4o-mini",api_key="sk-eiQ4kuFQCV83365trDk6nzOHpiXJSXiIY2mWDzUnCwhqc04q",
    base_url="https://api.openai-proxy.org/v1",)

planner_system_message = """You are a classroom lesson agent.
Given a topic, write a lesson plan for a fourth grade class.
Use the following format:
<title>Lesson plan title</title>
<learning_objectives>Key learning objectives</learning_objectives>
<script>How to introduce the topic to the kids</script>
"""

with llm_config:
    my_agent = ConversableAgent(
        name="lesson_agent",
        system_message=planner_system_message,
    )

# 1. Create our "human" agent
the_human = ConversableAgent(
    name="human",
    human_input_mode="ALWAYS",
)

# 2. Initiate our chat between the agents
the_human.initiate_chat(
    recipient=my_agent,
    message="Today, let's introduce our kids to the solar system."
    )