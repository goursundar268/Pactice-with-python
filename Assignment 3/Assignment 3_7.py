# Write a Python program to sort (ascending and descending) a dictionary by value.

d={"one":1,
   "two":2,
   "three":3,
   "four":4,
   "five":5}

def sort_value(a):
    return a[1]
new_d=sorted(d.items(),key=sort_value)
print(new_d)
    