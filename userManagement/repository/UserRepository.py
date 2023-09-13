from userManagement.config.DatabaseConfig import DataBaseConfig, pymysql
import pandas as pd

class UserRepository:

    @staticmethod
    def saveUser(user = None):
        try:
            connetion = DataBaseConfig.getConnection() #connetion db랑 연결된 객체
            cursor = connetion.cursor(pymysql.cursors.DictCursor) #DictCursor를 안쓰면 튜플로 나온다.
            sql = """
            insert into user_tb
            values(0, %s, %s, %s, %s)
            """
            # execute 사용시 db에 들어감, execute는 쿼리를 시작
            insertCount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
            connetion.commit() # commit이 되어야지만 insert가 된다. 트랜직션이 마무리가 되야함
            return insertCount
        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def getUsersAll():
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            select
                user_id as userId,
                username,
                password,
                name,
                email
            from
                user_tb
            """
            cursor.execute(sql)
            rs = cursor.fetchall()
            return rs
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def findUserByUsername(username=None):
            try:
                connection = DataBaseConfig.getConnection()
                cursor = connection.cursor(pymysql.cursors.DictCursor)
                sql = """
                select
                    user_id as userId,
                    username,
                    password,
                    name,
                    email
                from
                    user_tb
                where
                    username = %s
                """
                cursor.execute(sql, username)
                rs = cursor.fetchone()
                return rs
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def updateUser(user=None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            update user_tb
            set
               password = %s,
               name = %s,
               email = %s
            where
               user_id = %s
            """
            updateCount = cursor.execute(sql,
                        (user.get("password"), user.get("name"), user.get("email"), user.get("userId")))
            connection.commit()
            return updateCount
        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def deleteUser(user=None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            delete from
                user_tb
            where
                user_id
            """
            deleteCount = cursor.execute(sql,
                        (user.get("password"), user.get("name"), user.get("email"), user.get("userId")))
            connection.commit()
            return deleteCount
        except Exception as e:
            print(e)
            return 0


# if __name__ == "__main__":
#     userList = UserRepository.getUsersAll()
#     print(userList)
#
#     data = {
#         "userId": [1, 2, 3],
#         "username": ["aaa", "bbb", "ccc"],
#         "password": ["1234", "1111", "2222"],
#         "name": ["aaa", "bbb", "ccc"],
#         "email": ["aaa@gmail.com", "bbb@gmail.com", "ccc@gmail.com"]
#     }
#
#     # print(pd.Series(userList)) # 딕셔너리에 넣는다.
#     df = pd.DataFrame(userList)
#     print(df)


# fetchAll 다 가져옴
# fetchone 하나만 리턴하고 싶을 때 제일위에 있는 첫번째 행을 가져옴
# Series 하나의 시리즈만 가져옴


