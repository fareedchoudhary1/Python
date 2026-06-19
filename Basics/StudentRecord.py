# WAP to calculate the percentage of a student in the subjects math, science, social science, english and hindi  
x = input("Enter the student name:")
a = int(input("Enter the marks of english:"))
b = int(input("Enter the marks of hindi:"))
c = int(input("Enter the marks of science:"))
d = int(input("Enter the marks of social science:"))
e = int(input("Enter the marks of math:"))
n = ((a+b+c+d+e)/500)*100
print("Percentage scored by student is:",n)