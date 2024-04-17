"""
Author: Jack Edwards
jackedwards1215@gmail.com
April 16, 2024

Q2: Create a function that takes some text as input and returns a list of the
unique words in that text with a count of how many times each word appears.
What is the time complexity of your implementation?

Time Complexity
  count_words:
    O(m = text length) for lowercase conversion, removiing punctuation, and splitting
    O(n = # of words) for counting the words
    Total = O(3m + n)
    Most would write as O(m + n) or just O(n)
    
  print_dict
    O(n = # words) for iterating over dictionary
    O(nlog(n)) for sorted() - likely quicksort or mergesort
    Total = O(n + nlog(n)) = O(nlog(n))
    It's not neccesary to sort
  
The total time complexity is O(nlog(n)) if both methods are used
"""

def count_words(text):
  # Unique words may have different capitalization
  text = text.lower()
  newtext = ''
  
  # Remove punctuation for split function to work properly
  for letter in text:
    if letter.isalnum() or letter.isspace() or letter == '\'' or letter == '-':
      newtext += letter
  
  # Splits into list around whitespace
  word_list = newtext.split()
  counts_dict = {}
  
  # Count words
  for word in word_list:
    if word in counts_dict:
      counts_dict[word] += 1
    else:
      counts_dict[word] = 1
      
  return counts_dict


def print_dict(dict):
  print("Number of occurrences of each word:")
  for word, number in sorted(dict.items()):
    print(f"{word.capitalize()}: {number}")


#example usage#
quote = """
The important thing is not to stop questioning.
Curiosity has its own reason for existing.
One cannot help but be in awe when one contemplates the mysteries of eternity,
of life, of the marvellous structure of reality.
It is enough if one tries to comprehend only a little of this mystery every day.
Never lose a holy curiousity.

Albert Einstein
"""
dict = count_words(quote)
print(dict)
print_dict(dict)
      
      
  