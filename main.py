from gen_rtml import gen_rtml

from parse_args import parse_args
from get_teglon_data import get_teglon_data
import sys

# Import tile class
import tile

# Global variables
# Global Variables for Header and Entry generation. Can be changed with CLI args, these are just the defaults.
observer: str = "Zander Schatzberg"
email: str = "zschatzberg@thacher.org"
band: str = "r"
description: str = (
    "Follow up on Gravitational Wave events detected by the LVK GW observatories."
)
exposure_time: int = 300
output_path: str = "./rtml_pointings/GW_Followup_Pointings.rtml"


def main(output_path: str, observer: str, email: str, band: str, description: str):
    # Parse args
    args = parse_args(sys.argv[1:])
    args = parse_args(sys.argv[1:])
    if args.get("observer"):
        observer = args.get("observer")
    if args.get("email"):
        email = args.get("email")
    if args.get("band"):
        band = args.get("band")
    if args.get("description"):
        description = args.get("description")

    # Get data from Teglon
    dummy_id = "S230830b"
    teglon_data: list = get_teglon_data(dummy_id)

    # Generate RTML file
    gen_rtml(
        output=output_path,
        observer=observer,
        email=email,
        band=band,
        description=description,
        data=teglon_data,
    )

    print("RTML file generated successfully!")


main(output_path, observer, email, band, description)
