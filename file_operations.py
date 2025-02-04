fp = open("text.txt", "r") #this is open from reading
print(fp.read()) #read() method gets the entire file content
fp.close() # this is good practice

 # Same thing using the content manager !
 # This is more pythonic
with open("text.txt", "r") as f:
    print(f.read())
# no need to close

# read the file line by line
with open("text.txt", "r") as f:
    for line in f: # f is iterable and we get each individual line
        print(line, end= "\n\n")