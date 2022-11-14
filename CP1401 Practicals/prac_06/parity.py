"""2. Parity

function main():
    get Number
    Parity = Calculate_Parity(Number)
    Reply = is_Number_Odd(Parity)
    Display_Parity(Parity, Reply,Number)


function Display_Parity(Parity, Reply, Number):
    display "Parity of {Number} should be {Reply}: {Parity}"


function Calculate_Parity(Number):
    Parity = Number % 2
    return Parity


function is_Number_Odd(Number):
    display "To check if number is odd: "
    if Number % 2 == 1:
        Reply = 1
        display "True"
    else:
        Reply = 0
        display "False"
    return Reply



"""


def main():
    Number = int(input("Enter the number: "))
    Parity = Calculate_Parity(Number)
    Reply = is_Number_Odd(Parity)
    Display_Parity(Parity, Reply,Number)





def Display_Parity(Parity, Reply, Number):
    print(f"Parity of {Number} should be {Reply}: {Parity}")


def Calculate_Parity(Number):
    Parity = Number % 2
    return Parity


def is_Number_Odd(Number):
    print("To check if number is odd: ",end='')
    if Number % 2 == 1:
        Reply = 1
        print("True")
    else:
        Reply = 0
        print("False")
    return Reply
main()
