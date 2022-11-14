# question_4()
file_name = open("name.txt", 'r')
name = file_name.read().strip()
file_name.close()
print(f"Greetings {name} !")

# question_5()
COUNT = 0
TOTAL=0
file_name = input("Filename: ")
threshold = float(input("Threshold: "))
print("Processing...")
file_open = open(file_name, 'r')

# print(values)

for i in file_open:
    TOTAL=TOTAL+1
    if float(i) > threshold:
        COUNT=COUNT+1
file_open.close()
percentage=(COUNT/TOTAL)*100
print(f"{COUNT} out of {TOTAL} ({percentage}) values in {file_name} are greater than {threshold} ")

# question_6()
input_file=input("Input file name: ")
search_value=input("Search value: ")
output_file=input("Output file name: ")
file_input=open(input_file,'r')
file_output=open(output_file,'w')
for i in file_input:
    if i.strip()==search_value:
        file_output.write(i)
file_input.close()
file_output.close()

# question_6() optional version 2
input_file=input("Input file name: ")

output_file=input("Output file name: ")
file_input=open(input_file,'r')
file_output=open(output_file,'w')
for i in file_input:
    if i.startswith('#'):
        file_output.write(i)
file_input.close()
file_output.close()

