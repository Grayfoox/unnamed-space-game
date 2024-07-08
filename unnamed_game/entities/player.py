class Player(Entity):
    def __init__(self, name, email, group) -> None:
        self._name = name
        self._email = email
        self._group = group

        