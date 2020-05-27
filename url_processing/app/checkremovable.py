"""Checks removable words and removes."""
# pylint: disable=W0312
import re

# some redundant words
WORDS = ["login","signup","contact","mobile","email","mail","phone","signin","sign","comment","name",'*','?']
def email(word):
		"""checks for email."""
		regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
		if(re.search(regex,word)):
			return True
		return False
def mobile(word):
	"""checks for numbers."""
	if len(word) != 10 and len(word) != 12 and len(word)!=11:
		return False
	regex = '^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'
	if(re.search(regex,word)):
		return True
	return False

class Checkremovable():

	"""Initialises class."""
	def __init__(self,data):
		"""init."""
		self.data = data
		self.text = []
	def checkall(self):
		"""process all the redundant words."""
		for line in self.data.split('.'):
			words = line.split(' ')
			# print(words,"hello")
			found = True
			for word in words:
				if word.lower() in WORDS:
					found = False
					break
			for word in WORDS:
				for Word in words:
					if Word.lower() == word:
						found = False
						break
			if found == True:
				self.text += [words]
		# print(self.text)
		num = 0
		for line in self.text:
			for word in line:
				if email(word) == True or mobile(word) == True:
					# print(self.text[num])
					self.text.pop(num)
					num = num - 1
					break
			num = num + 1
		line = ""
		text = ""
		for lists in self.text:
			line = ""
			for word in lists:
				if word != " ":
					line += " " + word
			line += "."
			text += line
		# print(text)
		return text
