from random import randint

class Position:
    def __init__(self,title_position,salary):
        self.title_position = title_position
        self.salary = salary

class Company:
    def __init__(self,title):
        self.title = title
        self.positions = [Position("директор",500000),Position("программист",200000),Position("экономист",100000)]#список должностей
        self.persons = [Person(1,"Романов",self.positions[0])] #по умолчанию сотрудников в компании нет

    def show_info(self):
        print("В компании",self.title,"работают следующие сотрудники")
        for i,person in enumerate(self.persons):
            print(f"{i + 1}) {person.get_info()}")

    def add_person(self):
        man_id = len(self.persons)
        fio = input("Введите имя")
        new_person = Person(man_id + 1,fio,self.positions[randint(1,2)])
        self.persons.append(new_person)
        print("Сотрудник",fio,"принят в штат! Поздравляем!")

    def remove_person(self):
        fio = input("Введите имя сотрудника, которого сокращаем")
        for man in self.persons:
            if man.fio == fio:
                self.persons.remove(man)
                print("Сотрудник",fio,"сокращен с должности")
        self.show_info()

    def remove_position(self):
        position = input("Введите название должности с которой сокращаем всех сотрудников")

        for man in self.persons:
            if man.position.title_position == position:
                self.persons.pop(man.id - 1) #вычитаем 1 для получения индекса сотрудника, который удаляем
                print("Сотрудник",man.fio,"сокращен с должности",position)
        self.show_info()



class Person:
    #конструктор класса описывает структуру каждого объекта класса
    # self - это ссылка на объект, который вызывает конструктор(метод)
    def __init__(self,id,fio,position):
        self.id = id
        self.fio = fio
        self.position = position
    def get_info(self):
        return f"Сотрудник {self.fio} " \
               f"работает в должности {self.position.title_position} " \
               f"имеет оклад {self.position.salary}"

# man1 = Person("Иванов","Программист",100000)
# man2 = Person("Петров","Экономист",90000)
# man3 = Person("Сидоров","Юрист",80000)

# men = [man1,man2,man3]

my_company = Company("IT Start")
# my_company.show_info()
my_company.show_info()
for i in range(3):
    my_company.add_person()
my_company.show_info()
# my_company.remove_person()
my_company.remove_position()
# print(my_company.persons[0].fio)