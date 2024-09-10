## Homework:
Here are 5 programming homework questions with extended unit tests and usage restrictions:
### 1. Function: `count_vowels`
**Description**: Write a function that takes a string and returns the number of vowels (a, e, i, o, u) in the string. Implement this using a loop and conditional statements.

**Restrictions**: Do not use `string.count()` method or regular expressions (`re` module).

**Unit Tests**:
```python
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
```

### 2. Function: `merge_lists`
**Description**: Write a function that takes two sorted lists and merges them into a single sorted list. Implement the merging algorithm yourself using loops and comparisons.

**Restrictions**: You may not use the `sorted()` or `sort()` Python built-in functions, `list.extend()`, or list concatenation (`+`) to solve this question.

**Unit Tests**:
```python  
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
```

### 3. Function: `word_lengths`
**Description**: Write a function that takes a list of strings and returns a list with the lengths of each string. Use a for loop to solve this problem.

**Restrictions**: Do not use list comprehensions or the `map()` function.

**Unit Tests**:
```python
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])
```

### 4. Function: `reverse_string`
**Description**: Write a function that takes a string and returns it reversed. Implement the reversal using a loop or recursion.

**Restrictions**: Do not use the `reversed()` function.

**Unit Tests**:
```python
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
```

### 5. Function: `intersection`
**Description**: Write a function that takes two lists and returns their intersection as a new list. Implement this using nested loops or a dictionary for counting occurrences.

**Restrictions**: Do not use list comprehensions.

**Unit Tests**:
```python
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

```

### Test Suite
```python
def test_suite():
  test_count_vowels()
  test_merge_lists() 
  test_word_lengths()
  test_reverse_string()
  test_intersection()
test_suite()
```

### Test Function
Recall the custom test function from last week:
```python
import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)
```

### General Instructions:
1. Implement each function according to its description and restrictions.
2. Comment your code explaining your approach.
3. Consider time complexity in your solutions.
4. Handle edge cases and provide error handling where appropriate.
