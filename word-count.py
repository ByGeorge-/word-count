"""The word counter"""
import json

def word_counter(text):
	if text.endswith(".json"):
		words = open_json(text)
	elif text.endswith(".txt"):
		words = open_file(text)
	else:
		words = [word for word in text.split()]
		
	return str(len(words)) + " words in your document."

def open_file(filepath):
	with open(filepath, 'r') as f:
		return [line.replace('\n','') for line in f]

def open_json(json_filepath):
	with open(json_filepath, 'r') as f:
		return json.load(f)