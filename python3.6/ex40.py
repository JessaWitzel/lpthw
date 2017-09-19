class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

coconuts = (["I am a lovely bunch of coconuts",
            "I taste delicious and I am so good for you",
            "But if you shake me I'll fall on your head",
            "And knock you out dead"])

my_song = Song(coconuts)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
my_song.sing_me_a_song()
