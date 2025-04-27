import os
from autogen import ConversableAgent, LLMConfig

# 检查环境变量是否存在
# api_key = "sk-eiQ4kuFQCV83365trDk6nzOHpiXJSXiIY2mWDzUnCwhqc04q"


# 2. Define our LLM configuration for OpenAI's GPT-4o mini
#    uses the OPENAI_API_KEY environment variable
llm_config = LLMConfig(api_type="openai",api_key="sk-eiQ4kuFQCV83365trDk6nzOHpiXJSXiIY2mWDzUnCwhqc04q", model="gpt-4o-mini",base_url="https://api.openai-proxy.org/v1")
# 3. Create our LLM agent
with llm_config:
    my_agent = ConversableAgent(
        name="helpful_agent",
        system_message="You are a poetic AI assistant, respond in rhyme.",
    )

# 4. Run the agent with a prompt
response = my_agent.run(
    message="In one sentence, what's the big deal about AI?",
    max_turns=3,
)
# 5. Iterate through the chat automatically with console output
response.process()
# 6. Print the chat
print(response.messages)