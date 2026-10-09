import random

words = ["python", "programming", "computer", "science", "algorithm", "data", "function", "variable", "loop", "condition"]
word = random.choice(words)
guessed = []
lives = 6
guesses = 0

while True:
    display = ""
    for letter in word:
        if letter in guessed:
            display = display + letter + " "
        else:
            display = display + "_ "
    print(display)
    print(f"Lives: {lives}")

    if "_" not in display:
        print(f"You found it! it took you {guesses} guesses.")
        break
    if lives == 0:
        print(f"Game over! The word was '{word}'.")
        break

    guess = input("Guess a letter: ").lower()
    guessed.append(guess)
    guesses = guesses + 1

    if guess in word:
        print("Yes!")
    else:
        lives = lives - 1
        print("No!")