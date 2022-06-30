original_word = "Apple"
lives = 10
word = list(original_word.lower())
player_answer = list('_' * len(word))
guessed_letters = []

def validate_guess(guess):
  if type(guess) is not str or len(guess) > 1 or not guess.isalpha():
    return False
  else:
    return True

def handle_correct_guess(guess):
  indices_of_blanks_to_replace = []
  for i in range(len(word)):
    if word[i] == guess:
      indices_of_blanks_to_replace.append(i)

  for i in indices_of_blanks_to_replace:
    player_answer[i] = guess

def handle_wrong_guess(guess):
  global lives
  lives -= 1
  print(f"{guess} is not in the word. You lost a life :(")

# Main process
# 
while player_answer != word and lives > 0:
  print("")
  print(f"{''.join(player_answer)} ({lives} lives left)")
  guess = input("Please guess a letter:\n").lower()
  if not validate_guess(guess):
    print("Your guess must be a single letter.")
    continue

  if guess in guessed_letters:
    print(f"{guess} has already been guessed.")
    continue

  guessed_letters.append(guess)

  if guess in word:
    handle_correct_guess(guess)

  else:
    handle_wrong_guess(guess)

else:
  if player_answer == word:
    print("You win!")

  elif lives <= 0:
    print(f"You lose! The correct word was '{original_word}'")
