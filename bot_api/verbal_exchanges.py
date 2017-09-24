import random
import re

exchanges = []

class VerbalExchange:
    def __init__(self, name, intiating_patterns, potential_responses):
        self.name = name
        self.patterns = intiating_patterns
        self.responses = potential_responses

    def does_match(self, text):
        return any(re.match(p, text) for p in self.patterns)

    def give_rand_response(self):
        return random.choice(self.responses)

# Help exchange

help_initial_patterns = [
    "help",
    "halp",
    "how\s+do\s+I"
]

help_responses = [
    "Here's a list of things to help."
]

exchanges.append(VerbalExchange("Help", help_initial_patterns, help_responses))

# Update exchange


