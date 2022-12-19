"""
CP1404- Practical Week 1 menus.py

Pseudocode

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""

champions_name = input("Enter name: ")
choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print("Hello", champions_name)
    elif choice == 'G':
        print("Goodbye", champions_name)
    else:
        print("Invalid choice")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>> ").upper()
print("Finished.")
