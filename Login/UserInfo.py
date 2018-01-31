

class UserInfo:

    def __init__(self, userName, userEmail):
        self.__userName = userName
        self.__userEmail = userEmail

    @property
    def userName(self):
        return self.__userName

    @userName.getter
    def userName(self):
        return self.__userName

    @property
    def userEmail(self):
        return self.__userName

    @userEmail.getter
    def userEmail(self):
        return self.__userEmail

