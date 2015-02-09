list_1 = [8, 3, 19]
list_2 = [3, 19, 20]


print min(list_1, list_2)
#prints [3, 19, 8]

final=[]
for j, k, in zip(list_1, list_2):
     final.append( min(j, k))
      
print final




def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x == 3:
        return True
    else:
    
    
        for n in range(2, x - 1):
            if x % n == 0:
                print 'false'
                return False
        else:
            print 'true'
            return True

is_prime(9)
            
      