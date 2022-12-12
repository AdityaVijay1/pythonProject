"""
Wimbledon
Estimate: 40 minutes
Actual:   1 hour
"""


def main():
    global player_information, tennis_player_details, name_and_championships_count, champions_name
    filename = "wimbledon.csv"
    player_information = []
    tennis_player_details = []
    name_and_championships_count = {}
    champions_name = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            player_information.append(line)
    for i in player_information:
        detail = i.strip('\n').split(',')
        tennis_player_details.append(detail)
    get_championship_count()
    country_code = get_country_code()
    display_results(country_code)


def get_championship_count():
    for i in tennis_player_details:
        if i[2] == 'Champion':
            pass
        else:
            champions_name.append(i[2])
    for i in champions_name:
        name_and_championships_count[i] = champions_name.count(i)


def get_country_code():
    country_code = []
    for i in tennis_player_details:
        if i[1] == 'Country':
            pass
        else:
            country_code.append(i[1])
    country_code = set(country_code)
    country_code = list(country_code)
    country_code.sort()
    return country_code


def display_results(country_code):
    print("Wimbledon Champions:")
    for name in name_and_championships_count:
        print(f"{name} {name_and_championships_count[name]}")
    print()
    print(f"These {len(country_code)} countries have won Wimbledon: ")
    for i in country_code:
        if i == country_code[-1]:
            print(i)
        else:
            print(i, end=', ')


main()
