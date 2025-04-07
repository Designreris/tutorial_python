#### LISTS ####
users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

empty_list = []

# print('Dave' in empty_list)
# print(users[0])
# print(users[-1])
# print(users.index('Sara'))
# print(users[0:2])
# print(users[0:])
# print(users[-3:-1])
# print(len(data))

users.append('Elsa')
# print(users)

users += ['Jason'] # Note: needs [] 
# print(users)

users.extend(['Robert', 'Jimmy'])
# print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
# print(users)

users[2:2] = ['Eddie', 'Alex']
# print(users)

users[1:3] = ['Rob', 'JPJ'] # Note: slice
# print(users)

users.remove('Bob')
# print(users)

# print(users.pop(), users)

del users[0]
# print(users)

# del data
# print(data)

data.clear() # Note: clears list
# print(data)

users.sort() # Note: sorts by alphabet
# print(users)

users[1:2] = ['dave']
users.sort()
# print(users)

users.sort(key=str.lower) # Note: includes lowercase
# print(users)

nums = [4,42,78,1,5]
nums.reverse() # Note: flips list
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# print(sorted(nums, reverse=True)) # Note: keeps original list
# print(nums)

nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]
# print(nums_copy) # copy
# print(my_nums) # copy
# print(my_copy) # copy
# print(nums) # original

# print(type(nums))

my_list = list([1, 'Neil', True])
# print(my_list)


#### TUPLES ####
# Tuples cant change or sort!
my_tuple = tuple(('Dave', 42, True))

another_tuple = (1,2,3,8,2,2) # Packing the tuple

# print(my_tuple)
# print(type(my_tuple))
# print(type(another_tuple))

new_list = list(my_tuple)
new_list.append('Neil')
new_tuple = tuple(new_list)
# print(new_tuple)

(one, *two, three) = another_tuple # Unpacking a tuple
# print(one)
# print(two)
# print(three)

# print(another_tuple.count(2))







