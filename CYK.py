import sys
import string

class ConvertCNF():
	def __init__(self, rules):
		self.rules = rules
		self.terminal = {}
		self.temp_list = {}
		self.eliminateEpsilon()
		self.eliminateVariableUnit()
		self.moveTerminalToUnit()
		self.replaceLongProd()

	def startSymbol(self):
		pass

	def eliminateEpsilon(self):
		for key,value in self.rules.items():
			if 'ε' in value:
				for key2, value2 in self.rules.items():
					if key in str(value2):
						if key in value2:
							self.rules[key2].append('ε')
						else:
							for item in value2:
								new_prod = self.create_prod_combinations(item, key, item.count(key))
								self.rules[key2] = self.rules[key2] + new_prod
				self.rules[key].remove('ε')

		for key, value in self.rules.items():
			value = set(value)
			value = list(value)
			self.rules[key] = value
		#print("After Epsilon Elimination: ")
		#print(self.rules)

	def create_prod_combinations(self, prod, nt, count):
	        numset = 1 << count
	        new_prods = []

	        for i in range(numset):
	            nth_nt = 0
	            new_prod = ''

	            for s in prod:
	                if s == nt:
	                    if i & (1 << nth_nt):
	                        new_prod = new_prod+s
	                    nth_nt += 1
	                else:
	                    new_prod = new_prod+s

	            new_prods.append(new_prod)

	        return new_prods

	def eliminateVariableUnit(self):
		for key, value in self.rules.items():
			for key2, value2 in self.rules.items():
				if key in str(value2):
					if key in value2:
						self.rules[key2] = self.rules[key2] + self.rules[key]
						self.rules[key2].remove(key)
		#print("After eliminate variable unit")
		print(self.rules)

	def replaceLongProd(self):
		for key, value in self.rules.items():
			for i in range(len(value)):
				temp_str = ''
				if len(value[i])!=1 :
					for j in range(len(value[i])):
						if value[i][j] in self.terminal:
							temp_str += self.terminal[value[i][j]]
						else:
							temp_str+= value[i][j]
					self.rules[key][i] = temp_str
				if len(value[i])==2 and value[i].isupper():
					self.temp_list[value[i]] = key
		#print(self.rules) 

		for key, value in self.rules.copy().items():
			for i in range(len(value)):
				if len(value[i])>2 and value[i].isupper():
					for j in range(len(value[i])-1):
						if len(value[i])==2:
							break
						if value[i][j]+value[i][j+1] in self.temp_list:
							if self.temp_list[value[i][j]+value[i][j+1]] == key:
								continue
							else:
								self.rules[key][i] = self.rules[key][i].replace(self.rules[key][i][j:j+2], self.temp_list[value[i][j]+value[i][j+1]])
						else:
							item = self.getNewNTSymbol()
							self.rules[item] = [value[i][j]+value[i][j+1]]
							self.temp_list[value[i][j]+value[i][j+1]] = item
							self.rules[key][i] = self.rules[key][i].replace(self.rules[key][i][j:j+2], item)
		print(self.rules)

	def getNewNTSymbol(self):
		nt = list(string.ascii_uppercase)
		new_nt = ''
		for item in nt:
			if item in self.rules:
				continue
			else:
				new_nt = item
				break
		return new_nt

	def moveTerminalToUnit(self):
		for key, value in self.rules.items():
			for i in range(len(value)):
				#print(value[i])
				if len(value[i])>1 and any(c.islower() for c in value[i]):
					for c in range(len(value[i])):
						if value[i][c].islower():
							print(value[i][c])
							self.terminal[value[i][c]]=key
		#Need to check here with real example
		for item, value in self.terminal.items():
			dict_new_nt = item.upper()
			while dict_new_nt in self.rules:
				dict_new_nt = dict_new_nt+'0'
			self.rules[dict_new_nt] = [item]
			self.terminal[item] = dict_new_nt
		print(self.rules)


class CYK():
	def __init__(self, path):
		self.path = path
		self.rules = {}
		self.readGrammar()
		self.converted= ConvertCNF(self.rules)
		self.word = 'aaabbb'
		print("final")
		print(self.converted.rules)
	'''How to check start symbol?'''
	#Assume about Start symbol? Epsilon symbol? Terminal and non-termnial symbol?
	#
	def readGrammar(self):
		f = open(self.path)
		for content in f:
			content = content.rstrip()
			rule = content.split(" → ")
			self.rules[rule[0]] = rule[1].split(" | ")
	
	def parser(self):
		for i in range(len(self.word)):
			


if __name__ == "__main__":
    CYK(sys.argv[1])
