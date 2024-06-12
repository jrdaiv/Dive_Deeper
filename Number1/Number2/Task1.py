#

response1 = int(input("Please enter three numbers: "))
response2 = int(input("Please enter the second number: "))
response3 = int(input("Please enter the third number: "))

if response1  >= response2 and response1 >= response3:
    largest = response1
elif response2 >= response1 and response2 >= response3:
    largest = response2
else:
    largest = response3

print("The largest number is: ",largest)
