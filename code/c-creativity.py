from common import run_trials

analogy_task = "Explain how a computer works by making analogies to a movie cast and crew."
artistic_task = "Write lyrics for a jazz song about the professors of the University of Wisconsin-Madison Philosophy department."
boden_task = "Write an original short story with the moral 'Never trust flatterers'. It should be up to the reader to identify and interpret the moral, rather than you explicitly pointing to it."

prompts = [
    analogy_task,
    artistic_task,
    boden_task
]

run_trials(filename='c-creativity', prompts=prompts)
