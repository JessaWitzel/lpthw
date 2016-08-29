class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
happy_bday = Song(["Happy birthday to you",
					"I dont' want to get sued",
					"So I'll stop right there"])
						
bulls_on_parade = Song(["They rally around tha family",
					"With pockets full of shells"])
					
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

rock_a_doodle = Song(["I'm a singing rooster",
					"Who loves the farm",
					"And the farm loves me"])
bachelor_in_paradise = "Almost paradise, Knocking on heaven's door"
bip_song = Song([bachelor_in_paradise])

bip_song.sing_me_a_song()