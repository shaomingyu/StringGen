import prefix, suffix
from functools import reduce

def get_word_list(chain, pre, randomizer, int, NONWORD):
	return tuple(get_word_list_helper(int, [], chain, pre, randomizer, NONWORD))

def get_word_list_helper(int, lis, chain, pre, randomizer, NONWORD):
	if int is 0:
		return lis
	word = suffix.choose_word(chain, pre, randomizer)
	if word is NONWORD:
		return lis
	lis.append(word)
	return get_word_list_helper(int - 1, lis, chain, prefix.shift_in(pre, word), randomizer, NONWORD)

def generate(chain, randomizer, int, NONWORD):
	return reduce((lambda x, y: x + " " + y), get_word_list(chain, ('\n', '\n'), randomizer, int, NONWORD))
