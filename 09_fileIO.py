# File Input/Output
# open() function-takes 2 parameters: filename and mode.

# Modes
# r     –   open for reading
# w     -   open for writing
# a     -   open for appending
# +     -   open for updating.
# ‘rb’  -   will open for read in binary mode.
# ‘rt’  -   will open for read in text mode.

# WRITE
str = """
Abc Def 
Ghi Jkl
Mno Pqr
Stu Vwx
Yz
"""
file5 = open("myfile_01.txt", "w")
file5.write(str)
file5.close()


# Append
file6 = open("myfile_02.txt", "a")
file6.write(str)
file6.close()



# READ
# Approach-1.
file1 = open("myfile_02.txt", "r")
data = file1.read()
print(data)
file1.close()


# Approach-2.
file2 = open("myfile_01.txt")
# Read Single Line

line1 = file2.readline()
# Read one line from the file.

print(line1, type(line1))
# Return string

line2 = file2.readline()
print(line2, type(line2))
file2.close()


# Approach-3.
file3 = open("myfile_01.txt")
# Read All Lines

lines = file3.readlines()
# Read All Lines From the File.

print(lines, type(lines))
# Return List of String

file3.close()


# Approach-4.
file4 = open("myfile_01.txt")
line = file4.readline()
while line != "":
    print(line)
    line = file4.readline()
file4.close()


# With Statement
# Open the file in read mode using 'with', which automatically closes the file
with open("myfile_01.txt", "r") as f:
    # Read the contents of the file and print the contents
    print(f.read())


# Open Multiple Context files in a single "with" statement
with open("myfile_02.txt") as f1, open("myfile_01.txt") as f2:
    print(file1.read())
    print(file2.read())
