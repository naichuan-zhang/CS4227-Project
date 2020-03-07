from user.userbuilder.abstractuserbuilder import AbstractUserBuilder


class UserDirector:
    """the director"""
    def __init__(self, builder):
        super(UserDirector, self).__init__()
        self.__builder = builder

    def construct(self, username, password, email, icon):
        return self.__builder.reset()\
            .set_username(username)\
            .set_password(password)\
            .set_email(email)\
            .set_icon(icon)\
            .save().get_user()
