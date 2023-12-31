class DBException(Exception):
    ...


class DBNotFound(DBException):
    ...


class DuplicateKey(DBException):
    ...


class InvalidIdException(DBException):
    ...


class InvalidDict(DBException):
    ...
