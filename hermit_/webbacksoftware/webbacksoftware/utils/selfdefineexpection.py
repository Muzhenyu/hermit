class not_library_user_error(Exception):
    def __init__(self,error):
        super().__init__(self)
        self.error=error

    def __str__(self):
        return self.error

class not_User_obj_error(Exception):
    def __init__(self,error):
        super().__init__(self)
        self.error=error

    def __str__(self):
        return self.error

class Not_exist(Exception):
    def __init__(self,error,errorcode=None):
        super().__init__(self)
        self.error=error
        self.errorcode=errorcode

    def __str__(self):
        return self.error

