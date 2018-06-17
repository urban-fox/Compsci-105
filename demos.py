# List methods

# List comprehension ---------------------------------------------
list_comprehension = [x ** 2 for x in range(1, 10)]

# Equivalent to
list_for_loop = []
for i in range(1,10):
  list_for_loop.append(i ** 2)

print("List Comprehension:", list_comprehension)
print("List For Loop: ", list_for_loop)

# List comprehension with two variables
print("List comprehension with two variables",
  [x * y for x in range(1,5) for y in range(5, 10)]  
)

print("List comprehension with two variables - concatenation",
  [x + y for x in 'abc' for y in 'xyz']
)

# Filtering
# [EXPRESSION for VARIABLE in SEQUENCE if CONDITION]
print("With condition: 1 - 100 divisible by 4 only",
  [x for x in range(1, 101) if x%4 == 0]
)

# In-place methods
# append, insert, remove, extend, reverse, sort

# Exercises:

# List comprehension that generates odd numbers betweeen 1 and 50 (inclusive)
list_odd_numbers = [x for x in range(1,51, 2)]
print("List odd numbers 1-50", list_odd_numbers)

# Only outputs vowels of a given phrase
def vowels_only(input):
  vowels = 'AEIOUaeiou'
  return [x for x in input if x in vowels]
print("Vowels only", vowels_only("This is just a test phrase"))

# List comprehension to generate a list of tuples: x, x**2, x**3
print("First 3 powers", 
  [(x, x**2, x**3) for x in range(1, 11)]
)
