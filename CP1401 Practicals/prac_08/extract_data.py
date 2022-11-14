"""Pseudocode
CP1401- Practical 8- Extract Data

# record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]
record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]
display "Last name:",record[1]
display "Born:",record[2]
display "{record[0]} was born in {record[2][2]} and was a great {record[-1]} player"w
"""

# record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]
record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]
print("Last name:", record[1])
print("Born:", record[2])
print(f"{record[0]} was born in {record[2][2]} and was a great {record[-1]} player")
