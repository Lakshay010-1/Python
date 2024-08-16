# open() function-takes 2 parameters: filename and mode.

# Modes
# r     –   open for reading
# w     -   open for writing
# a     -   open for appending
# +     -   open for updating.
# ‘rb’  -   will open for read in binary mode.
# ‘rt’  -   will open for read in text mode.

""""Read """
1
file1 = open("file1.txt", "r")
data = file1.read()
print(data)
file1.close()

2
file2 = open("file2.txt")
# Read Single Line                 
line1 = file2.readline()            # Read one line from the file.                            
print(line1, type(line1))           #Return string
line2 = file2.readline()
print(line2, type(line2))
file2.close()

3
file3 = open("file2.txt")
# Read All Lines
lines = file3.readlines()          #Read All Lines From the File.
print(lines, type(lines))          #Return List of String
file3.close()


4
file4=open("file2.txt")
line = file4.readline()
while(line != ""):
    print(line)
    line = file4.readline()
file4.close()

""""Write"""
str = '''Abc Def 
Ghi Jkl
Mno Pqr
 Stu Vwx
   Yz'''
file5 = open("myfile.txt", "w")
file5.write(str)
file5.close()


""""Append """
str = '''Abc Def 
Ghi Jkl
Mno Pqr
 Stu Vwx
   Yz'''
file6 = open("file2.txt", "a")
file6.write(str)
file6.close()


# With Statement
# Open the file in read mode using 'with', which automatically closes the file
with open("file.txt", "r") as f:
# Read the contents of the file and print the contents
    print(f.read())
