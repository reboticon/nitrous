numbers = """-1255643 1196420 -7051267
6470816 121385 559882
8767363 -2184671 -6752906
"""

numbers = map(int, numbers.split())

col1 = numbers[0::3]
col2 = numbers[1::3]
col3 = numbers[2::3]
print col1
print col2
print col3


print min(col1, col2, col3)



