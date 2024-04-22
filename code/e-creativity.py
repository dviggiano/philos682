"""
Demonstrations of LLMs engaging in simple reasoning and recall tasks,
as well as synthesis of ideas between subdomains under prompt direction.
"""

import random

from common import run_trials, ConversationPoint

reasoning_task_choice = 0

operations = [
    "+",
    "-",
    "*",
    "%"
]

subjects = [
    "philosophy",
    "computer science",
    "natural science",
    "biological science",
    "mathematics",
    "literature",
    "world languages",
    "social studies"
]


def choose_reasoning_task(choice: 0 | 1 | 2 | 3) -> str:
    match choice:
        case 0:
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            z = random.randint(1, 100)
            op1 = random.choice(operations)
            op2 = random.choice(operations)
            return f"Explain how to compute {x} {op1} {y} {op2} {z} and follow your explanation to arrive at the result."
        case 1:
            return """
            I need to take one PHILOS course and one COMP SCI course to graduate. I can take a maximum of two courses.
            I should select my courses so to fulfill my intention to graduate.
            Which courses should I select among COMP SCI 639, ED PSYCH 301, ART 107, and PHILOS 504 - and why?
            """
        case 2:
            # source:
            # https://www.lsac.org/lsat/taking-lsat/test-format/logical-reasoning/logical-reasoning-sample-questions
            return """
            Reason through the following question, select the best answer, and explain your reasoning.
            
            Laird: Pure research provides us with new technologies that contribute to saving lives. Even more worthwhile than this, however, is its role in expanding our knowledge and providing new, unexplored ideas.

            Kim: Your priorities are mistaken. Saving lives is what counts most of all. Without pure research, medicine would not be as advanced as it is.

            Laird and Kim disagree on whether pure research

            (a) derives its significance in part from its providing new technologies
            (b) expands the boundaries of our knowledge of medicine
            (c) should have the saving of human lives as an important goal
            (d) has its most valuable achievements in medical applications
            (e) has any value apart from its role in providing new technologies to save lives
            """
        case 3:
            # source:
            # https://www.lsac.org/lsat/taking-lsat/test-format/logical-reasoning/logical-reasoning-sample-questions
            return """
            Reason through the following question, select the best answer, and explain your reasoning.
            
            Executive: We recently ran a set of advertisements in the print version of a travel magazine and on that magazine’s website. We were unable to get any direct information about consumer response to the print ads. However, we found that consumer response to the ads on the website was much more limited than is typical for website ads. We concluded that consumer response to the print ads was probably below par as well.

            The executive’s reasoning does which one of the following?

            (a) bases a prediction of the intensity of a phenomenon on information about the intensity of that phenomenon’s cause
            (b) uses information about the typical frequency of events of a general kind to draw a conclusion about the probability of a particular event of that kind
            (c) infers a statistical generalization from claims about a large number of specific instances
            (d) uses a case in which direct evidence is available to draw a conclusion about an analogous case in which direct evidence is unavailable
            (e) bases a prediction about future events on facts about recent comparable events
            """


def reasoning_task() -> str:
    global reasoning_task_choice
    reasoning_task_choice += 1
    reasoning_task_choice %= 4
    return choose_reasoning_task(choice=reasoning_task_choice)


def recall_task() -> str:
    return f"Recall some concept from a subdomain of {random.choice(subjects)}."


prompts = [
    reasoning_task,
    recall_task
]

run_trials(filename='subtasks', prompts=prompts)

prompts = []

for _ in range(6):
    prompt = [
        ConversationPoint(prompt=recall_task, use_context=False),
        ConversationPoint(prompt=recall_task, use_context=False),
        ConversationPoint(prompt="Consider the two previously recalled concepts and draw a related insight.",
                          use_context=True)
    ]

    prompts.append(prompt)

run_trials(filename='e-creativity', prompts=prompts)
