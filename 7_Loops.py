# Loops Statements
    # while loop
    # for loop 
    # for else loop

# while loop
j=0
while(j<=10):
    print(j)
    j+=1
# while loop on list
list1 = ["Luck","Light", "Near","Lawlight","list"]
i = 0
while(i<len(list1)):
    print(list1[i])
    i +=1       # or i=i+1

#for loop
# range function
for i in range(10):
    print(i)

for i in range(0,10,2):
    print(i,end=" ")

list2 = [1, 4, 6, 234, 6, 764]
for item in list2:
    print(item)

# for-else loop
tuple1=(1,2,5,3,7,"ZERO")
for item in tuple1:
    print(item)
else:
    print("done")       # this is printed when the loop Completely Executed.
 
#‘break’ is used to come out of the loop when specific condition encountered. It instructs the program to exit the loop.
for i in range(100):
    if(i == 13):
        break # Exit the loop right now
    print(i)

#‘continue’ is used to stop the current iteration of the loop and continue to the next one. It instructs the Program to “skip this iteration”.
for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)

#'pass' is a null statement. It instructs to “do nothing”.
for i in range(645):
    pass
