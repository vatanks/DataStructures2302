
import time

def recursive_anagram(letters, wordset, anagram):
    if len(wordset) == 0:
        return anagram
    else:
        word1 = wordset.pop()
        if letters == sorted(word1):
            anagram.append(word1) 
    return recursive_anagram(letters, wordset, anagram)
    

file = open
with open("alpha.txt", "r") as file:
    lines = [line.strip() for line in file]
Wordset = (set(lines))
print(Wordset)
input_word = input("Enter the word you want to try")
word_letters = sorted(list(input_word))
print(word_letters)
anagrams = list()
start_time = time.time()
print(recursive_anagram(word_letters, Wordset, anagrams))
print("--- %s seconds ---" % (time.time() - start_time))
