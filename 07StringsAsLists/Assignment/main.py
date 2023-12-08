def is_alliteration(word1, word2):
    if word1[0] == word2[0]:
        return True
    return False
print(is_alliteration("apple", "ant"))
print(is_alliteration("cat", "dog"))
print(is_alliteration("elephant", "eagle"))
print("##############")
def count_vowels(word):
    total = 0
    for letters in word:
        if letters in ["a","e","i","o","u"]:
            total = total + 1
    return total

print(count_vowels("apple"))
print(count_vowels("banana"))
print(count_vowels("sky"))
print("###############")
def count_numbers(word):
    total = 0
    for numbers in word:
        if numbers in "1,2,3,4,5,6,7,8,9,0":
            total = total + 1
    return total

print(count_numbers("apple123"))
print(count_numbers("banana"))
print(count_numbers("sky"))
print("#############")
def count_target_letters (word,character):
    total = 0
    for characters in word:
        if characters in word:
            if characters in character:
                total = total + 1
    return total

print(count_target_letters("apple", "a"))
print(count_target_letters("banana", "a"))
print(count_target_letters("", "a"))
print("################")

def in_alphabetical_order(letters):
    previous = letters[0]
    for letter in letters:
        if letter < previous:
            return False
        previous = letter
    return True

print(in_alphabetical_order("abc"))
print(in_alphabetical_order("cba"))
print(in_alphabetical_order("defgh"))

print("###############")
def alternate_case(word):

    nextupper = True 
    result = ""
    for letters in word:
        if nextupper == True:
            result = result + letters.upper()
            nextupper = False 
        elif nextupper == False:
            result = result + letters
            nextupper = True
    return result



print(alternate_case("python"))
print(alternate_case("github"))
print(alternate_case("copilot"))

def remove_vowels(letters):
    newword = ""
    for letter in letters:
        if letter in "aeiou":
            pass
    else:
        result = result + letter
    return result
    
print(remove_vowels("apple"))
print(remove_vowels("banana"))
print(remove_vowels("elephant"))

