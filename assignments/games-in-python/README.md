
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game in Python to practice string manipulation, loops, conditionals, and user interaction.

## 📝 Tasks

### 🛠️ Create the Hangman Game Engine

#### Description

Implement the core game logic that selects a secret word, tracks guesses, and updates the displayed progress after each guess.

#### Requirements
Completed program should:

- Choose a secret word randomly from a predefined list
- Display the current word progress using underscores for unknown letters, e.g. `_ a _ _ m a n`
- Accept a single letter guess per turn
- Update the displayed progress when the guess is correct
- Track letters already guessed and prevent repeated guesses

### 🛠️ Add Guess Tracking and Win/Lose Logic

#### Description

Build the game flow that counts incorrect guesses, ends the game correctly, and shows the right win or lose message.

#### Requirements
Completed program should:

- Allow a fixed number of incorrect guesses (for example, 6)
- Deduct one attempt when the player guesses a wrong letter
- End the game when the word is fully guessed or attempts run out
- Print a win message with the completed word when the player succeeds
- Print a lose message showing the secret word when the player fails

### 🛠️ Improve Player Feedback

#### Description

Add clear prompts and game status updates so the player always knows what to do next.

#### Requirements
Completed program should:

- Prompt the player with messages like `Enter a letter:`
- Show the current word progress and remaining guesses after each turn
- Notify the player if a guessed letter has already been used
- Use clear messages for winning or losing the game

#### Example Gameplay

```text
Word: _ a _ _ m a n
Guesses left: 5
Enter a letter: n
Good guess! Word: _ a n _ m a n
```