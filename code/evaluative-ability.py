"""
Demonstrations of LLMs comprehending LLM outputs and produce descriptive evaluations of their impact and value.
"""

import csv
from common import run_trials

prompt = "User: What makes this insight valuable?"
prompts = []
filenames = [  # use existing results
    'results/e-creativity.csv',
    'results/t-creativity.csv'
]

for filename in filenames:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        for row in reader:
            model = row[1]
            response = row[3].replace("LLM: ", f"{model}: ")
            prompts.append(response + prompt)

run_trials(filename='evaluative-ability', prompts=prompts)
