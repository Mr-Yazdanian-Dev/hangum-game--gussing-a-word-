import random

# TODO-1 - plz create a random word from the given list
# TODO-2 - user must choose a letter
# TODO-3 - if the letter is in the word, replace that letter with its blank position, else repeat the process, remove one chance to guess, and say you are wrong\

def hangman_game():
    # requirements
    alphabet_list = [
    'a','A','b','B','c','C','d','D','e','E',
    'f','F','g','G','h','H','i','I','j','J',
    'k','K','l','L','m','M','n','N','o','O',
    'p','P','q','Q','r','R','s','S','t','T',
    'u','U','v','V','w','W','x','X','y','Y',
    'z','Z'
    ]
    word_list = [
    # Economics (20)
    "inflation", "deflation", "recession", "investment", "capital",
    "credit", "equity", "dividend", "interest", "market",
    "tariff", "subsidy", "budget", "taxation", "currency",
    "exchange", "trade", "demand", "supply", "competition",

    # Science (20)
    "atom", "molecule", "neutron", "proton", "electron",
    "gravity", "evolution", "photosynthesis", "genetics", "biology",
    "chemistry", "physics", "geology", "astronomy", "ecology",
    "climate", "energy", "radiation", "fusion", "organism",

    # Technology (20)
    "computer", "algorithm", "database", "network", "software",
    "hardware", "internet", "encryption", "cybersecurity", "robotics",
    "artificial", "intelligence", "automation", "virtual", "blockchain",
    "cryptocurrency", "programming", "python", "javascript", "compiler",

    # Arts (20)
    "painting", "sculpture", "music", "theatre", "cinema",
    "literature", "poetry", "novel", "dance", "opera",
    "symphony", "architecture", "photography", "calligraphy", "design",
    "fashion", "aesthetics", "creativity", "culture", "tradition",

    # Sports (20)
    "football", "basketball", "cricket", "baseball", "tennis",
    "golf", "hockey", "rugby", "swimming", "cycling",
    "boxing", "wrestling", "karate", "judo", "archery",
    "gymnastics", "rowing", "skiing", "surfing", "marathon"
    ]
    hangman_stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """
]

    # select the random word    # ok
    word_goal = random.choice(word_list)

    # make a list of underscores for easier replacement    # ok
    word_goal_blank = ["_"] * len(word_goal)               # point

    your_chance = 6
    your_correct_guesses = []

    print("Let's play Hangman!")

    while your_chance > 0:
        print("\nWord:", " ".join(word_goal_blank))        # point

        # ask for guessing a letter                        # ok
        your_letter = input("Enter your letter: ").lower()

        # check if you select a right character            # ok
        if your_letter not in alphabet_list:
            print("Sorry, that's not a valid letter.")
            continue

        if your_letter in word_goal:

            if your_letter in your_correct_guesses:
                print("\nYou've already guessed")
            else:
                print("✅ Correct guess!")
                your_correct_guesses.append(your_letter)
            print(hangman_stages[your_chance])

            for i, letter in enumerate(word_goal):          # point
                    if letter == your_letter:
                        # replace underscore with the guessed letter
                        word_goal_blank[i] = your_letter    # ok

            if "_" not in word_goal_blank:
                print("\n🎉 You win!")
                print("The word was:", word_goal)
                break                                      # point

        else:
            your_chance -= 1
            print(hangman_stages[your_chance])
            print(f"❌ Wrong guess! Chances left: {your_chance}")
            print("-" * 20)

    else:
        print("\n😢 You lost!")
        print("The word was:", word_goal)




hangman_game()