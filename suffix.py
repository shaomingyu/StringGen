from immdict import ImmDict


def empty_suffix():
    return ImmDict({})


def add_word(suffix, word):
    if not suffix.get(word):
        return suffix.put(word, 1)
    else:
        return suffix.put(word, suffix.get(word) + 1)


def choose_word(chain, pre, randomizer):
    dictionary = chain.get(pre)
    output = [x for x in dictionary.keys() for n in range(dictionary.get(x))]
    return output[randomizer(len(output)) - 1]
