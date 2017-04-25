import prefix, suffix
from functools import reduce
from immdict import ImmDict

NONWORD = '\n'

def build(file):
	return build_chain(add_to_chain, pairs_gen(file, line_gen), ImmDict())

def build_chain(function, generator, dictionary):
	return reduce(function, generator, dictionary)

def add_to_chain(chain, pair):
	if chain.get(pair[0]) is None:
		return chain.put(pair[0], suffix.add_word(ImmDict(), pair[1]))
	return chain.put(pair[0], suffix.add_word(chain.get(pair[0]), pair[1]))

def line_gen(file):
	o = open(file)
	return (line for line in o)

def pairs_gen(file, generator):
	pre = (NONWORD, NONWORD)
	gen = generator(file)
	for line in gen:
		words = line.split(" ")
		for word in words:
			tup = (pre, word)
			pre = prefix.shift_in(pre, word)
			yield tup
		words = next(generator(file)).split(" ")




