import tile
from secrets import get_teglon_pass
import requests as req


def get_teglon_data(id: str) -> list:
    """
    Makes an HTTP request to Teglon and returns a list of tiles given the ID of a GW alert.
    """
    teglon_logininfo = get_teglon_pass()

    url: str = f"https://ziggy.ucolick.org/teglon_events/{id}/{id}_THACHER_4D_0.9_bayestar.fits.gz.txt"

    r = req.get(url, auth=(teglon_logininfo["username"], teglon_logininfo["password"]))

    if r.status_code != 200:
        raise Exception(
            "There was an issue with the request to Teglon. That's all we know."
        )

    return parse_teglon(r.text)


def parse_teglon(data: str) -> list:
    """
    parses the text file that we recieve from teglon into a list of tiles
    """
    tile_list: list = []

    lines = data.split("\n")

    # Breaks the data into a list of strings, where each line is an element
    for n, line in enumerate(lines):
        if len(line) == 0 or line[0] == "#":
            continue
        entry = line.split(" ")

        if entry[0] == "Field_Name" or len(entry) < 10:
            continue
        tile_list.append(
            tile.Tile(
                field_name=entry[0],
                ra=float(entry[1]),
                dec=float(entry[2]),
                prob=float(entry[3]),
                percentile=float(entry[4]),
                ebv=float(entry[5]),
                a_lambda=float(entry[6]),
                lum_dist=float(entry[7]),
                b_mag=float(entry[8]),
                k_mag=float(entry[9]),
                rank=n - 73,  # To account for the header
            )
        )

    return tile_list
