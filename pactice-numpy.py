import numpy as np
arr=np.array([30,50,40,60,80,70,10])
print(arr)

# all element add to 7
arr2=arr+7
print(arr2)

#add,sub,mul,div create 
print("***************************************************************************************")
print("add,sub,mul,div create")
print("\t")

m1=np.array([10,15,20,20,16,10])
m2=np.array([12,15,10,20,10,20,])

add=m1+m2
print("add to m1+m2=",add)

mul=m1*m2
print("mul to m1*m2=",mul)

sub=(m1-m2)
print("sub to m1-m2",sub)

div=m1/m2
print("div to m1/m2",div)

print("**************************************************************************************")
#create to a unine,intersection,set diff
print("create to a unine,intersection,set diff")
print("\t")

union=np.union1d(m1,m2)
print("m1 and m2 union is",union)

intersection=np.intersect1d(m1,m2)
print("m1 to m2 intersection is",intersection)

set_diff=np.setdiff1d(m1,m2)
print("m1 and m2 setdiffent is",set_diff)

print("**************************************************************************************")
#create to a mean,median,mode,standard deviation
print("\t")

x=np.array([10,12,10,7,9,10,8,12])
mean=np.mean(x)
print("mean is a ",mean)

median=np.median(x)
print("median is a",median)

# mode=np.mode(m1,m2)
# print("mode is a",mode)

sta_dev=np.std(x)
print("standard deviation is",sta_dev)
