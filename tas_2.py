import random
import sys
def letters(big_string):
    for i in 0, len(big_string):
        l = big_string[i]
        if l.isupper():
            print(l)

def palindrome(pali):
    s = len(pali)
    ss = s/2
    for l in 0, ss:
        if pali[l-1] != pali[-l]:
            return False
    return True

def find_letter(where, letter):
    res = []
    split = where.split(" ")
    for word in split:
        w = word.lower()
        if w[0] == letter:
            res.append(word)
    print(res)

def mix_words(just_string):
    split = just_string.split(" ")
    random.shuffle(split)
    for word in split:
        sys.stdout.write(word + " ")
    print("")



print letters("Trees Are So Kind")

print palindrome("avid diva")

print find_letter("Bears are the best animals ever", 'b')

print mix_words("Bears are the best animals ever")