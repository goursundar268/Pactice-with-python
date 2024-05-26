def concatenate_dicts(*dicts):
    new_dict={}
    for d in dicts:
        new_dict.update(d)
    return new_dict
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
dict3={"e":5,"f":6}

dict=concatenate_dicts(dict1,dict2)
print(dict)