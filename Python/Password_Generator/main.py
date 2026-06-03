from generation import GeneratePassword

try:
     user_input= int(input("Enter the Length of the Password: "))
     if(user_input<1):
          print("Password length Should be greater than 0")
     else:GeneratePassword(user_input)
     
except ValueError:
     print("Invalid input, Please Enter a Number")
     exit()