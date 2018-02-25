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
    values[l] = '0123456789'
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


def assign(values, letter, val):
    other_values = values[letter].replace(val, '')
    if all(eliminate(values, letter, tmp_val) for tmp_val in other_values):
        return values
    else:
        return False


def wrd_to_int(word, values):
    tmp = 0
    for s in word:
        tmp = tmp * 10 + int(values[s])
    return tmp
# print(wrd_to_int('money', eliminate(solution, '', '012345678')))


# check
def check_sum(a1, a2, s, values):
    if wrd_to_int(a1, values) + wrd_to_int(a2, values) == wrd_to_int(s, values):
        print("true")
        return True
    else:
        return False


def search(values):
    if values is False:
        return False  # Failed earlier
    if all(len(values[s]) == 1 for s in set_of_letters):
        if check_sum(addend_1, addend_2, summand, values):
            return values  # Solved!
        else:
            return False
    n,s = min((len(values[s]), s) for s in set_of_letters if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])


def some(seq):
    for e in seq:
        if e:
            return e
    return False


def in_grid(values):
    if values == False:
        print('No solution found. Sorry.')
    else:
        print(addend_1 + '+' + addend_2 + '=' + summand)
        print(str(wrd_to_int(addend_1, values)) + '+' + str(wrd_to_int(addend_2, values)) + '=' + str(wrd_to_int(summand, values)))


if len(summand) - 1 == len(addend_1) and len(summand) - 1 == len(addend_2):
    assign(values, summand[0], '1')

in_grid(search(values))

# todo: leading letters should not be 0's
# todo: in case summand has more letters than both addends, the leading letter of the summand should equal 1 (?)
# todo: how to make it faster (?)

