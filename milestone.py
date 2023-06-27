import random

class Hangman:
	def __init__(self, word_list, num_lives=5):
		self.word_list = word_list
		self.word = random.choice(self.word_list)
		self.word_guessed = [""] * len(self.word)
		word_as_list = [char for char in self.word]
		main_list = [item for item in word_as_list if item != self.word_guessed]
		self.num_letters = len(main_list)
		self.num_lives = num_lives
		self.list_of_guesses = []

	def check_guess(self, guess):
		guess = guess.lower()
		i = 0
		if guess in self.word:
			print(f"Good guess! {guess} is in the word!")
			for char in self.word:
				if guess == char:
					self.word_guessed[i] = guess
				i+=1
			self.num_letters -=1
		else:
			self.num_lives -=1
			print(f"Too bad, {guess} is not in the word.")
			print(f"You have {self.num_lives} left.")

	def ask_for_input(self):
		while True:
			guess = input("Please guess a letter")
			if len(guess) > 1:
				print("Invalid letter. Please enter a single alphabetical character")
			elif guess in self.list_of_guesses:
				print("You already tried that letter")
			else:
				self.check_guess(guess)
				self.list_of_guesses.append(guess)

hangman = Hangman(['apple','banana','cherry'])
hangman.ask_for_input()
