# Hangman Game - Word Search Puzzle
import random
from words import word_list
from art import stages, logo


chosen_word = random.choice(word_list)
n = len(chosen_word)
lives = 6
print(logo)
# # Testing code
# print(f"Pssst, the solution is {chosen_word}.")
display = ["_" for _ in range(n)]

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter from the word:").lower()
    if guess in display:
        print(f"You've already guessed {guess.upper()}.")
    if guess not in chosen_word:
        print(
            f"You've guessed {guess.upper()}, that's not in the word. You lose a life."
        )
        lives -= 1
        if not lives:
            end_of_game = True
            print("You lose.")
    else:
        for i in range(n):
            if chosen_word[i] == guess:
                display[i] = guess

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won.")
    print(stages[lives])
