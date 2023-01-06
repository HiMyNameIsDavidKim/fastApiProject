from pydantic import BaseModel


class User(BaseModel):
    username: str
    pwd: str

    def get_username(self):
        return self.username

    def get_pwd(self):
        return self.pwd