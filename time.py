import time

class Time:
	def _init_(self, sentence):
		self.sen = sentence
		self.timedate = [0 for x in range(5)]
		self.uppervalue = [59, 24, 31, 2200]
		self.lowervalue = [0,0, 1, 1970]
	
	def cheack(self, index):
		if self.timedate[index] >= self.uppervalue[index] and index < 4:
			self.timedate[index + 1] += self.timedate[index]/self.uppervalue[index] + 1
			self.timedate[index] = self.timedate[index]%self.uppervalue[index]
		if self.timedate[index] <= self.lowwervalue[index] and index >= 0:
			self.timedate[index + 1] -= self.timedate[index]/self.uppervalue[index] + 1
			self.timedate[index] = self.timedate[index]/self.uppervalue[index]
	
	def time_operation(self, value, index, opp):
		if opp = "add":
			self.timedate[index] += value
		elif opp = "sub":
			self.timedate[index] -= value
		elif opp = "set":
			self.timedate[index] = value
	
	def 