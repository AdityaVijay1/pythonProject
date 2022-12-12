"""CP1404 Practicals
Languages
Estimate Time: 10 minutes
Actual Time: 15 minutes"""


from CP1404_Practicals.prac_06.programming_language import ProgrammingLanguage


def main():

    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    language_names=[python,ruby,visual_basic]
    dynamic_langauges=[language.name for language in language_names if language.is_dynamic()]
    print()
    print('They dynamically typed languages are:')
    for i in dynamic_langauges:
        print(i)
    # for language in language_names:
    #     if language.is_dynamic():
    #         print(language.name)


main()