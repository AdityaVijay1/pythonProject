total = 0.0
count = 0
file_name=input("Enter a file name: ")
in_file = open(f"{file_name}.txt", 'r')
for line in in_file:
    score = float(line)
    total += score
    count += 1
    print(f"Score = {score}  Total so far = {total:.1f}")
in_file.close()
average = total / count
print(f"Average = {average:.1f}")