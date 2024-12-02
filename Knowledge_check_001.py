#Even or Odd
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'
#odd numbers leave a remainder of 1 when divided by 2

#Converting a Number to a String!
def number_to_string(num):
    return str(num)
#str converts to string

#Vowel Count
def get_count(sentence):
    return sum(1 for char in sentence if char in "aeiou")
#counts char "aeiou" in a loop to check how many times each letter comes up.