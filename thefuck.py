def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    print count
    return int(count)
    
    
count([1,2,1,1], 1)