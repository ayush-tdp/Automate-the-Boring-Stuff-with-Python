myList = [["a","b","c","d"],"e","f"]

# print(len(myList))
# print(myList[0])
# print(myList[0][3])
# print(myList[0:2])
# print(myList[0:])
# print(myList[:2])
# print(myList[:])

myList1 = [1,2,3,4,10,7,6]
myList2 = [5,6,7,8]

# del myList2[0]
# del myList2
print(myList1 + myList2)    

try:
    var1,var2,var3,var4,var5 = myList2
    print(var1,var2,var3,var4)
except ValueError:
    print(ValueError)

print(myList1.index(4))
# myList1.append("sdfcsf")
myList1.remove(1)
# print(myList1.sort())
print(myList1.sort(reverse=True))
print(myList1)

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort(key=str.lower)
print(spam)