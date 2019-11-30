from autocomplete import predict
from autocomplete.models import train_models
from fast_autocomplete import AutoComplete
from glob import glob


class Magic:
	def __init__(self):
		self.load_autocomplete_markov_chain()
		self.load_autocomplete_trie()
		print("DONE")

	def prediction(self, text):

		# remove non ascii chars
		text = ''.join([i if ord(i) < 128 else ' ' for i in text])

		splited_text = text.split()
		pred = []

		if(len(splited_text) > 1):
			last_word = splited_text[-1]
			second_last_word = splited_text[-2]

			try:
				pred += predict(second_last_word, last_word)
			except Exception as e:
				print("ERROR Markov Chain")
				pass

			text = ' '.join(word.capitalize() for word in text.split()[:-1])
			pred = [text + ' ' + word.capitalize() for word, points in pred]

		try:
			list_prediction = self.Trie.search(text)
			pred += [lp[0] for lp in list_prediction]
			pred = [word.capitalize() for word in pred]

		except Exception as e:
			print("ERROR TRIE")
			pass

		return pred

	def load_autocomplete_trie(self):
		directory = glob('bigData/*')

		words = set()

		for file_name in directory:
			if file_name == 'bigData/bigtext.txt':
				continue

			with open(file_name, 'r') as file:
				for line in file:
					line = line.strip()
					words.add(line)

		words = {word:{} for word in words}

		self.Trie = AutoComplete(words=words)

	def load_autocomplete_markov_chain(self):
		bigString = ''
		
		directory = glob('bigData/*')

		for file_name in directory:
			with open(file_name, 'r') as file:
				for line in file:
					if line[-1] != '\n':
						line += '\n'

					bigString += line

		train_models(bigString)

