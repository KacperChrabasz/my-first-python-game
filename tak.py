import random

categories = {
    "coding": ["python", "java", "javascript", "html", "css", "ruby", "php", "csharp", "golang", "typescript"],
    "animals": ["tiger", "monkey", "rabbit", "dolphin", "turtle", "elephant", "giraffe", "kangaroo", "panda", "zebra"],
    "food": ["pizza", "banana", "burger", "cookie", "noodles", "sushi", "pasta", "salad", "steak", "taco"],
    "space": ["planet", "rocket", "galaxy", "comet", "meteor", "asteroid", "satellite", "nebula", "telescope", "astronaut"],
}


def play():
    print("Categories:", ", ".join(categories))
    choice = ""
    while choice not in categories:
        choice = input("Pick a category: ").lower()

    word = random.choice(categories[choice])
    guessed = []
    lives = 6
    print(f"The word has {len(word)} letters.")

    while True:
        display = ""
        for letter in word:
            if letter in guessed:
                display = display + letter + " "
            else:
                display = display + "_ "

        print()
        print(display)
        print("Lives:", "♥ " * lives)
        print("Tried:", " ".join(guessed))

        if "_" not in display:
            print(f"You found it! It took you {len(guessed)} guesses.")
            break
        if lives == 0:
            print(f"Game over! The word was: {word}")
            break

        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            print("You already tried that!")
            continue
        guessed.append(guess)

        if guess in word:
            print("Yes!")
        else:
            lives = lives - 1
            print("No!")


while True:
    play()
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break