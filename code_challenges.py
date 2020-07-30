'''
Print out all of the strings in the following array in alphabetical order, each on a separate line.
'''
arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

arr.sort()
# for word in arr:
    # print(word)
'''
'Cha Cha'
'Foxtrot'
'Jive'
'Paso Doble'
'Rumba'
'Samba'
'Tango'
'Viennese Waltz'
'Waltz'
'''
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code.
# Run through the UPER problem solving framework while going through your thought process.

def print_letter_count(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    print(counts)

# print_letter_count('aaabbcbca')

def expensive_function(x, y):
    
    key = (x, y)
    if key not in cache:
        cache[key] = whatever_expensive_thing()
    
    return cache[key]

# Given an dictionary with keys and values that consist of both strings and integers, 
# design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following dictionary as input:
test_dict = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

def sum_numeric_values(dictionary):
    total = 0
    for element in dictionary.values():
        if type(element) == int:
            total += element
    return total
print(sum_numeric_values(test_dict))
