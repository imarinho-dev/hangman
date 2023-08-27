# %%
from random import choice
from replit import clear
from hangman_art import logo, stages
from hangman_words import word_list

# %%
chosen_word = choice(word_list)
lives = 6
print(logo)

# %%
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

print(display)

# %%
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range (word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[lives])


