
#variables
lines=0
words=0
chars=0
#welcome user
print("Welcome to Word Count")
print("Now Analyzing file")

#save file locations in an array
filename = ["C:\\Users\\marce\\Documents\\MarcelpierresGIT\\Python\\WordCount\\wordcount1.txt","wordcount2.txt"]

#open file
file = open(filename[0], "r")

#loop through each line in the file
for line in file:
    #counter for number of lines
    lines=lines+1
    
    #save values in each line
    words = words +  len(line.split()) 

    #save characters
    chars = chars + len(line.replace(" ",""))

# the replace function doesn account for newline
chars = chars - (lines - 1)    

#display output
print ("Lines: %i   Words: %i   Characters: %i " % (lines,words,chars))
print ("Thank You for Watching!!!")

file.close()