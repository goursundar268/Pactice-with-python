d1={"a":"apple","b":"boy","c":"cat","d":"dog"}
d1["c"]="cow"
print(d1.values())
print(d1.values())
d2={"d":"day","e":"egg"}
d1.update(d2)
print(d1)
print(d2)
d2.clear()
print(d2)
print(d1.get("b"))
del d2
print(d2)

