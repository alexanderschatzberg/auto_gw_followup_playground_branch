"""
placeholder for eventual call that will get data from Teglon 
"""
import tile


def get_teglon_data() -> list:
    tile1 = tile.Tile(ra=0.0, dec=0.0, priority=1, targ_name="test")
    tile2 = tile.Tile(ra=0.0, dec=0.0, priority=1, targ_name="thisisareallyspecialtest")

    data: list = [tile1, tile2]
    return data
