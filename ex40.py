#-*- coding:utf-8 -*-
class Song(object):
	def __init__(self,lyrics):  #init前后 两个 下划线
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])

appy_bday = Song(["q","2","3"])

ulls_on_parade = Song(["ee","ff","gg"])

	

bulls_on_parade = Song(["They rally around the family","With pockects full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

appy_bday.sing_me_a_song()
ulls_on_parade.sing_me_a_song()