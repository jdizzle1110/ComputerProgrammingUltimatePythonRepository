import csv
import os

os.chdir(os.pathdirname(os.path.abspath(__file__)))


f = open("../data/400-most-common-english-words.cvs", "r")
words = f.read().split("\n")
f.close()


def find_longest_vowel(words):
    vowel = ""
    vowelcount = 0
    vowelcount2 = 0
    for word in words:
        if word in "aeiou":
            vowelcount = vowelcount + 1



    return vowelcount

print(find_longest_vowel(words))


def average_word_length(words):
    totalWords = 0
    letters = 0
    avg = 0
    for word in words:
        totalWords = totalWords + 1
        letters = letters + len(word)
    avg = letters / totalWords
    return avg 

print(average_word_length(words))

