#-*- coding:utf-8 -*-
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
PHRASES = {
			"class %%%(%%%):":
			"Make a class named %%% that is-a %%%.",
			"class %%%(object):\n\tdef __init__(self,***)":
			"class %%% has-a __init__ that takes self and *** parameters.",
			"class %%%(object):\n\tdef ***(self,@@@)":
			"class %%% has-a function named *** that takes self and @@@ parameters.",
			"*** = %%%()":
			"Set *** to an instance of class %%%.",
			"***.***(@@@):":
			"From *** get the *** function, and call it with parameters self,@@@.",
			"***.*** = '***'":
			"From *** get the *** attribute and set it to '***'."
			}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] =="english":
	PHRASE_FIRST = True

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())    #strip干啥用的？——————去掉空格


def convert(snippet,phrase):
	class_names = [w.capitalize() for w in 
					random.sample(WORDS,snippet.count("%%%"))] #snippet的意思见while段，是key
	other_names = random.sample(WORDS,snippet.count("***"))#sample作用是生成一个WORD的子序列，里面含有的元素数目= “***”在snippet出现的次数
	results = []
	param_names = []
	
	for i in range(0,snippet.count("@@@")):
		param_count = random.randint(1,3)  #返回1 or 2 or 3
		param_names.append(','.join(random.sample(WORDS,param_count)))
		
	for sentence in snippet,phrase:
		result = sentence[:]
		
		#fake class names
		for word in class_names:
			result = result.replace("%%%",word,1)
			
		#fake other names
		for word in other_names:
			result = result.replace("***",word,1)
			
		#fake parameter lists
		for word in param_names:
			result = result.replace("@@@",word,1)
			
		results.append(result)
		
	return results
	

#keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()  #调出pharase这个dictionary的所有keys,无序排列;snippets是完整的字典key list
		random.shuffle(snippets) #把snippets这个key list洗牌，元素重排。
		
		for snippet in snippets: #所以我们现在有了一个小一点的叫做snippets的list，这个列表的每个元素是一个key，叫做snippet
			phrase = PHRASES[snippet] #大写的PHARASE是个字典，小写的phrase是字典的部分value
			question,answer = convert(snippet,phrase)
			if PHRASE_FIRST:
				question,answer = answer,question
				
			print question
			
			raw_input(">")
			print "ANSWER: %s\n\n" %answer
except EOFError:
	print "\nBye"
	


































