class Tile:
    ra: float
    dec: float
    priority: int
    targ_name: str

    def __init__(self, ra: float, dec: float, priority: int, targ_name: str):
        self.ra = ra
        self.dec = dec
        self.priority = priority
        self.targ_name = targ_name
