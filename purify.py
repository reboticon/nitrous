def purify(x):
    new_list = []
    for item in x:
        if (item + 2) % 2 == 0 and item != 0:
            new_list.append(item)
    print new_list
      
purify([1,2,3,4,5,6,0,4,332,18])