numbers = """3988689 -2568741
8919518 729135
2590543 4301715
-8565317 -92424
4155932 -4584657
2246128 2047316
509554 -3927156
-2166616 6856159
-5765829 -7994090
-3735809 2845417
8736261 8938045
-6918790 4752570
1933145 4917659
3549721 -3421574
-7781289 -8347421
2968119 6207399
-916163 1887637
-3063465 -8325619
-3810648 -1628783
1581956 -9654715
3786560 -6171915
2392601 -5703886
-99072 -9774015 """
numbers = numbers.split()
numbers = map(int, numbers)
list1 = numbers[0:len(numbers):2]
list2 = numbers[1:len(numbers):2]

final = []
for i, j in zip(list1, list2):
    if i < j:
        final.append(i)
    else:
        final.append(j)
         
print final
print len(final)

-2568741 729135 2590543 -8565317 -4584657 2047316 -3927156 -2166616 -7994090 -3735809 8736261 -6918790 1933145 -3421574 -8347421 2968119 -916163 -8325619 -3810648 -9654715 -6171915 -5703886 -9774015