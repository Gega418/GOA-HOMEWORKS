member1 = int(input("შეიყვანე პირველი ოჯახის წევრის ასაკი: "))
member2 = int(input("შეიყვანე მეორე ოჯახის წევრის ასაკი: "))
member3 = int(input("შეიყვანე მესამე ოჯახის წევრის ასაკი: "))
member4 = int(input("შეიყვანე მეოთხე ოჯახის წევრის ასაკი: "))

# 25 წლის შემდეგ ასაკის გამოთვლა
print(member1 + 25)
print(member2 + 25)
print(member3 + 25)
print(member4 + 25)


name = input("შეიყვანე შენი სახელი: ")
print(type(name))  # ყოველთვის str, რადგან input სტრინგს აბრუნებს



age = int(input("შეიყვანე შენი ასაკი: "))
age_str = str(age)
print(age_str)
print(type(age_str))  # <class 'str'>


# str() — გადაქცევს ნებისმიერ მონაცემს ტექსტად (სტრინგად)
# int() — გადაქცევს მონაცემს მთელ რიცხვად (integer)
# float() — გადაქცევს მონაცემს ათწილად რიცხვად (decimal number)