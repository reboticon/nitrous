
numbers = """7228302 242
12007 1086
5607975 552
7602545 545
8746376 1796554
2904018 178
6290879 3384768
3165782 862
3794589 503
-2850667 -4493405
10793 1588
2234336 243"""

numbers = map(float, numbers.split())
col1 = numbers[::2]
col2 = numbers[1::2]
final =[]
final =[x /y for x,y in zip(col1, col2)]
realfinal = []
for i in final:
    realfinal.append(round(i))
    
       
   

print [int(x) for x in realfinal]
