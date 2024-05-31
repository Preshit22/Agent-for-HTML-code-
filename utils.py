import copy
import json
from typing import List
from openai.types.chat import ChatCompletionMessageParam

def pprint_prompt(prompt_messages: List[ChatCompletionMessageParam]):
    print(json.dumps(truncate_data_strings(prompt_messages), indent=4))

def truncate_data_strings(data: List[ChatCompletionMessageParam]):
    cloned_data = copy.deepcopy(data)
    if isinstance(cloned_data, dict):
        for key, value in cloned_data.items():
            if isinstance(value, (dict, list)):
                cloned_data[key] = truncate_data_strings(value)
            elif isinstance(value, str):
                cloned_data[key] = value[:40]
                if len(value) > 40:
                    cloned_data[key] += "..." + f" ({len(value)} chars)"
    elif isinstance(cloned_data, list):
        cloned_data = [truncate_data_strings(item) for item in cloned_data]
    return cloned_data
