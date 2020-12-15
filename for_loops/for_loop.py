ruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:                ->fruit is a new variable which will store particular list item one by one
    print(fruit)
    print(fruit + " Pie")
print(fruits)



for number in range(1, 11):        ->range 1-10
    print(number, end=' ')
print('\n')



# Don't change the code below
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row
maximum = -1
for score in student_scores:
    if score > maximum:
        maximum = score

print(f'The highest score in the class is: {maximum}')
