import glob

class plag():
	def __init__(self,file=None):
		self.file = file
		self.remove = "!@#$%^&*()_+= -{}:?><,./;\"[']"
		self.d = {}
		self.euc = 0

	def list_freq(self):
		List = self.file.read().lower()
		words_list = List.split()
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
	for i in range(0,len(objects)):
		summ = 0
		for j in range(i+1,len(objects)):
			for key,value in objects[i].d.items():
				for key1,value1 in objects[j].d.items():
					if key==key1:
						summ = summ+(value*value1)
			p = (summ/(objects[i].getEuc()*objects[j].getEuc()))*100
			print('The similarity between '+str(files_list[i])[2:]+' and '+str(files_list[j])[2:]+' is : '+str(p)+'%')

files_list = glob.glob('./*.txt')
objects = []
for file in files_list:
	read_file = open(file,'r')
	a = plag(read_file)
	objects.append(a)
for obj in objects:
	obj.list_freq()
	obj.Euc()
CrossProduct(objects)