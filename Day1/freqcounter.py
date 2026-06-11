#Word Frequency Counter: Take a paragraph as input. 
# Count how many times each word appears (case-insensitive, ignore punctuation). 
# Print the top 5 most frequent words. 
from collections import Counter
import re

paragraph = input("Enter a paragraph: ")
words = re.findall(r'\b\w+\b', paragraph.lower())

#  `\b`  Word boundary (start/end of a word) 
#  `\w`  Any letter, digit, or underscore    
#  `+`   One or more occurrences             

freq = Counter(words)
print("Top 5 most frequent words:")
for word, count in freq.most_common(5):
    print(f"{word}: {count}")

    