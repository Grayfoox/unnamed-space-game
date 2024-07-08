class Party(Entity):
    def __init__(self, name, owner) -> None:
        self._owner = owner
        self._name = name
        # zatím jednoduše 1 group - 1 party, později nám to dává možnost na komplexnejší situace apod.