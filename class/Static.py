class UserInfo:

    # cls변수(클래스변수 == static)
    adminUser = {
        "username": "root",
        "password": "1q2w3e4r"
    }

    def __init__(self):
        self.adminUser = {
            "username": "user1",
            "password": "1234"
        }

    @classmethod
    def showAdminUser(cls): # 여기서 cls는 제일 위에 정의해둔 cls를 의미함
        print("[showAdminUser")
        print(cls.adminUser)

class User:

    # 멤버변수는 안에 정의해 놓는다.
    # init에 정의해놓는다.
    def __init__(self):
        self.username = None
        self.password = None
        self.name = None
        self.email = None

    @staticmethod
    def showUserClassInfo():
        print("그냥 실행할 수 있는 메소드")

if __name__ == "__main__":
    userInfo = UserInfo()
    print(userInfo.adminUser)
    print(UserInfo.adminUser)

    userInfo.showAdminUser()
    UserInfo.showAdminUser()

    User.showUserClassInfo() # static 메소드




