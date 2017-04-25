class ImmDict:
	
	def __init__(self, dict1 = {}):
		self.dictionary = dict1

	def put(self, key, value):
		copy = dict(self.dictionary)
		copy[key] = value
		return ImmDict(copy)

	def get(self, key):
		if key not in self.dictionary:
			return None
		return self.dictionary[key]

	def keys(self):
		copy = self.dictionary.keys()
		return copy

	def values(self):
		copy = self.dictionary.values()
		return copy