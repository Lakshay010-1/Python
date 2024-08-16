# String - String is a data type.String is a sequence of characters enclosed in quotes.
# Strings are immutable
# String Indexing :
    # From Front - 0 based indexing
    # From Back  - -1 based indexing

# f-string (formatted string literals)
name=input("Enter Your Name:")
print(f"Hero Name is {name} \nHave a great day ")

# format
string1= "{1} is a good {0}".format("XYZphone", "smartphone")
print(string1)

# Method Chaining
sentence="My name is <|Name|> and i am a <|Occasion|>."
print(sentence.replace("<|Name|>", "Lakshay").replace("<|Occasion|>", "Student"))

# Different Ways of writing a string.
str1 ='abc'                             # Single quoted string
str2 = "abc"                            # Double quoted string
str3 = '''abc'''                        # Triple quoted string

"""Character """
chr=str1[1]             #Return character at the specified index
# print(chr)

""" String Slicing (alike sub-string)"""
# Positive
strPos1=str1[0:2]       #start from 0 index all the way till 2 (excluding 2)

# Negative
strNeg=str1[-3:-1]      # Same as str1[0:2]

# Skip
length=len(str1)
strSkip=str1[0:length:2]
print(strSkip)

# Technique
strPos2=str1[:2]        #same as str1[0:2]
strPos3=str1[0:]        #same as str1[0:len(str1)]

""" String Functions """
len=len(str1)                               # Return length of the string
TorF1=str1.endswith("c")                    # Returns True or false based on the condition
TorF2=str1.startswith("b")                  # Returns True or false based on the condition   
capit=str1.capitalize()                     # Capitalize the first alphabet only.
title=str1.title()                          # Capitalize the first alphabet of each word in the string.
low=str1.lower()                            # Convert the string in lowercase
upp=str1.upper()                            # Convert the string in uppercase
strip=str1.strip()                          # Remove all whitespace/blankspace in the string     
find=str1.find("b")                         # Returns the index from first occurence of the input string in the main string.
replace=str1.replace("B","BadBoatBus")      # Replace all occurence of the "old String" with the "new String"


"""" Escape Sequence """
s1="a \n b \n c \n"                 # New Line
s2=" a \t b \t c \t \n"             #tab space    
s3=" a \\ b \\ c \\ \n"             #backlash symbol
s4=" a \" b \" c \" \n"             #Double Quote Symbol
s5=" a \' b \' c \' \n"             #Single Quote Symbol
print("Line-1 \n",s1,"Line-2",s2,"Line-3",s3,"Line-4",s4,"Line-5",s5)