import argparse #for command line arguments

def positive(input): #function to check wether the given input is a valid positive number
    if int(input) <= 0:
        raise argparse.ArgumentTypeError("invalid positive value: %s" % input)
    return input

parser = argparse.ArgumentParser(description="Print a ascii-art tree in a chosen height.") #create parser object
parser.add_argument("--star", action="store_true", help="parameter to indicate whether the tree should be drawn with a star on top of it") #add argument for the star
parser.add_argument("--height", type=positive, help="number for the height of the tree", required=True) #create argument for the height

args = parser.parse_args() #create object to get the args from parser object

star_bool = args.star #get the value of star argument
height = args.height #get the value of height argument
        
def calculate_width(value): #calculate the widest layer of the tree 
    offset = 1
    for i in range(1, int(value)):
        offset += 2
    return offset

width = calculate_width(height) #for alignment

if star_bool: #print the star if star argument was passed
    print('*'.center(width))

j = 1
for i in range(int(height)): #print the tree
    leaf = 'X' * j
    print(leaf.center(width))
    j += 2

t = int(width / 3)
print(('I'*t).center(width)) #print the tribe


    



