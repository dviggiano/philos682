import copy

from constants import MAX_TOKENS, NUM_TRIALS

from typing import Iterable, Callable

import anthropic
import csv
import datetime
import dotenv
import google.generativeai
import openai
import os
import dataclasses


models = [
    "GPT-4",
    "Gemini",
    # "Claude"
]

dotenv.load_dotenv()
gpt = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
google.generativeai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
gemini = google.generativeai.GenerativeModel(model_name='gemini-pro')
# claude = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))


def ask_llm(prompt: str, model: str) -> str:
    match model:
        case 'GPT-4':
            response = gpt.chat.completions.create(
                model='gpt-4',
                messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                    }
                ]
            )
            output = response.choices[0].message.content.strip()
            return output
        case 'Gemini':
            while True:  # rerun if error is encountered
                try:
                    response = gemini.generate_content(prompt)
                    output = response.text
                    return output
                except:
                    continue
        case 'Claude':  # unused
            # response = claude.messages.create(
            #     model='claude-3-opus-20240229',
            #     messages=[
            #         {
            #             'role': 'user',
            #             'content': prompt
            #         }
            #     ],
            #     max_tokens=MAX_TOKENS
            # )
            # output = response.content[0].text
            # return output
            return ''


@dataclasses.dataclass
class ConversationPoint:
    prompt: str | Callable[[], str]
    use_context: bool


def converse_with_llm(prompts: Iterable[ConversationPoint], model: str) -> str:
    conversation = ""

    while prompts:
        prompt = prompts[0]  # grab next prompt
        conversation += f"User: {prompt.prompt}\n"
        response = ask_llm(prompt=conversation if prompt.use_context else prompt.prompt, model=model)
        conversation += f"LLM: {response}\n"
        prompts = prompts[1:]  # advance in conversation

    return conversation


def get_timestamp() -> str:
    timestamp = datetime.datetime.now()
    formatted_timestamp = timestamp.strftime("%m/%d/%Y %H:%M:%S")
    return formatted_timestamp


def run_trials(filename: str, prompts: Iterable[str | Callable[[], str] | Iterable[ConversationPoint]]):
    headers = [
        "Prompt",
        "Model",
        "Trial",
        "Response",
        "Timestamp"
    ]

    results = []

    for prompt in prompts:
        print(prompt)

        for model in models:
            for trial in range(1, NUM_TRIALS + 1):
                if callable(prompt):
                    actual_prompt = prompt()  # call function to generate final prompt
                elif type(prompt) == str:
                    actual_prompt = prompt
                else:
                    actual_prompt = copy.deepcopy(prompt)

                if all(type(item) == ConversationPoint for item in actual_prompt):
                    for conversation_point in actual_prompt:
                        if callable(conversation_point.prompt):
                            conversation_point.prompt = conversation_point.prompt()

                results.append([
                    actual_prompt if type(actual_prompt) == str else
                    [conversation_point.prompt for conversation_point in actual_prompt],
                    model,
                    trial,
                    ask_llm(prompt=actual_prompt, model=model) if type(actual_prompt) == str else
                    converse_with_llm(prompts=actual_prompt, model=model),
                    get_timestamp()
                ])

                print(f"\t{model}, trial {trial}")

    with open(f'results/{filename}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(results)
