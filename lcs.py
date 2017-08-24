import glob

class Plagiarism_Project_LCS():
	def __init__(self,file=None):
		self.file = file
		self.doc = ''

	def read(self):
		self.doc = self.file.read().lower()

	def remove(self):
		s = ''
		remove = "!@#$%^&*()_+= -{}:?><,./;\"[']"
		word_list = self.doc.strip().split()
		for i in range(len(word_list)):
			word_list[i] = word_list[i].strip(remove)

		for i in word_list:
			s = s+' '+str(i)
		self.set_doc(s)

	def get_doc(self):
		return self.doc
	def set_doc(self,Ndoc):
		self.doc = Ndoc[::]

	def lcs(self,file1,file2):
		string_1 = file1.get_doc()
		string_2 = file2.get_doc()
		# print(string_1)
		# print(string_2)
		i = 0
		j = 0
		sub_string = string_1[0]
		final_string = ''
		while True:
			if sub_string in string_2:
				j+=1
				if len(sub_string) > len(final_string):
					final_string = sub_string[::]
				if i+j>=len(string_1):
					break
				else:
					# print('i = ',i,'j = ',j)
					sub_string = sub_string + string_1[i+j]
			else:
				i += 1
				j = 0
				if i+j >= len(string_1):
					break
				sub_string = string_1[i]
		# print(sub_string)
		len_lcs = len(sub_string)
		return ((len_lcs*2)/(len(string_1)+len(string_2))*100)

def matrix_display(plagvalues):
	matrix = []
	small_matrix = []
	for i in plagvalues:
		if len(small_matrix) == len(files_list):
			matrix.append(small_matrix)
			small_matrix = [i]
		else:
			small_matrix.append(i)
	matrix.append(small_matrix)
	# print(matrix,'\n\n')
	print(' '*len(max(files_list)),' ',end='')
	num = 1
	for i in files_list:
		print('file'+str(num),'       ',end='')
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
plagvalues = []
o = Plagiarism_Project_LCS()
List = []
for file in files_list:
	op_file = open(file,'r')
	List.append(op_file)
objects = []
for file in List:
	a = Plagiarism_Project_LCS(file)
	objects.append(a)
for obj in objects:
	obj.read()
	obj.remove()
for i in range(len(objects)):
	for j in range(len(objects)):
		plagvalues.append(o.lcs(objects[i],objects[j]))
# print(plagvalues)
matrix_display(plagvalues)