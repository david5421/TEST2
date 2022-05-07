

"""""
PLAIN ENGLISH
create a list to store 5 numbers (float)
capture user's input 5 times for their grades
each time we capture the user's input, we apprend te number to the list 

sort the list ascending, then splice the items starting at the index 2
once we have three highest number in the list, we sum them up and divide by 3 

output a message to the user

end

"""""

"""""
PSEUDO CODE
create list 
capture input
append number to list

capture input
append number to list

capture
append number to list

capture input
append number to list

capture input
append number to list

print message to user

"""""

# grade = []

# grade = input("Enter the 1st grade: ")
# grades.append(float(grade))

# grade = input("Enter the 2nd grade: ")
# grades.append(float(grade))

# grade = input("Enter the 3rd grade: ")
# grades.append(float(grades))

# grade = input("Enter the 4th grade: ")
# grades.append(float(grade))
 
# grade = input("Enter the 5th grade: ")
# grades.append(float(grade))

# grades.sort()

# grades = grades[2:]

# grades = sum(grades)
# result = grades / 3

# print("Average Grade {0:.2f}".format(result))

# print(grades)

"""""
CODE REFRACTOR USING LOOP

"""""
grades = []

for i in range(24):
    grades.append(float(input("Enter the grade: ")))

grades.sort()
avgGrades = sum(grades[2:]) / 24
avg = "Average Grade {0:.2f}%".format(avgGrades)
print("Average Grade {0:.2f}%".format(avgGrades))

total = 0
for i in range(10):
    n = grades[i]
    if avgGrades < n:
        total = total + 1
        print("Percentage of grades above the average ")

def printResult(total, average):
    percent = total/ 24
    result = percent * 100

## Analyze grades on a final exam.
infile = open ("grades.txt" , 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range (len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0  #number of grades above average
for grade in grades:
    if grade > average:
        num+=1
print("Number of grades:", len(grades))
print("Avergae grades:", average)
print("Percentage of grades above average: {0:.2f}%"
                    .format(100 * num / len(grades)))
