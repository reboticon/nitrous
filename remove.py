def remove_duplicates(x):
    new_list = []
    for item in x:
        if item not in new_list:
            new_list.append(item)
    print new_list
    return new_list   
   
   
remove_duplicates([1,1,2,2]) 