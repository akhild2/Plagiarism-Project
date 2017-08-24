import glob

class plag():
	def __init__(self,file=None):
		self.file = file
		self.remove = "!@#$%^&*()_+= -{}:?><,./;\"[']"
		self.d = {}
		self.euc = 0
		self.List = ''

	def list_freq(self):
		self.List = self.file.read().lower()
		words_list = self.List.split()
		for i in range(len(words_list)):
			words_list[i] = words_list[i].strip(self.remove)
		self.d = {}
		for word in words_list:
			if word not in self.d:
				self.d[word]=1
			else:
				self.d[word]+=1

	def getEuc(self):
		return self.euc

	def setEuc(self,Neuc):
		self.euc = Neuc

	def Euc(self):
		summ = 0
		for key,value in self.d.items():
			summ = summ+(value**2)
		self.setEuc(summ**0.5)

def CrossProduct(objects):
	l = []
	for i in range(0,len(objects)):
		for j in range(0,len(objects)):
			summ = 0
			for key,value in objects[i].d.items():
				for key1,value1 in objects[j].d.items():
					if key==key1:
						summ = summ+(value*value1)
			p = (summ/(objects[i].getEuc()*objects[j].getEuc()))*100
			l.append(p)
	return l

def matrix_display(plag_values):
	matrix = []
	small_matrix = []
	for i in plag_values:
		if len(small_matrix) == len(files_list):
			matrix.append(small_matrix)
			small_matrix = [i]
		else:
			small_matrix.append(i)
	matrix.append(small_matrix)
	print(' '*(len(max(files_list))),'  ',end='')
	num = 1
	for i in files_list:
		print('file'+str(num),'        ',end='')
		num+=1
	print('')
	pos = 0
	num = 1
	for i in files_list:
		print('file'+str(num),' | ',end='')
		num+=1
		for j in matrix[pos]:
			print('{:10.2f}'.format(j),' | ',end='')
		print('')
		pos+=1

files_list = glob.glob('./*.txt')
objects = []
for file in files_list:
	read_file = open(file,'r')
	a = plag(read_file)
	objects.append(a)
for obj in objects:
	obj.list_freq()
	obj.Euc()
plag_values = CrossProduct(objects)
matrix_display(plag_values)