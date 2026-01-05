#hello world
#Word document is there. Name 


print("Hello World!")

#Variables

string_variable = ("This is a string")
print(f"What is a string ? " + string_variable)

Integer_variable = (1)
print(f"You are always number " + str(Integer_variable))

float_variable = (3.14159)
print(f"Pi is an example of float. The valure of pi is: "+str(float_variable))

boolean_variable = True
print(boolean_variable)

#Input and verification using if statements
answer = input("What is the numerical value of Pi: ")
if answer == str(float_variable):
    print("Correct")
else:
    print("Incorrect")

# This is good but it does not take into account any other invalid options. 
