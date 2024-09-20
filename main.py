# ------------------------------------------------------------------------

# Lab 1
# 1. Create a list called my_list with the values [1, 5, 'apple', 20.5].
my_list = [1, 5, 'apple', 20.5]
# 2. Using indexing, print the value 'apple' from my_list.
print(my_list[2])
# 3. Add the value 10 to the end of my_list using the append() method. Print the updated list.
my_list.append(10)
print(my_list)
# 4. Remove the value 20.5 from my_list using the remove() method. Print the updated list.
my_list.remove(20.5)
print(my_list)
# 5. Reverse the order of the elements in my_list using a method. Print the reversed list.
my_list.reverse()
print(my_list)

# ### Lab Exercise 2: Dictionaries in Python
# 1. Create a dictionary called person with keys 'name', 'age', 'job' and values 'John', 30, 'teacher'.
person = {'name': 'John', 'age':30, 'job':'teacher'}
# 2. Print the value corresponding to the 'job' key.
print(person['job'])
# 3. Add a new key-value pair: 'city': 'Paris' to the person dictionary. Print the updated dictionary.
person['city'] = 'Paris'
print(person)
# 4. Remove the 'age' key-value pair from person. Print the updated dictionary.
person.pop('age')
print(person)
# 5. Iterate through the person dictionary and print out each key-value pair on a separate line.
for key, value in person.items():
    print(f'{key}: {value}')
# # -----------------------------------------------------------------------------
## Homework:
# Here are 5 programming homework questions with extended unit tests and usage restrictions:

# ### 1. Function: `count_vowels`
# **Description**: Write a function that takes a string and returns the number of vowels (a, e, i, o, u) in the string. Implement this using a loop and conditional statements.

# **Restrictions**: Do not use `string.count()` method or regular expressions (`re` module).

def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
    
print(count_vowels('independence'))

### 2. Function: `merge_lists`
# **Description**: Write a function that takes two sorted lists and merges them into a single sorted list. Implement the merging algorithm yourself using loops and comparisons.

# **Restrictions**: You may not use the `sorted()` or `sort()` Python built-in functions, `list.extend()`, or list concatenation (`+`) to solve this question.

def merge_lists(list1, list2):
    merged_list = []
    a, b = 0, 0

    while a < len(list1) and b < len(list2):
        if list1[a] < list2[b]:
            merged_list.append(list1[a])
            a += 1
        else:
            merged_list.append(list2[b])
            b += 1

    while a < len(list1):
        merged_list.append(list1[a])
        a += 1

    while b < len(list2):
        merged_list.append(list2[b])
        b += 1

    return merged_list

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

result = merge_lists(list1, list2)
print(result)

# ### 3. Function: `word_lengths`
# **Description**: Write a function that takes a list of strings and returns a list with the lengths of each string. Use a for loop to solve this problem.

# **Restrictions**: Do not use list comprehensions or the `map()` function.

def word_lengths(strings):
    lengths = []
    
    for string in strings:
        length = len(string)
        lengths.append(length)
        
    return lengths
    
my_strings = ["rushi", "jiya", "ryan"]
print(word_lengths(my_strings))

# ### 4. Function: `reverse_string`
# **Description**: Write a function that takes a string and returns it reversed. Implement the reversal using a loop or recursion.

# **Restrictions**: Do not use the `reversed()` function.

def reverse_string(s):
    reverse_string = ""
    for char in s:
        reverse_string = char + reverse_string
        
    return reverse_string
    
strng = "super monkey"
print(reverse_string(strng))

# ### 5. Function: `intersection`
# **Description**: Write a function that takes two lists and returns their intersection as a new list. Implement this using nested loops or a dictionary for counting occurrences.

# **Restrictions**: Do not use list comprehensions.

def intersection(colors1, colors2):
    intersection = []
    
    for color1 in colors1:
        for color2 in colors2:
            if color1 == color2:
                intersection.append(color1)
    return intersection
colors1 = {'y', 'e', 'l', 'l', 'o', 'w'}
colors2 = {'b', 'l', 'u', 'e'}

print(intersection(colors1, colors2))

# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)



# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 11])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
