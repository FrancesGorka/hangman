# Hangman

> Hangman is a classic word guessing game in which a player thinks of a word, and the other player tries to guess that word within a certain number of attempts. This repository contains an implementation of the Hangman game where the computer thinks of a word, and the user tries to guess it.

This repo is divided into multiple project milestones in the form of Python files, each building upon the previous one. The only library imported is 'random', a built-in Python library used to generate random numbers.

## Milestone 2

The computer randomly selects a word from a predefined list. You can run the script, and the selected word will be displayed.

## Milestone 3

Implements the basic functionality of the game. It imports code from milestone2.py and asks the user to input a letter to guess. If the input is a valid letter, it checks whether the letter is in the selected word.

## Milestone 4

Introduces a class-based approach for better organization. The Hangman class manages the game logic, including word selection, guessing, and tracking remaining lives. It prevents repeated guesses and provides feedback based on the guessed letters.

## Milestone 5

Refactors the Hangman class and adds a play_game function that takes a list of words. It allows you to play the Hangman game with multiple words. The game continues until the player wins by guessing the word or runs out of lives.

## Dependencies
This Hangman game implementation is built using Python. No additional libraries or packages are required.
