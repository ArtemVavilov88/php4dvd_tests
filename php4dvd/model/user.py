class User(object):

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def admin(cls):
        return cls(username="admin", password="admin")

    #random values for username and password
    @classmethod
    def random_data(cls):
        from random import randint
        return cls(username="user" + str(randint(0, 1000)), password="pass" + str(randint(0, 1000)))














