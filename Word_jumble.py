# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random
# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "electrical", "difficult", "answer", "xylophone","fighting","institute","spiderweb","flashtime","waves")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
# create a jumble version of the word
jumble = " "
while word:
		position = random.randrange(len(word))
		jumble += word[position]
		word = word[:position] + word[(position+1):]
# create a hint for the player incase of stuck
if correct == "python":
		hint = "It's one of the programming language."
elif correct == "jumble":
		hint = "It is a part of the name of the game."
elif correct == "easy":
		hint = "It is not difficult for u."
elif correct == "electrical":
		hint = "feel the current passed by a nueron in ur brain and answer this as quick as electric current."
elif correct == "difficult":
		hint = "It is not difficult for u."
elif correct == "answer":
		hint = "Ur answer is right in front of u"
elif correct == "xylophone":
		hint = "It's time to ring the bells."
elif correct == "fighting":
		hint = "It's time to spill some blood."	
elif correct == "institute":
		hint = "Stop playing the game and go to some 'place' where u can learn something."
elif correct == "spiderweb":
		hint = "it's so dirty here, try to clean ur room."
elif correct == "flashtime":
		hint = "Let the time stop for a moment."
elif correct == "waves":
		hint = "It is a kind of disturbance."
		
# start the game
print(
"""
		Welcome to Word Jumble!

	   Unscramble the letters to guess the word.
         (Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)
# Let the player to guess
guess = input("\nYour guess: ")
tries = 1
while guess.lower() != correct and guess != "":
		print("Sorry, that's not it.")
		tries += 1
		if tries >= 5:
				answer = input("Press enter key if u want a hint")
				if not answer:
						print(hint)
				else:
						print("It's ok!")
		guess = input("Your guess: ")
if guess.lower() == correct:
		print("That's it! You guessed it in",tries,"tries!")

print("\nThanks for playing.")

input("\n\nPress the enter key to exit.")
