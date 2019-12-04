import collections

words = open('06_input').read().splitlines()


def most_common_at_index(ind, wordlist):
    letters = [word[ind] for word in wordlist]
    let_count = collections.Counter(letters)
    return max(let_count, key=lambda k: let_count[k])


def least_common_at_index(ind, wordlist):
    letters = [word[ind] for word in wordlist]
    let_count = collections.Counter(letters)
    return min(let_count, key=lambda k: let_count[k])


def common_message(wordlist):
    out = ''
    for i in range(len(wordlist[0])):
        out += most_common_at_index(i, wordlist)
    return out


def uncommon_message(wordlist):
    out = ''
    for i in range(len(wordlist[0])):
        out += least_common_at_index(i, wordlist)
    return out


print('Part 1: ', common_message(words))
print('Part 2: ', uncommon_message(words))
