'''
solving_cryptoarith_puzzle.py solves cryptoarithmetic puzzles, e.g. send+more=money, where each
letter is uniquely mapped to a digit. The program was encouraged by "Artificial Intelligence: A Modern Approach" by
Peter Norvig and Stuart Russell and Peter Norvig's "Solving Every Sudoku Puzzle".
'''

import time

# input
addend_1 = input('1st addend: ')
addend_2 = input('2nd addend: ')

summand = input('summand: ')

print('working on that...')

# test data
# addend_1 = 'fss'
# addend_2 = 'tho'
# summand = 'ezz'

#test solution
# letters = 'fsthoez'
# numbers = '5623480'
# test_values = {}
# for i in range(len(letters)):
#     test_values[letters[i]] = numbers[i]
# print(test_values)


# tip: when constructing a list in python, variables are passed by value
wrd_lst = [addend_1, addend_2, summand]


# check if summand is not shorter than addends
if len(summand) < len(addend_1) or len(summand) < len(addend_2):
    print('I\'m afraid your entries are faulty.')

# split words into char lists and build a set of letters (needed as keys to dict)
sp_wrd_lst = [list(addend_1), list(addend_2), list(summand)]
set_of_letters = set()
for i in sp_wrd_lst:
    for l in i:
        set_of_letters.add(l)
# print(set_of_letters)


# tip: 'for' loop saves the value of iterating variable, e.g. l in the loop below
# build an initial dictionary
values = {}
for l in set_of_letters:
    values[l] = '1234567890'
# print(values)


# tip: str.replace(old, new) returns a string, does not manipulate the string itself
# eliminate val in values[letter]
def eliminate(values, letter, val):

    if val not in values[letter]:
        return values

    values[letter] = values[letter].replace(val, '')

    if len(values[letter]) == 0:
        return False
    elif len(values[letter]) == 1:
        tmp_val = values[letter]
        if not all(eliminate(values, tmp_let, tmp_val) for tmp_let in set_of_letters.difference({letter})):
            return False

    for v in values.keys():
        if len(values[v]) == 0:
            return False
        elif len(values[v]) == 1:
            if not assign(values, v, values[v]):
                return False
    return values


# assigns each letter a value
def assign(values, letter, val):
    other_values = values[letter].replace(val, '')
    if all(eliminate(values, letter, tmp_val) for tmp_val in other_values):
        return values
    else:
        return False


# turns a string word into an int based on each letter's value in values
def wrd_to_int(word, values):
    tmp = 0
    for s in word:
        tmp = tmp * 10 + int(values[s])
    return tmp
# print(wrd_to_int('money', eliminate(solution, '', '012345678')))


# check if the values that we have found fits the equality
def check_sum(a1, a2, s, values):
    if wrd_to_int(a1, values) + wrd_to_int(a2, values) == wrd_to_int(s, values):
        print("true")
        return True
    else:
        return False


# search function
def search(values):
    if values is False:
        return False
    if all(len(values[l]) == 1 for l in set_of_letters):
        if check_sum(addend_1, addend_2, summand, values):
            return values
        else:
            return False
    n,l = min((len(values[l]), l) for l in set_of_letters if len(values[l]) > 1)
    return some(search(assign(values.copy(), l, v)) for v in values[l])


# returns first non-false element in sequence
def some(seq):
    for e in seq:
        if e:
            return e
    return False


# prints pretty output
def pretty_print(values):
    if values is False:
        print('No solution found. Sorry.')
    else:
        print(addend_1 + '+' + addend_2 + '=' + summand)
        print(str(wrd_to_int(addend_1, values)) + '+' + str(wrd_to_int(addend_2, values)) + '=' + str(wrd_to_int(summand, values)))


# if the summand is one letter more than both of addends then its left-most letter must be 1
if len(summand) - 1 == len(addend_1) and len(summand) - 1 == len(addend_2):
    assign(values, summand[0], '1')


# search itself
start = time.time()
pretty_print(search(values))
end = time.time()
print('time elapsed: ' + str(end - start) + ' seconds')


# todo: leading letters should not be 0's (I moved 0 to the end when initiating values dict, so somewhat completed)
# todo: how to make it faster (?)

