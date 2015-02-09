def median(x):
    midpoint = 0
    even = 0
    x = sorted(x)    
    if len(x) % 2 ==0:
        even = len(x) / 2
        midpoint =(float(x[even]) + x[even -1])/2
        print midpoint
        return midpoint
    else:
        midpoint = x[len(x) / 2]
        print midpoint
        return midpoint
   

median([5, 2, 78])
