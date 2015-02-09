#import argument variables
from sys import argv
#assign python script and input file to argv
script, input_file = argv

#define a function, print_all that reads a file
def print_all(x):
    print x.read()
#define a function, rewind that starts over      
def rewind(x):
    x.seek(0)
#define a function that prints a single line.      
def print_a_line(line_count, x):
    print line_count, x.readline(),
#set current file to the open test.txt      
current_file = open(input_file)

print "First let's print the whole file:\n",
#prints the current file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
