# List comprehensions:

# List comprehension that generates odd numbers betweeen 1 and 50 (inclusive)
list_odd_numbers = [x for x in range(1,51, 2)]
print("List odd numbers 1-50", list_odd_numbers)

# Only outputs vowels of a given phrase
def vowels_only(input):
  vowels = 'AEIOUaeiou'
  return [x for x in input if x in vowels]
print("Vowels only", vowels_only("This is just a test phrase"))