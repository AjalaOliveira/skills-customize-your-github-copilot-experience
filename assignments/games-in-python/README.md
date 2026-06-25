
# 📘 Assignment: Hangman

## 🎯 Objective

Build a command-line Hangman game in Python that reinforces working with strings, loops, conditionals and user input.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create a playable Hangman game that selects a secret word and lets the player guess letters until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list (in-code or external file).
- Display the current word progress using underscores for unknown letters (e.g., `_ a _ g _ a _`).
- Accept single-letter guesses (case-insensitive) and update the display accordingly.
- Track and display incorrect guesses and remaining attempts.
- Prevent repeated guesses from affecting remaining attempts and inform the player.
- End the game with a clear win or lose message and reveal the secret word on loss.

#### Example session
```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Good guess! Word: _ a _ _ _
Guess a letter: z
Incorrect. Attempts remaining: 5
...
You win! The word was: magic
```

### 🛠️ Optional: Difficulty & Word Source

#### Description
Add difficulty levels (more/ fewer attempts) and/or load words from an external `words.txt` file.

#### Requirements

- Support at least two difficulty levels (e.g., Easy/Hard) that change the allowed attempts.
- If using a `words.txt` file, validate file presence and handle errors gracefully.

---

Place your solution file(s) (e.g., `hangman.py`) in this folder alongside this `README.md`.
