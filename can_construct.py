from collections import Counter
def can_construct(ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)

note = 'abracadbra'
magazine_1 = 'hocuspocusaardvarkbillygoatbadboy'
magazine_2 = 'hocuspocusaardvarkbillygoat'

print(can_construct(note, magazine_1)) # True, all letters appear with same or higher frequency in magazine_1
print(can_construct(note, magazine_2)) # False, missing a "b" in magazine_2

"""
Why this works from Python docs:

What is Counter?
A Counter is a dict subclass for counting hashable objects. It is a collection 
where elements are stored as dictionary keys and their counts are stored as 
dictionary values. Counts are allowed to be any integer value including zero 
or negative counts. The Counter class is similar to bags or multisets in other 
languages.

What do addition and subtraction of counters do?
>>> c = Counter(a=3, b=1)
>>> d = Counter(a=1, b=2)
>>> c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
>>> c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})

Subtracting a counter from another counter removes the difference in counts
of identical keys
If removing the difference ends in zero the entire key,value pair is removed
In python if you check for truthiness of an empty Counter() you will get False

Therefore, if all the letters in ransomNote are also in magazine with the same or
higher frequency in magazine then using a Counter and subtracting will give us an
empty Counter()
"""
