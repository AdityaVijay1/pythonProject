"""Pseudocode

function main():
    for i in range(0, 3176, 635):
        minutes, seconds = Seconds_To_Minutes(i)
        print(f"{i} seconds is {minutes}m {seconds}s")
    print()
    favourite_duration = int(input("Favourite duration in seconds: "))
    minutes, seconds = Seconds_To_Minutes(favourite_duration)
    print(f"You love {minutes}m {seconds}s")


function Seconds_To_Minutes(Seconds):
    total_minutes = Seconds // 60
    total_seconds = Seconds % 60
    return total_minutes, total_seconds


main()

"""


def main():
    for i in range(0, 3176, 635):
        minutes, seconds = Seconds_To_Minutes(i)
        print(f"{i} seconds is {minutes}m {seconds}s")
    print()
    favourite_duration = int(input("Favourite duration in seconds: "))
    minutes, seconds = Seconds_To_Minutes(favourite_duration)
    print(f"You love {minutes}m {seconds}s")


def Seconds_To_Minutes(Seconds):
    total_minutes = Seconds // 60
    total_seconds = Seconds % 60
    return total_minutes, total_seconds


main()
