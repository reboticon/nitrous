cubes = [x**3 for x in range(1, 11)]
print filter(lambda x: x % 3 == 0, cubes)



#8's bit  4's bit  2's bit  1's bit
 #   1       0       1      0 
  #  8   +   0    +  2   +  0  = 10 
      
      
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11 #4?
print 0b11 * 0b11 # 9?
    