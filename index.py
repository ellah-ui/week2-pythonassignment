my_list = []
my_list.append(10)
my_list.append (20)
my_list.append(30)
my_list.append(40) # this will add the elements to the list

my_list.insert(1, 15) # this will insert 15 at the second position in the list

print(my_list) # this will print the list
 
my_list.extend([50,60,70]) # this will add the elements to the list

my_list.pop() # this will remove the last element from the list

my_list.sort() # this will sort out the list in ascending order

index_of_30 = my_list.index(30) # this will return the index of 30 in the list
print(index_of_30)

print(my_list) # this will print the list