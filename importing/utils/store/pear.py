def peep(iterable,finder,expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFound(f"{expected} not found")


class NotFound(Exception):
    pass