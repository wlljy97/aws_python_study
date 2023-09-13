import pandas as pd
from userManagement.controller.UserController import UserController
from userManagement.entity.User import User


class UserView:

    @staticmethod
    def register():
        from userManagement.entity.User import User
        from userManagement.controller.UserController import UserController
        print("[사용자 등록 화면]")
        username = input("사용자 이름 >>> ")
        password = input("비밀번호 >>> ")
        name = input("이름 >>> ")
        email = input("이메일 >>> ")

        response = UserController.registerUser(User(
            username=username,
            password=password,
            name=name,
            email=email
        ))

        if not response.__dict__.get("body"):
            print("데이터를 추가하는 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")

    # @staticmethod
    # def showUserAll():
    #     from userManagement.repository.UserRepository import UserRepository
    #     user_list = UserRepository.getUsersAll()
    #     if user_list:
    #         for user in user_list:
    #             print(f"사용자 ID: {user['userId']}, 사용자 이름: {user['username']}, 이름: {user['name']}, 이메일: {user['email']}")
    #     else:
    #         print("데이터를 조회하는 중 오류가 발생하였습니다.")

    @staticmethod
    def showAllUser():
        response = UserController.getUsersAll()
        print("[ 전체 사용자 조회 ]")
        if bool(response.body):
            print(pd.DataFrame(response.body))
        else:
            print("조회 할 데이터가 없습니다.")

    @staticmethod
    def showFindUser():
        print("[ username으로 사용자 정보 검색 ]")
        username = input("검색하실 사용자이름을 입력하세요 >>> ")
        response = UserController.getUser(username)
        if bool(response.body):
            print(pd.Series(response.body))
        else:
            print("조회 할 데이터가 없습니다.")

    @staticmethod
    def updateUser():
        print("[ 사용자 정보 수정 ]")
        response = UserController.getUsersAll()
        if not bool(response.body):
            print("수정할 사용자 정보가 없습니다.")
            return
        df = pd.DataFrame(response.body)
        print()
        userId = input("수정하실 userId를 입력하세요 >>> ")
        index = df.index[df["userId"] == int(userId)].values[0]
        print(df.iloc[index])
        print()
        UserView.showUpdateMenu(response.body[index])

    # loc 데이터프레임에서 사용됨, 찾고자 하는 조건
    # iloc index값을 찾음

    @staticmethod
    def showUpdateMenu(oldUser):
        newUser = User()
        while True:
            print("1. password 수정")
            print("2. name 수정")
            print("3. email 수정")
            print("s. 저장")
            print("c. 취소")
            select = input("메뉴 선택 >>> ")

            if select == "c":
                return None
            elif select == "s":
                return newUser
            elif select == "1":
                pass
            elif select == "2":
                pass
            elif select == "3":
                pass
            else:
                print("선택하신 번호는 등록되지 않은 메뉴입니다.")

        return None
