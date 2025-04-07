# DICTIONARIES - Similar to JS lists
band = {
  'vocals': 'Plant',
  'guitar': 'Page',
}

# Constructor
band_2 = dict(vocals='Plant', guitar='Page')

# print(band)
# print(band_2)
# print(type(band))
# print(len(band))


# Access items
# print(band['vocals'])
# print(band.get('guitar'))

# List all keys
# print(band.keys())

# List all values
# print(band.values())

# List of key/value pairs as tuples
# print(band.items())

# verify a key exists
# print('guitar' in band)
# print('triangle' in band)

# change values
band['vocals'] = 'Coverdale'
band.update({'bass': 'JPJ'}) # adds new key:value
# print(band)

# Remove items
# print(band.pop('bass'))
# print(band)

band['drums'] = 'Bon'
# print(band)
# print(band.popitem()) # removes last item, returns tuple
# print(band)

# DELETE AND CLEAR
del band['drums']
# print(band)

band_2.clear() # empties dictionary {}
# print(band_2)

del band_2 # removes dictionary


# COPY DICTIONARIES

# REFERENCE DICT
# band_2 = band # creates a reference - same place in memory, not a copy.
# print("Bad copy!")
# print(band)
# print(band_2)
# band_2['drums'] = 'Dave'
# print(band)
# print(band_2)

# COPY DICT
band_2 = band.copy()
band_2['drums'] = 'Dave'
# print(band)
# print(band_2)

# or use the dict() constructor function
band_3 = dict(band)
# print('good copy')
# print(band_3)

# NESTED DICTIONARIES
member_1 = {
  'name': 'Plant',
  'instrument': 'vocals',
}
member_2 = {
  'name': 'Page',
  'instrument': 'guitar',
}
band = {
  'member_1': member_1,
  'member_2': member_2
}
# print(band)
# print(band['member_1']['name'])


# SETS
nums = {1,2,3,4}
nums_2 = set((5,6,7,8))
# print(nums)
# print(nums_2)
# print(type(nums))
# print(len(nums))

# No duplicates allowed
nums = { 1,2,2,4}
# print(nums)

# True is a dupe of 1, False is a dupe of zero.
nums = {1, True, 2, False, 3, 4 ,0}
# print(nums)

# check if a value is in a set
# print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# add a new element to a set
nums.add(8)
# print(nums)

# add elements from one set to another
more_nums = {5,6,7}
nums.update(more_nums)
# print(nums)

# you can use update with lists, tuples and dictionaries, too.

# MERGE TWO SETS TO CREATE A NEW SET
one = {1,2,3}
two = {5,6,7}
my_new_set = one.union(two)
# print(my_new_set)

# Keep only duplicates - intersection_update()
one = {1,2,3}
two = {2,3,7}
one.intersection_update(two)
# print(one)
# print(two)

# Keep everything except the duplicates - symmetric_difference_update()
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
# print(one)
# print(two)
