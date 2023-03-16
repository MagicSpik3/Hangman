old_list = ['A', 'B', 'C']
exclude_list = ['B']
# new list = old_list - exclude list
# remove stop words using list comprehension
newlist = [word for word in old_list if not word in exclude_list]
print(newlist)