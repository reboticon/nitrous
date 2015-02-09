a = [1,2,3]
b= [1,2,3]

def string_match(a, b):
  count = 0
  if len(a) > len(b):
    c = len(a)
  else:
    c = len(b)
  
  
  for i in range(c -1):
   
    
    if a[i] == b[i] and a[i+1] == b[i+1]:
      count += 1
  return count
    
print string_match(a,b)

i = "hello"
end = i[-10:3]
print i[0:2]
print i[0:4]
print end