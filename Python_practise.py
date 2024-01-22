#practise
list1 = ['Urdu', 'Arabic' , 'Turkish']

#add at the end of the list
list1.append('English')
print(list1)

#add at a specific location of the list e.g. 2nd index
list1.insert(2 ,"Korean")
print(list1)

#add another list at the end of a list
list2 = ['Spanish', 'Japanese']
list1.extend(list2)
print(list1)

#remove and return last element of the list
list2.pop()
print(list2)

#sort the list alphabetically or in ascending order
list1.sort()
print(list1)

#sort the list in descending order
list1.sort(reverse = True)
print(list1)

#loop through the list
for index, course in enumerate(list1):
    print(index , course)

#comma separated list
list3 = ','.join(list1)
print(list3)

#split a string and convert each word into list element
split_str = "Split this string into list elements"
new_list = split_str.split(" ")
print(new_list)