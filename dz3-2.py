list_boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard'] 
list_girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(list_boys) != len(list_girls):
    print("Кто-то может остаться без пары")
else:
    for boys, girls in zip(sorted(list_boys),sorted(list_girls)):
        print(boys, " and ", girls)