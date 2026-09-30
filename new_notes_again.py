grade = 100


if grade >=90:
     print("you cooked")
elif grade >= 70:
    print("you are passing")
elif grade <70:
     print("you fail")
     print("do better")
     #top should be the least likley situation
username= input("what is your username: ")

raining= False

if raining:
     print("bring an umbrella")
else:
    print("wear sunscreen")
#LISTSTSTSTSTSTSTSTSTS.
#tuples
#one peice
siblings= ["fat","fatter","fit"]#brackets seperated by commas and must be proper data types
#lists deal with evil
print(*siblings)#in relation to strings, or lists, * is the unpacker
siblings.append("fattest")
siblings.insert(2,"flat")
print(*siblings)
siblings.pop(3)
siblings.remove("fat")
siblings
print(*siblings)
#lists|[]|ordered|mutable|duplicates are allowed
#tuples|()|ordered|immutable|duplicates are allowed
#set|{}|unordered|mutable| no duplicates ever

visited = {"texas","ohio","colorado","idaho"}
print(*visited)
print(len(visited))
visited.add("arizona")
print(*visited)
visited.remove("arizona")
#variabletype,(variablename))