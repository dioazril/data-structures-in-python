dict1 = {
    "value": 2 #Garbage Collection
}

dict2 = dict1

dict3 = {
    "value": 3
}

dict2 = dict3
dict1 = dict2

print(dict1)
print(dict2)
print(dict3)


