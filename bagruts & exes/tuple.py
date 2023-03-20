list1=[1,2,2,2,3,5,7,2,6]
list2=[2,2,2,2,3,5,7,2,0]
list3=[3,2,2,2,3,5,7,2,6]
for i, j, k in zip(list1, list2,list3): #zip combines lists to one list which built from tuples that contains the lists
    print(i)
    print(j)
print(list(enumerate(list1))) #enumerate on list retuerns another list which built from tuples that contains the index and the number in this index
