# read file 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf8') as f:
		for line in f:
			lines.append(line.strip())
	return lines#有回傳就要存回去

def convert(lines):#要把上面的line清單傳進來
	new = []
	person = None
	for line in lines: #從清單中一行一行拿出來
		if line == 'Lin':
			person = 'Lin'
			continue #才不會重複
		elif line == 'Cynthia':
			person = 'Cynthia'
			continue #才不會重複

		if person:#如果person有值
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt') #有回傳就要存回去
	lines = convert(lines)
	write_file('output.txt', lines)

main()










