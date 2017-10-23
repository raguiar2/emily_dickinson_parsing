import os

DIRECTORY = 'poems/'

# rename poetry files because 
# they were in uppercase. 
def main():
	for filename in os.listdir('poems'):
		os.rename(DIRECTORY+filename,DIRECTORY+filename.lower())
		with open(DIRECTORY+filename.lower()) as f:
			lines = f.readlines()
		lines[0] = lines[0].lower()
		with open(DIRECTORY+filename.lower(), "w") as f:
			f.writelines(lines)

if __name__ == '__main__':
	main()