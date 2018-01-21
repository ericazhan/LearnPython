# -*- coding: utf- 8 -*-

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split()
	return words
#split就是拆字喽？大小写无所谓？
#是拆字，大写不可以（连高亮都没有了）。。
#原来三个引号里面的内容，成了这个模块的自带帮助。。

def sort_words(words):
	""" Sorts the words."""
	return sorted(words)
#sorted这个方程待查——单词按首字母排序

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
#pop待查

def print_last_word(words):
	"""Prints the last word after poping it off."""
	word = words.pop(-1)
	print word
#存疑

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
sentence = "There is no free lunch."
aa = break_words(sentence)
print aa	
	
	
	
	
	
