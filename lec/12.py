# List Methods

lst = [5, 6, 7, 8] # make a list
lst[1] = 12 # change the element at index 1 to 12
print("line 3:", lst) # the list changed
lst.pop() # 'pop' off the last element
print("line 5:", lst) # the list changed
lst.append(15) # add 15 to the end of lst
print("line 7:", lst) # the list changed

# Mutative Function
def mystery2(): # mutative function
    four.pop()
    four.pop()

four = [4, 4, 4, 4]
len(four) # initially length 4
mystery2() # mutate the list 
len(four) # now length 2

# Tuples
t = (1, 2, [3, 4]) # a tuple
print(t[0]) # supports indexing
print(t[2]) # supports indexing
t[2] = 5 # errors!
t[2][0] = 5 # this value is mutable though
print(t) # changed!

# Golden Rule Example
lst1 = [1, [2, 3], 4]
lst2 = lst1
lst3 = lst1[:]
print(lst1 == lst2)
print(lst1 == lst3)
print(lst1 is lst2)
print(lst1 is lst3)
lst1[0] = 10
print(lst1)
print(lst2)
print(lst3)
lst3[2] = 40
print(lst1)
print(lst2)
print(lst3)
lst3[1][1] = 30
print(lst1)
print(lst2)
print(lst3)