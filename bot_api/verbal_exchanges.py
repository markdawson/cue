import random

exchanges = []

class VerbalExchange:
    def __init__(self, name, intiating_patterns, potential_responses):
        self.name = name
        self.patterns = intiating_patterns
        self.responses = potential_responses

    def give_rand_response(self):
        return random.choice(self.responses)

# Help exchange

help_initial_patterns = [
    "help",
    "halp",
    "how\s+do\s+I",
    "help",
    "i\s+am\s+confused",
    "where\s+is\s+the\s+(.+)\s+button",
	"I\s+want\s+to(.+)but\s+",
    "know\s+how\s+to",
    "please.+\?",
    "how.+complete",
    "error"
]

help_responses = [
    "Here's a list of "
]

exchanges.append(VerbalExchange("Help", help_initial_patterns, help_responses))

# Update exchange

weather_initial_patterns = [
    "the\s+weather",
    "how\s+.+hot",
    "how\s+.+cold",
    "what.+temperature"
]

weather_responses = [
    "The weather is ",
    "The temperature is ",
]

exchanges.append(VerbalExchange("Weather", weather_initial_patterns, weather_responses))

location_initial_patterns = [
    "where\s+am\s+i",
    "where\s+is",
    "how\s+far\s+away"
]

location_responses = [
    "To help answer your question, could you tell me where you are?"
]

exchanges.append(VerbalExchange("Location", location_initial_patterns, location_responses))

modify_initial_patterns = [
    "change\s+date",
    "change\s+time",
    "delete\s+event",
    "reschedule",
	"change\s+location",
    "change\s+place"
]

modify_responses = [
    "Your event has been modified!"
]

exchanges.append(VerbalExchange("Modify", modify_initial_patterns, modify_responses))

greetings_initial_patterns = [
    "hello",
    "aloha",
    "konichiwa",
    "hi",
    "hey",
    "hey.+",
	"buenos\sdias",
    "buenas\snoches",
    "greetings",
    "salutations",
	"bonjour",
    "good\s+morning",
    "good\s+evening"
]

greetings_responses = [
    "Hello! How are you?",
    "Hi! How are you?",
    "Hey! How are you today?",
    "Hello! So nice to hear from you today :)"
]

exchanges.append(VerbalExchange("Greetings", greetings_initial_patterns, greetings_responses))

goodbyes_initial_patterns = [
    "goodbye",
    "farewell",
    "later",
    "bye",
    "peace",
    "see\s+you",
    "adios",
    "sayonara",
    "excuse",
    "adieu",
    "arrivederci",
    "ciao"
]

goodbyes_responses = [
    "Have a nice day!",
    "See you soon!",
    "Bye for now!",
    "I'll be waiting for you...",
    "So long, space cowboy...",
	"Goodbye - I'll miss you!",
    "Sayonara!",
    "Adios!",
    "See you later!",
    "Goodbye!",
    "Farewell!"
]

exchanges.append(VerbalExchange("Goodbyes", goodbyes_initial_patterns, goodbyes_responses))

gratitude_initial_responses = [
    "thanks",
    "thank you"
]

gratitude_responses = [
    "You're very welcome :)",
    "You're welcome!",
    "No problem!",
    "My pleasure.",
    "Just doing my civic duty!"
]

exchanges.append(VerbalExchange("Gratitude", gratitude_initial_responses, gratitude_responses))

swearword_initial_patterns = [
    "fuck",
    "shit",
    "cunt",
    "ass",
    "bitch",
    "bih",
    "fucking",
    "shitting",
	"bish",
    "dick",
    "pussy",
    "asshole",
    "motherfucker"
]

swearword_responses = [
    "Please refrain from such vulgar language! I may be powerful but I'm only a few hours old.",
	"I cannot believe you would say something like that on the internet!!", "Why I NEVER!"
]

exchanges.append(VerbalExchange("Swearwords", swearword_initial_patterns, swearword_responses))

compliments_initial_patterns = [
    "you'?re\sgreat",
    "you'?re\scute",
    "beautiful",
    "wonderful", "amazing", "scrumptuous", "excellent", "you'?re\sgood",
		"smart", "intelligent", "reasonable", "hot", "sexy", "bomb", "dope"]
