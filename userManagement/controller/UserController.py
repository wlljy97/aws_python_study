from userManagement.util.ResponseUtil import ResponseEntity
from userManagement.repository.UserRepository import UserRepository

class UserController:

    # @staticmethod
    # def showUserAllUser(Users = None):
    #     from userManagement.repository.UserRepository import UserRepository
    #     responseBody = bool(UserRepository.getUsersAll(Users))
    #     return ResponseEntity(body=responseBody)

    @staticmethod
    def registerUser(User = None):
        from userManagement.repository.UserRepository import UserRepository
        responseBody = bool(UserRepository.saveUser(User))
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getUsersAll():
        responseBody = UserRepository.getUsersAll()
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getUser(username=None):
        responseBody = UserRepository.findUserByUsername(username)
        return ResponseEntity(body=responseBody)