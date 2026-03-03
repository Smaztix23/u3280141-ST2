#values
a = 10
b = 5
name = "Goober"
height = 178  #cm
weight = 70   #kg

#operations
sum_result = a + b
difference = a - b
product = a * b
division = a / b

bmi = weight / ((height / 100) ** 2)

greeting = "Hello, " + name + "!"
double_a = a * 2

#results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
print("Double of a:", double_a)
print("Greeting:", greeting)
print("BMI:", round(bmi, 2))