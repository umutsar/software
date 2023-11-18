import argparse

class PersonalInformation:
    def __init__(self, name, surname, football_team, football_team_short):
        self.name = name;
        self.surname = surname;
        self.football_team = football_team;
        self. football_team_short = football_team_short;

    def combinate(self):
        pass
class Dates:
    def __init__(self, birthday_year, birthday_mounth, birthday_day):
        self.birthday_year = birthday_year;
        self.birthday_mounth = birthday_mounth;
        self.birthday_mounth = birthday_day;

class AnotherKeywords:
    def __init__(self, keyword1, keyword2, keyword3, keyword4, keyword5):
        self.keyword1 = keyword1;
        self.keyword2 = keyword2;
        self.keyword3 = keyword3;
        self.keyword4 = keyword4;
        self.keyword5 = keyword5;

class Symbols:
    def __init__(self, default_symbols, symbol1, symbol2, symbol3):
        self.default_symbols = ['.', ',', '!', '#', '-', '*', '_'];
        self.symbol1 = symbol1;
        self.symbol2 = symbol2;
        self.symbol3 = symbol3;
        
class Another_date:
    def __init__(self, another_year, another_mounth, another_day):
        self.another_year = another_year;
        self.another_mounth = another_mounth;
        self.another_day = another_day;

def setup():
    name = input("Enter name of target person: ");
    date_year = input("Do you know year of birthday of target person? y/n: ");
    date_mounth = input("Do you know mounth of birthday of target person? y/n: ");
    date_day = input("Enter birthday of target person? y/n: ");

birthday_values = []
def birthday():
    if date_year == 'y' and date_mounth == 'n' and date_day == 'n':
        year = input("Enter year: ")
        mounth = None
        day = None
        birthday_values.append(year)

    elif date_year == 'y' and date_mounth == 'y' and date_day == 'n':
        year = input("Enter year: ")
        mounth = input("Enter mounth: ")
        day = None
        birthday_values.append(year)
        birthday_values.append(mounth)

    elif date_year == 'y' and date_mounth == 'y' and date_day == 'y':
        year = input("Enter year: ")
        mounth = input("Enter mounth: ")
        day = input("Enter day: ")
        birthday_values.append(year)
        birthday_values.append(mounth)
        birthday_values.append(day)

    elif date_year == 'y' and date_mounth == 'n' and date_day == 'y':
        year = input("Enter year: ")
        mounth = None
        day = input("Enter day: ")
        birthday_values.append(year)
        birthday_values.append(day)

    elif date_year == 'n' and date_mounth == 'y' and date_day == 'y':
        year = None
        mounth = input("Enter mounth: ")
        day = input("Enter day: ")
        birthday_values.append(mounth)
        birthday_values.append(day)

    elif date_year == 'n' and date_mounth == 'y' and date_day == 'n':
        year = None
        mounth = input("Enter mounth: ")
        day = None
        birthday_values.append(mounth)

    elif date_year == 'n' and date_mounth == 'n' and date_day == 'y':
        year = None
        mounth = None
        day = input("Enter day: ")
        birthday_values.append(day)

    elif date_year == 'n' and date_mounth == 'n' and date_year == 'n':
        year = None
        mounth = None
        day = None
        birthday_values = []

    else:
        print("Please enter valid values! ")
        birthday_values = []
        birthday()
birthday()

# ***********************************************************************************

birthday_values_count = len(birthday_values);
if birthday_values_count > 0:
    for i in range(0,birthday_values_count, 1):
        print(birthday_values[i])

print("**This program includes (. , ! # - * _) characters as default.");
print("If you want to add another symbol character, please enter write here.");
print("You can press 0 for skip this step.")
another_symbols = input("For example: $½&[]\/");

if another_symbols == 0:
    pass

all_keywords = []
while 1:
    is_continue = input("If you want to add another keyword, please press 1 , else please press 0.");
    if is_continue == 1:
        another_keyword = input("Enter another keyword do you want");
        all_keywords.append(another_keyword)
        print(all_keywords)
    elif is_continue == 0:
        break
    else:
        print("Please press 1 or 0 !!!");

all_things = []
all_things.append(name)
all_things.append(surname)

all_things.append(date_year)
all_things.append(date_mounth)
all_things.append(date_day)

all_things.append(symbol)
all_things.append(date_year)
all_things.append(date_year)
all_things.append(date_year)


# parser = argparse.ArgumentParser(description="Belirtilen uzunluk aralığında rastgele kelime üretir.")

# parser.add_argument("-a", "--min-length", type=int, help="Minimum kelime uzunluğu")
# parser.add_argument("-b", "--max-length", type=int, help="Maksimum kelime uzunluğu")

# args = parser.parse_args()
# min_lenght = args.min_lenght
# max_lenght = args.max_lenght
