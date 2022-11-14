# question_1()
data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                "Something else that's very important = 9.2%", "x = 42%"]
for i in data_strings:
    start_value=i.find('=')
    print(float(i[start_value+2:-1]))

#question_2()
dob=input("DOB: ")
NEXT_YEAR=2023
year=dob[-4:len(dob)]
print("You were born in",year)
print(f"You will turn {NEXT_YEAR-int(year)} in 2023")

#question_03
subject_code=input('Enter subject code: ')
while subject_code!='':
    class_level=int(subject_code[2])

    if class_level==1:
        year_string='first-year'
    elif class_level==2:
        year_string='second-year'
    elif class_level==3:
        year_string='third-year'
    else:
        year_string='Masters or other'
    if subject_code.startswith('CP'):
        it_string=' IT'
    elif subject_code.startswith('MA'):
        it_string=' Math'
    elif subject_code.startswith('PH'):
        it_string=' Public Health'
    else:
        it_string=''
    print(f"That is a {year_string}{it_string} subject.")
    subject_code = input('Enter subject code: ')