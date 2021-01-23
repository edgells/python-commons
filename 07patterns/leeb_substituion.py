"""
    里氏替换原则
    父类出现的地方子类一定能够出现
"""


class Database:
    def connect(self):
        pass

    def close_connect(self):
        pass

    def execute(self):
        pass

    def command(self):
        pass

    def insert(self, **kwargs):
        pass

    def select(self, username: str):
        pass

    def update(self, username):
        pass

    def delete(self, username):
        pass


class UserService:
    def __init__(self, db: Database):
        self._db = db

    @property
    def db(self):
        return self._db

    def create_user(self, username, password, *args, **kwargs):
        return self.db.insert(username=username, password=password)

    def find_user(self, username):
        return self.db.select(username)

    def update_user_info(self, username):
        return self.db.update(username)

    def delete_user(self, username):
        return self.db.delete(username)


class MysqlDatabase(Database):
    def __init__(self, db_type, db_host, db_port, db_name, db_user, db_password, *args, **kwargs):
        pass

    def insert(self, user):
        self.db.insert()

    def update(self, username):
        pass

    def select(self, username: str):
        pass

    def delete(self, username):
        pass


class OracleDatabase(Database):
    pass


def test():
    # 数据在mysql
    userService = UserService(MysqlDatabase())

    # 数据在Oracle
    userService = UserService(OracleDatabase())


if __name__ == '__main__':
    test()