#open a file and read it's content
file=open('Codingal.txt','r')
print(file.read())
file.close()

#open file and read it's first 12 charachters
file=open('Codingal.txt','r')
print(file.read(12))
file.close()

#append your age and name in the file
file=open('Codingal.txt','a')
file.write(". My name is hamza and I love to play football")
file.close()