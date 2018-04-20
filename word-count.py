"""The word counter"""
import json

def word_counter(text):
	if text.endswith(".json"):
		lines = open_json(text)
		words = [word for word in lines.split()]

	elif text.endswith(".txt"):
		lines = open_file(text)
		words = [word for word in lines.split()]

	# if text is a file I/O object, e.g. with open("text.txt") as f: / wc.word_counter(f) / >>> 420 words in document 
	elif type(text) == "_io.TextIOWrapper": 
		lines = [line for line in list(text)]
		words = [word for word in lines.split()]
		
	else:
		words = [word for word in text.split()]
		
	return str(len(words)) + " words in your document."

def open_file(filepath):
	with open(filepath, 'r') as f:
		return [line.replace('\n','') for line in f]

def open_json(json_filepath):
	with open(json_filepath, 'r') as f:
		return json.load(f)
