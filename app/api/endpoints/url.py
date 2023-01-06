from app.services.user_service import UserService

LOGIN = ''


class Url(object):
    def router(self, menu):
        if menu == LOGIN:
            UserService().login()