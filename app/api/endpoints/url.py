
LOGIN = ''


class UserService:
    def login(self):
        pass


class Url(object):
    def router(self, menu):
        if menu == LOGIN:
            UserService().login()