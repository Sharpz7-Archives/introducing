"""
https://www.goodhousekeeping.com/life/parenting/a31401884/gender-neutral-baby-names/
"""

MIN_BACKSTORY_LENGTH = 150

# Using some kind of brown corpus might make verb checking easier

REPLACERS = [
    ("yourself", "themselves"),
    ("yours ", "theirs "),
    ("your ", "their "),
    ("Your ", "Their "),
    ("You", "They"),
    ("you.", "them."),

    # Mistake in backstory generator
    ("ofcivilization", "of civilization")
]

EASTER_EGG_REPLACERS = [
    ("wizard", "programmer"),
    ("paladin", "COBOL Programmer"),
    ("war", "cheese-making"),
    ("magic", "programming"),
    ("guild", "MLH Club"),
    ("monster", "COBOL Programmer"),
    ("religion", "Github Org"),
    ("religious", "programming"),
    ("faith", "Tech Stack"),
    ("lord", "Senior Developer"),
    ("crime", "Project Management"),
    ("sword", "laptop"),
    ("gods", "Linux Founders"),
    ("lore", "C Code"),
    ("hermit", "Visual Basic Dev")
]

THEM_WORDS = ["to", "how", "in", "the", "so", "survive", "for"]
THEY_WORDS = [
    "were", "ed", "ld", "nd", "ever", "became", "want", "woke", "saw", "still"
    ]

NAMES = [
    "Bellamy",
    "Charlie",
    "Dakota",
    "Denver",
    "Emerson",
    "Finley",
    "Justice",
    "River",
    "Skyler",
    "Tatum",
    "Jessie",
    "Marion",
    "Jackie",
    "Alva",
    "Ollie",
    "Jodie",
    "Cleo",
    "Kerry",
    "Frankie",
    "Guadalupe",
    "Carey",
    "Tommie",
    "Angel",
    "Hollis",
    "Sammie",
    "Jamie",
    "Kris",
    "Robbie",
    "Tracy",
    "Merrill",
    "Noel",
    "Rene",
    "Johnnie",
    "Ariel",
    "Jan",
    "Casey",
    "Jackie",
    "Kerry",
    "Jodie",
    "Finley",
    "Skylar",
    "Justice",
    "Rene",
    "Darian",
    "Frankie",
    "Oakley",
    "Robbie",
    "Remy",
    "Milan",
    "Jaylin",
    "Devan",
    "Armani",
    "Charlie",
    "Stevie",
    "Channing",
    "Gerry",
    "Monroe",
    "Kirby",
    "Azariah",
    "Santana",
]