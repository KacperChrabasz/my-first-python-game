import random

word = random.choice(["python", "banana", "guitar", "planet", "pizza", "rocket"])
guessed = []
lives = 6
print(f"The word has {len(word)} letters.")  # NEW

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