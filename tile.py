class Tile:
    ra: float
    dec: float
    percentile: float
    prob: float
    ebv: float
    a_lambda: float
    b_mag: float
    k_mag: float
    field_name: str
    lum_dist: float
    rank: int

    def __init__(
        self,
        ra: float,
        dec: float,
        percentile: float,
        field_name: str,
        prob: float,
        ebv: float,
        a_lambda: float,
        b_mag: float,
        k_mag: float,
        lum_dist: float,
        rank: int,
    ) -> None:
        self.ra = ra
        self.dec = dec
        self.percentile = percentile
        self.targ_name = field_name
        self.prob = prob
        self.ebv = ebv
        self.a_lambda = a_lambda
        self.b_mag = b_mag
        self.k_mag = k_mag
        self.lum_dist = lum_dist
        self.rank = rank

    def __str__(self) -> str:
        return f"ID: {self.targ_name} (RA: {self.ra}, Dec: {self.dec}), Percentile: {self.percentile}, Rank: {self.rank}"
