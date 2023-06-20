import random

word_list = ['banana', 'pineapple', 'pear', 'grape', 'apple']
word = random.choice(word_list)

if __name__ == "__main__":
    print(word_list)

    
    print(word)

    guess = input('Please enter a single letter: ')
    if len(guess) == 1 and guess.isalpha:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input!")
    