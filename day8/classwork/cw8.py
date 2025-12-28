# type() ფუნქცია ბრუნავს მონაცემის ტიპს
# მაგალითად, თუ გვაქვს მთელი რიცხვი, type(10) დაბრუნებს <class 'int'>


age = input("შეიყვანე შენი ასაკი: ")
print(type(age))  # input ფუნქცია ყოველთვის სტრინგს აბრუნებს


age = int(input("შეიყვანე შენი ასაკი: "))
print(type(age))  # ახლა დაბრუნდება <class 'int'>


num = 10                  # int
decimal = 3.14            # float
text = "Giorgi"           # str
is_student = True          # bool

print(type(num))
print(type(decimal))
print(type(text))
print(type(is_student))


name = "Gega"           # str
lastname = "Pirtskhelava" # str
age = 15                # int
height = 1.73          # float

print(type(name))
print(type(lastname))
print(type(age))
print(type(height))