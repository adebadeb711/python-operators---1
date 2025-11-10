print("Enter Marks Obtained in 4 Subjects: ")

math = int(input("maths :"))
science = int(input("science :"))
english = int(input("english :"))
bengali = int(input("bengali :"))

sum = math+english+science+bengali
print("sum of math, english, science and bengali")
perc = (sum/400)*100
print(end="Percentage Mark = ")
print(perc)