#!/usr/bin/env python3

def admin_login(username, password):
    
    return  "Access granted" if (username =="admin" or username == "ADMIN") and password == "12345" else "Access denied"

def hows_the_weather(temperature):
  if temperature <= 40:
      return "It's brisk out there!"
  elif 40 < temperature <= 65:
      return "It's a little chilly out there!"
  elif temperature >85:
      return "It's too dang hot out there!"
  else:
      return "It's perfect out there!"
   

def fizzbuzz(num):
   if num % 3 == 0 and num % 5 == 0:
       return "FizzBuzz"
   elif num % 5 == 0:
       return "Buzz"
   elif num % 3 == 0:
       return "Fizz"
   else:
       return num

def calculator(operation, num1, num2):
    if operation == '+' :
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')
        return None    

#print(admin_login("ADMI", "12345"))
#print(hows_the_weather(40))
#print(fizzbuzz(11))
print(calculator('*', 3, 3))