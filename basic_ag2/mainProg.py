import autogen
import os
import logging

# logging.basicConfig(level=logging.DEBUG)
from autogen import UserProxyAgent, LLMConfig
from autogen.agentchat.contrib.captainagent import CaptainAgent


def build_llm_config(model_name):
    config_list = [
        {
            "model": "gpt-4o-mini",
            "api_key": "sk-t0JeUhkUiPkaoMuD1556E419324d4f06878aD06114A2D2D1",
            "base_url": "http://89.169.98.193:30007/v1",  # This for local model
            "price": [10, 10],
        },
        {
            "model": "/data/models/deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
            "api_key": "sk-t0JeUhkUiPkaoMuD1556E419324d4f06878aD06114A2D2D1",
            "base_url": "http://89.169.98.193:30007/v1",  # This for local model
            "price": [10, 10],
        },
    ]

    # Function to filter a specific model
    def get_config_by_model(config_list, model_name):
        for config in config_list:
            if config["model"] == model_name:
                return config
        return None

    selected_model = model_name
    config = get_config_by_model(config_list, selected_model)

    if config:
        print(f"Configuration for {selected_model}:")
        print(config)
        return LLMConfig(config_list=[config])
    else:
        print(f"No configuration found for model: {selected_model}")
        return None

    config_list = [config]

    llm_config = {"temperature": 0, "config_list": config_list}

    return llm_config


llm_config = build_llm_config("gpt-4o-mini")

## build agents
captain_agent = CaptainAgent(
    name="captain_agent",
    llm_config=llm_config,
    # code_execution_config={"use_docker": False, "work_dir": "groupchat"},
    agent_config_save_path=None,  # If you'd like to save the created agents in nested chat for further use, specify the save directory here
)
captain_user_proxy = UserProxyAgent(name="captain_user_proxy", human_input_mode="NEVER")

result = captain_user_proxy.initiate_chat(
    captain_agent,
    message="Find a recent paper about large language models on arxiv and find its potential applications in role play.",
    max_turns=1,
)
