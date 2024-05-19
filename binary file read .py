import pickle
fp=open("sample.dat","rb")
data=pickle.load(fp)
print(data)