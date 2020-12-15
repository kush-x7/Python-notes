dictionary have 2 item ->key , value

-----> created dictionary

programming_dictionary =
{
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

------> Printing a dictionary

print(programming_dictionary["Bug"])      -> An error.......


------->entering more in a programming_dictionary

programming_dictionary["loop"]= "added a new item in a dictionary"


empty_dictionary={}   ->created a empty a dictionary

-------------------------------------------------------

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif score > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)
