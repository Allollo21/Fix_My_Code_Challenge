#!/usr/bin/python3
"""
User Model
"""
import hashlib
import uuid

class User:
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hashed in MD5
    """

    def __init__(self):
        """Initialize a new user with a unique `id`."""
        self.__id = str(uuid.uuid4())
        self.__password = None

    @property
    def id(self):
        """ID getter."""
        return self.__id

    @property
    def password(self):
        """Password getter."""
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter:
        - Sets to `None` if `pwd` is `None` or not a string.
        - Hashes `pwd` in MD5 before assigning to `__password`.
        """
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """
        Validates the password:
        - Returns `False` if `pwd` is `None`, not a string, or `__password` is `None`.
        - Compares `__password` with the MD5 hash of `pwd`.
        """
        if pwd is None or not isinstance(pwd, str) or self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password

if __name__ == '__main__':
    # Test cases for the User class
    user_1 = User()
    assert user_1.id, "New User should have an id"

    user_2 = User()
    assert user_1.id != user_2.id, "User.id should be unique"

    u_pwd = "myPassword"
    user_1.password = u_pwd
    assert user_1.password != u_pwd, "User.password should be hashed"

    assert user_2.password is None, "User.password should be None by default"

    user_2.password = None
    assert user_2.password is None, "User.password should be None if set to None"

    user_2.password = 89
    assert user_2.password is None, "User.password should be None if set to an integer"

    assert user_1.is_valid_password(u_pwd), "is_valid_password should return True if it's the right password"
    assert not user_1.is_valid_password("Fakepwd"), "is_valid_password should return False if it's not the right password"
    assert not user_1.is_valid_password(None), "is_valid_password should return False if compared with None"
    assert not user_1.is_valid_password(89), "is_valid_password should return False if compared with an integer"
    assert not user_2.is_valid_password("No pwd"), "is_valid_password should return False if no password set before"

