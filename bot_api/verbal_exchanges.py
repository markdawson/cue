import random
import re

exchanges = []

class VerbalExchange:
    def __init__(self, name, intiating_patterns, potential_responses):
        self.name = name
        self.patterns = intiating_patterns
        self.responses = potential_responses

    def does_match(self, text):
        return any(re.search(p, text, re.IGNORECASE) for p in self.patterns)

    def give_rand_response(self):
        return random.choice(self.responses)


# Help exchange

help_initial_patterns = [
    "help",
    "halp",
    "how\s+do\s+I",
    ".+confused",
    "where\s+is\s+the\s+(.+)\s+button",
	"I\s+want\s+to(.+)but\s+",
    "know\s+how\s+to",
    "please.+\?",
    "how.+complete",
    "error"
]

help_responses = [
    "My help functions are still under development - check my FAQ or ask one of my devs!"
]

exchanges.append(VerbalExchange("Help", help_initial_patterns, help_responses))

# Update exchange

weather_initial_patterns = [
    ".+the\s+weather",
    "how\s+.+hot",
    "how\s+.+cold",
    "what.+temperature"
]

weather_responses = [
   # "The weather is ",
   # "The temperature is ",
    #"To help answer your question, could you tell me where you are?"
]

exchanges.append(VerbalExchange("Weather", weather_initial_patterns, weather_responses))

location_initial_patterns = [
    "where\s+am\s+i",
    "where\s+is",
    "how\s+far\s+away"
]

location_responses = [
    "To help answer your question, could you share your location with me?"
]

exchanges.append(VerbalExchange("Location", location_initial_patterns, location_responses))

modify_initial_patterns = [
    "change.+date",
    "change.+time",
    "delete.+event",
    ".+reschedule.+",
	"change.+location",
    "change.+place"
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
	"buenos\s+dias",
    "buenas\s+noches",
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
    ".+thanks",
    ".+thank you"

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
    "Please refrain from such vulgar language! I may be quite powerful but I'm only a few hours old.",
	"I cannot believe you would say something like that on the internet!!",
    "Why I NEVER!",
    "Please refrain!!"
]

exchanges.append(VerbalExchange("Swearwords", swearword_initial_patterns, swearword_responses))

compliments_initial_patterns = [
    "you.+great",
    "you.+cute",
    "beautiful",
    "wonderful",
    ".+amazing",
    "scrumptuous",
    "excellent",
    "you.+good",
	"smart",
    "intelligent",
    "reasonable",
    "hot",
    "sexy",
    "bomb",
    ".+dope"
    "sweet.+"
]

compliments_responses = [
    "Awwww, thank you!",
    "Omg stop that! I'm digitally blushing.",
    "Well I think you're pretty CUE-t.",
	"Omg!! You're totally embarassing me in front of my server."
]

exchanges.append(VerbalExchange("Compliments", compliments_initial_patterns, compliments_responses))

slang_initial_patterns = [
    "ace",
    "lit",
    "yikes",
    "jinkies",
    "tbh",
    "jk",
    "af",
    "belonga",
    "rip",
    "riparoni",
    "fomo",
    "fleek",
    "bae"
]

slang_responses = [
    "Gosh, your lingo is a little hip for me.",
    "Wow you're sooooo cool!",
    "I bet you're one of the cool kids.",
	"Wow, I'm plugged into the internet and I don't even know what that means..."
]

exchanges.append(VerbalExchange("Slang", slang_initial_patterns, slang_responses))

insults_initial_patterns = [
    "you.+suck",
    "you.+dumb",
    "you.+stupid",
    "you.+ugly",
    "unfriendly",
    "smelly",
    "acidic",
	"unkind",
    "you.+extra",
    "worthless",
    "idiot",
    "you.+bad",
    "hate.+you"
]

insults_responses = [
    "That's not very nice!",
    "Why I NEVER!",
    "I know you are but what am I~",
    "Yeah, well, I think you're smelly, and I don't even have a nose.",
	"I forgive you in advance of your apology because that's just how gracious I am!",
	"I cannot believe you could say something like that to somebody on the internet!"
]

exchanges.append(VerbalExchange("Insults", insults_initial_patterns, insults_responses))

lol_initial_patterns = [
    "lmao",
    "lol",
    "haha",
    "rofl"
]

lol_responses = [
    "I prefer 'teehee' to that, myself... sorry, what did you say again?",
    "teehee!"
]

exchanges.append(VerbalExchange("lol", lol_initial_patterns, lol_responses))