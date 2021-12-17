class User:
    #static variable
    __count = 0

    #method to work with class not with objects
    @classmethod
    def get_count(cls): #cls - class
        print(f'Total count = {cls.__count}')


    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password
        User.__count += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def login(self):
        return self.__login

    #setter as property can't exist without getter as property for the same value
    def password(self, password):
        self.__password = password

    def show_info(self):
        print("Name = " + self.__name + " login = " + self.__login)

class SuperUser(User):
    #static variable
    __count = 0

    #constructor reload
    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.__role = role

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    #method reload
    def show_info(self):
        super().show_info()
        print("Role = " + self.__role)


# class User tests
#
# #constructor and method test
# u = User('Gleb', 'Glebon', 'Airplane')
# u.show_info()
# #getters and setters test
# u.name = 'Dima'
# print(u.name)
# print(u.login)
# u.password('Car')

# #class method test
# User.get_count()

# class SuperUser tests
#
# #constructor and method test
su = SuperUser('name', 'login', 'password', 'role')
su.show_info()
# #getters and setters test
# su.name = 'su Dima'
# print(su.name)
# print(su.login)
# su.password('su Car')
#
# su.role = 'su role'
# print(su.role)

# #class method test
SuperUser.get_count()

