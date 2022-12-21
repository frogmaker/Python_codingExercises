#Użyj funkcji any(), aby określić, czy przeslana lista zawiera liczby parzyste


numbers1 = [1, 3, 5, 6, 7]
numbers2 = [1, 3, 5, 7, 9, 11, 13]
numbers3 = [2, 4, 6, 8]

def compareLists(list1, list2):
    return [numbers in list1 for numbers in list2] #pokazuje na których pozycjach listy2 są elementy zawarte w liście1


print(compareLists(numbers1, numbers2))
print()

def anyEvenOld(list):
    for num in list:
        if num % 2 == 0:
            return True
    return False


print(anyEvenOld(numbers1))
print(anyEvenOld(numbers2))
print(anyEvenOld(numbers3))
print()

def any_even(lista):
    return [nr % 2 == 0 for nr in lista]


print(any_even(numbers1))
print(any_even(numbers2))
print(any_even(numbers3))
print()

def any_even_with_any(lista):
    return any([nr % 2 == 0 for nr in lista])





print(any_even_with_any(numbers1))
print(any_even_with_any(numbers2))
print(any_even_with_any(numbers3))
print()

if (any_even_with_any(numbers1)):
    print("tak jest tu parzysta")
else:
    print("nie")

if (any_even_with_any(numbers2)):
    print("tak jest tu parzysta")
else:
    print("nie")
    
if (any_even(numbers2)):
    print("tak jest tu parzysta")
else:
    print("nie")

if ([0]):     # pusta list = False, lista z czymkolwiek, nawet z  [0], [False] = True
    print("tak jest tu parzysta")
else:
    print("nie")

# any - jakikolwiek - funkcja any SPRAWDZA, czy JAKAKOLWIEK wartość to True
# all - WSZYSTKIE

print()
def all_even(lista):
    return all([nr % 2 == 0 for nr in lista])

print(all_even(numbers3))
print(all_even(numbers1))


john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
}

jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}

def with_python(name):
    for skill in name['skills']:
        if skill == "Python":
            return True
    return False


print("czy python?", with_python(john))


required_skills = ['Python', 'JavaScript']


def has_required_skills(person, skillsreq):
    return all([skill in person['skills'] for skill in skillsreq])


def has_required_skills_debag(person, skillsreq):
    return [skill in person['skills'] for skill in skillsreq]


print()
print("debug1")
print(has_required_skills_debag(jane, required_skills))
print()


def has_required_skills_debug(person, skillsreq):

    skillsreq_cp = []
    for skill in skillsreq:
        if skill in person['skills']:
            skillsreq_cp.append(skill)
            # print(skillsreq)
            # print(skillsreq_cp)
            if skillsreq_cp == skillsreq:
                return True
            # else:
            #     print("jeszcze nie spełnia kryteriów")
    return False




    # return [skill == reqskill for skill in person['skills'] for reqskill in skillsreq]

print()
print("debug,john", has_required_skills_debug(john, required_skills))
print("debug,jane", has_required_skills_debug(jane, required_skills))
print()
print("czy john sie nadaje? ", has_required_skills(john, required_skills))
print("czy jane sie nadaje? ", has_required_skills(jane, required_skills))
