fread=open("sample.txt","r")
data=fread.read()
print(data)
print(type(data))

data=fread.readline()
print(data)