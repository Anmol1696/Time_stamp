import time
from .table.py import *
from .wordtonum.py import num

class Time:
	def _init_(self, sentence):
		self.sen = sentence.lower()
		self.timedate = time.strftime("%M %H %d %m %y")
		self.uppervalue = [59, 24, 31, 2200]
		self.lowervalue = [0,0, 1, 1970]
		self.time_clause = []
		self.time_phrase = 0
	
	def cheack(self, ind):
		if self.timedate[ind] >= self.uppervalue[ind] and ind < 4:
			self.timedate[ind + 1] += self.timedate[ind]/self.uppervalue[ind] + 1
			self.timedate[ind] = self.timedate[ind]%self.uppervalue[ind]
		if self.timedate[ind] <= self.lowwervalue[ind] and ind >= 0:
			self.timedate[ind + 1] -= self.timedate[ind]/self.uppervalue[ind] + 1
			self.timedate[ind] = self.timedate[ind]/self.uppervalue[ind]
	
	def time_operation(self, value, ind, opp):
		if opp = "add":
			self.timedate[ind] += value
		elif opp = "sub":
			self.timedate[ind] -= value
		elif opp = "set":
			self.timedate[ind] = value
	
	def finding_num(self):
		words = self.sen.split(" ")
		temp_list = [name[0] for name in word_list]
		for word in words
			try:
				if word in temp_list: self.time_clause.append((word, temp_list.index(word), 'word_list'))
				try: 
					temp = int(word)
					self.time_clause.append((word, temp, 'int'))
				except:
					pass
				
				try:
					temp = num(word)
					self.time_clause.append((word, temp, 'num'))
				except:
					pass
			except:
				pass
		
		x = words.index(self.time_clause[0][0])
		if x >= 3: temp = x - 3
		else: temp = 0
		
		if len(self.time_clause) == 1:	
			self.time_phrase = words[temp:x + 3]
		elif len(self.time_clause) == 0:
			print 'No refference of date, day, or time'
			return None
		else:
			last = words.index(self.time_clause[-1][0])
			self.time_phrase = words[temp:last + 3]
		
		return (self.time_clause, self.time_phrase)
	
	def guessing_timestamp(self):
		# to do => opp, value, type
		to_do = {
			'opp' = '',
			'value' = [0 for x in range(5)],
			'type' = ''
		}
		
		# Add, Set, Sub
		opp = {
			'add' = 0,
			'set' = 0,
			'sub' = 0
		}
		# Stamp, Triger, Period
		triger = {
			'S' = 0,
			'P less' = 0,
			'P more' = 0
		}
		
		new_time = [0 for x in range(5)]
		
		helper = [name[0] for name in helper_list]
		time_word = [name[0] for name in self.time_clause]
		temp_list = [name[0] for name in word_list] + time_word
		
		time_opp = [name[1] for name in self.time_clause]
		time_value = [name[2] for name in self.time_clause]
		ind = []
		val = []
		for word in self.time_phrase:
			if word in helper:
				lis = helper_list[helper.index(word)][4].split('/')
				rank = helper_list[helper.index(word)][1]
				for x in ['add','set','sub']: 
					opp[x] += 1
				for x in ['S','P less','P more']:
					triger[x] += 1
			if word in temp_list:
				try:
					ind.append(word_list[temp_list.index(word)][5])
				except:
					val.append(time_value[time_word.index(word)])
					opp[time_opp[time_word.index(word)]] += 1
			