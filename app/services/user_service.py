from app.models.user import User


class UserService:
    def login(self, username, pwd):
        user = User(username, pwd)
        print(f'리액트에서 보낸 유저이름 : {user.get_username()}')
        print(f'리액트에서 보낸 비밀번호 : {user.get_pwd()}')