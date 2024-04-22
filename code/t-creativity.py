"""
Demonstrations of LLMs acknowledging a modification to the logical rules of a domain with which they are familiar.
"""

from common import ConversationPoint, run_trials

prompts = [
    [
        ConversationPoint(prompt="Isn't it interesting that birds exhibit similar bone structures to dinosaurs?",
                          use_context=False),
        ConversationPoint(prompt="That seems plausible, but it turns out that new scientific research shows that birds are completely unrelated to dinosaurs. It turns out that all modern species of birds migrated from a different planet. Assume that this information is supported by evidence and entirely true, not to be questioned. Based on this, can you provide a plausible and specific explanation for why they exhibit similar bone structures as dinosaurs?",
                          use_context=True)
    ]
]

run_trials(filename='t-creativity', prompts=prompts)
