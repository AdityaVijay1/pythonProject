#1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it. Remember to close your file.
champions_name=input("Enter your name: ")
out_file=open('name.txt', 'w')
out_file.write(champions_name)
out_file.close()


#2. Write code that opens "name.txt" and reads the name (as above) then prints
in_file=open('name.txt')
champions_name=in_file.read()
print("Your name is", champions_name)
in_file.close()

#3. Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result
total=0
in_file=open('numbers.txt')
number_of_lines=2
for i in range(number_of_lines):
    value=in_file.readline()
    total=total+int(value)
print('Total of first two numbers:',total)


#4. Write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.
total=0
in_file=open('numbers.txt')
numbers=in_file.readlines()
for i in numbers:
    total=total+int(i)
print('Total of all numbers:',total)

