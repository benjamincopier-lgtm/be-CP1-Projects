#str methods
#make a string first
#methhead write what you want to be thingied dot action called dot notation, lower capitalize, upper, and title
#user=stupid
#methheads change not the variable
# join at split
#isalpha checks if the entire string is letters
#isnumeric checks to see if the entire string is numbers
#isupper checks for upper
#print(f"hello {variable} welcome to ,y program")
#name=input("what is your name: ").strip().title()
#print("hello " + name.strip().title())
#sentence = "the Quick brown fox jumps over the lazy dog"
#print(sentence.capitalize())
#fixed=sentence.replace("fox", "wolf")
#print(fixed)
#print(sentence.split("the"))
#ord finds the value of the keyboardchar numb val
def split_number_by_string(number, position):
    # Convert number to string
    num_str = str(number)
    
    # Split using string slicing
    left_part = num_str[:position]
    right_part = num_str[position:]
    
    # Convert back to integers
    return int(left_part), int(right_part)

# Example Usage: Split 123456789 at index 4 (after the 4th digit)
left, right = split_number_by_string(123456789, 4)
print(f"Left: {left}, Right: {right}")
# Output: Left: 1234, Right: 56789
#import random calls a module library
#a function is movable code that has been built that you can use just by saying its name
#save randint give lowest and give highest (1, 10)
#for a computer to get a rand int it needs a specific numb
#rand.rand gives a 0-1 