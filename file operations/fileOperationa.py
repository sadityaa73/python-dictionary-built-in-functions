# These are the following ways to rad the content of the files.
print("\n")
readFile = open('file operations/dataFile.txt','r')
print(readFile.read())

print("\n")
readFile1 = open('file operations/dataFile.txt','r')
for content in readFile1:
    print(content)
    
print("\n")    
# read file in python by using with Statement:

with open('file operations/dataFile.txt') as file:
    print(file.read())
    
print("\n")

#These are the following to write content in a file :

writeFile = open('file operations/writeData.txt','w')
writeFile.write("hello my name is aditya")
writeFile.close()

# write content in file by using with statements:

with open('file operations/writeData.txt','w') as wfile:
    wfile.write("hello my is ---")
    wfile.close()
    
readfiles = open('file operations/writeData.txt','r')
print(readfiles.read())


