class Group(Entity):
    def __init__(self, name) -> None:
        self._name = name
        self._players = None # reference na hráče?
        self._resources = None # nejspíše dát napevno eco/inf a rare řešit v poli bokem?