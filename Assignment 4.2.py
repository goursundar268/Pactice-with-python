# write a python program in python to create
# A binary file and print the content of the file.
import pickle
fp=open("sample.dat","wb")
d={"one":100,"two":200,"three":300,"four":400,"five":500}
pickle.dump(d,fp)
fp.close()