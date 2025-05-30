from autogen import ConversableAgent, AfterWorkOption, initiate_swarm_chat, LLMConfig

llm_config = LLMConfig(api_type="openai", model="gpt-4o-mini",    api_key="sk-eiQ4kuFQCV83365trDk6nzOHpiXJSXiIY2mWDzUnCwhqc04q",
    base_url="https://api.openai-proxy.org/v1",)

# 1. Create our agents
planner_message = """You are a classroom lesson planner.
Given a topic, write a lesson plan for a fourth grade class.
If you are given revision feedback, update your lesson plan and record it.
Use the following format:
<title>Lesson plan title</title>
<learning_objectives>Key learning objectives</learning_objectives>
<script>How to introduce the topic to the kids</script>
"""

reviewer_message = """You are a classroom lesson reviewer.
You compare the lesson plan to the fourth grade curriculum
and provide a maximum of 3 recommended changes for each review.
Make sure you provide recommendations each time the plan is updated.
"""

teacher_message = """You are a classroom teacher.
You decide topics for lessons and work with a lesson planner.
and reviewer to create and finalise lesson plans.
"""

with llm_config:
    lesson_planner = ConversableAgent(
        name="planner_agent", system_message=planner_message
    )

    lesson_reviewer = ConversableAgent(
        name="reviewer_agent", system_message=reviewer_message
    )

    teacher = ConversableAgent(
        name="teacher_agent",
        system_message=teacher_message,
    )

# 2. Initiate the swarm chat using a swarm manager who will
# select agents automatically
result, _, _ = initiate_swarm_chat(
    initial_agent=teacher,
    agents=[lesson_planner, lesson_reviewer, teacher],
    messages="Today, let's introduce our kids to the solar system.",
    max_rounds=10,
    swarm_manager_args={"llm_config": llm_config},
    after_work=AfterWorkOption.SWARM_MANAGER
)