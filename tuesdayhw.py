##Given a list as a parameter,write a function that returns a list of numbers 
# that are less than ten
# For example: Say your input parameter to the function is 
# [1,11,14,5,8,9]...Your output should [1,5,8,9]

my_list = [1,11,14,5,8,9]
c = 10

the_list = [i for i in my_list if i < c]
print(the_list)

##Write a function that takes in two lists and returns the two lists 
# merged together and sorted
##Hint: You can use the .sort() method

list_1 = [1,2,3,4,5]
list_2 = [1,2,3,5,8,13,21,34]

list_3= list_1 + list_2

print('Sorted list', list_3)

