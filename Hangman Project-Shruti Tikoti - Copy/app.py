import random

def select_word():
    words = {
        "python": "A popular programming language",
        "programming": "The process of writing computer code",
        "computer": "An electronic device for processing data",
        "hangman": "A classic word-guessing game",
        "developer": "A person who writes software"
    }
    word, hint = random.choice(list(words.items()))
    return word, hint

def initialize_game(word, hint):
    return {
        "word": word,
        "hint": hint,
        "hidden_word": ["_"] * len(word),
        "guessed_letters": set(),
        "attempts_left": 6,
        "score": 0
    }

def display_hangman(attempts):
    stages = [
        """
           ----
           |  |
           |  O
           | /|\\
           | / \\
          ---
        """,
        """
           ----
           |  |
           |  O
           | /|\\
           | /
          ---
        """,
        """
           ----
           |  |
           |  O
           | /|\\
           |
          ---
        """,
        """
           ----
           |  |
           |  O
           | /|
           |
          ---
        """,
        """
           ----
           |  |
           |  O
           |  |
           |
          ---
        """,
        """
           ----
           |  |
           |  O
           |
           |
          ---
        """,
        """
           ----
           |  |
           |
           |
           |
          ---
        """
    ]
    print(stages[attempts])

def process_guess(game_state, guess):
    word = game_state["word"]
    hidden_word = game_state["hidden_word"]
    guessed_letters = game_state["guessed_letters"]
    
    if guess in guessed_letters:
        return game_state, "Already guessed!"
    
    guessed_letters.add(guess)
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        game_state["score"] += 10  
        return game_state, "Correct guess!"
    
    game_state["attempts_left"] -= 1
    game_state["score"] -= 5  
    return game_state, "Wrong guess!"

def play_hangman():
    word, hint = select_word()
    game_state = initialize_game(word, hint)
    
    print("\nWELCOME TO HANGMAN!\n")
    
    while game_state["attempts_left"] > 0:
        display_hangman(game_state["attempts_left"])
        print(" ".join(game_state["hidden_word"]))
        print(f"Attempts left: {game_state['attempts_left']}")
        print(f"Score: {game_state['score']}")
        print("Type 'hint' if you need help!\n")
        
        guess = input("Guess a letter: ").lower()
        
        if guess == "hint":
            print(f"Hint: {game_state['hint']}\n")
            game_state["score"] -= 10  
            continue
        
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.\n")
            continue
        
        game_state, message = process_guess(game_state, guess)
        print(message + "\n")
        
        if "_" not in game_state["hidden_word"]:
            print(f"Congratulations! You won! The word was '{word}'.")
            print(f"Final Score: {game_state['score']}\n")
            return
    
    display_hangman(game_state["attempts_left"])
    print(f"Game over! The word was '{word}'.")
    print(f"Final Score: {game_state['score']}\n")

if __name__ == "__main__":
    play_hangman()
