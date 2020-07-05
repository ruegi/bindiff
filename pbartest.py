######
# The MIT License (MIT)
# Copyright (c) 2016 Vladimir Ignatev
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software
# is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
######

######
# made
#	in Decembre 28 of 2015
#	by @vladignatyev
#	at https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
# modified
#	in May 6 of 2018
#	by Leonardo Da Vinci. Git - @davincif
#	at https://gist.github.com/davincif/3e1cb5ef1c4007d4f5ca690d68db8e7b
# verändert
# 2020-07-5 Michael Rüsweg-Gilbert
# 2. Parm in Func progress: geändert in current
######

import sys

class ProgressBar():
	background = None
	load = None
	head = None
	size = None
	count = 0
	
	def __init__(self, background, load, size, head=''):
		self.background = background
		self.load = load
		self.head = head
		self.size = float(size)
	
	def progress(self, curr, status='', flush=True):
		bar_len = 60
		filled_len = int(round(bar_len * curr / self.size))

		percents = round(100 * curr / self.size, 2)
		if(self.head is None):
			bar = self.load * filled_len
		else:
			bar = self.load * (filled_len - 1) + self.head
		
		bar = bar + self.background * (bar_len - filled_len)
		str2print = f"[{bar}] {percents}%% ... {status}"

		sys.stdout.write('%s\r' % (' ' * len(str2print)))
		
		# print("{}\r".format(' ' * len(str2print)), end='', flush=flush)
		# print(str2print, end="", flush=flush)

		if(flush):
		  sys.stdout.write(str2print)
		  sys.stdout.flush()  # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)
		else:
		  print(str2print, end="", flush=flush)

#run tests
def main():
	from time import sleep

	pb = ProgressBar('-', '=', 10, head='>')
	pb.progress(0)
	for i in range(2):
		pb2 = ProgressBar('-', '#', 200, head='>')
		for idx in range (200):
			pb2.progress(1)
			sleep(0.01)
		print('\n')
		pb2.progress(0, status="Null Test")
		pb.progress(5)


if __name__ == '__main__':
	main()
