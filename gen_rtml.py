# Needed to accept cli args
import os
from parse_args import parse_args

# mport tile class
import tile


# Generates the header of the RTML file being generated
def generate_header(output, observer: str, email: str) -> None:
    output.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
    output.write('<RTML version="2.3">\n')
    output.write("\n<Contact>\n")
    output.write("<User>" + observer + "</User>\n")
    output.write("<Email>" + email + "</Email>\n")
    output.write("</Contact>\n\n")


# Generates one observation to be scheuled given an RA, Dec, and Priority, and targ_name
# This is called for each tile from Telgon, which are sorted by priority according to their probability of containing a GW event


def generate_entry(
    output,
    ra: float,
    dec: float,
    priority: int,
    targ_name: str,
    observer: str,
    band: str,
    description: str,
) -> None:
    output.write('<Request bestefforts="true">\n')
    output.write("<ID>GW_Followup_" + targ_name + "</ID>\n")
    output.write("<UserName>" + observer + "</UserName>\n")
    output.write("<Observers>" + observer + "</Observers>\n")
    output.write(f"<Description>{description}</Description>\n")
    output.write("<Reason>Monitor=0</Reason>\n")
    output.write("<Project>Teglon GW Follow Up </Project>\n")
    output.write("<Schedule>\n")
    output.write("<Airmass>1.5</Airmass>\n")
    output.write("<Moon>\n")
    output.write("<Distance>150</Distance>\n")
    output.write("<Width>10</Width>\n")
    output.write("</Moon>\n")
    output.write("<Priority>" + str(priority) + "</Priority>\n")
    output.write("</Schedule>\n")
    output.write('<Target count="1" interval="1" autofocus="true">\n')
    output.write("<Name>GW_Followup" + targ_name + "</Name>\n")
    output.write("<Coordinates>\n")
    raval = f"{ra:.8f}"
    decval = f"{dec:.8f}"

    raval = f"{raval}"
    output.write("<RightAscension>" + raval + "</RightAscension>\n")
    decval = f"{decval}"
    output.write("<Declination>" + decval + "</Declination>\n")
    output.write("</Coordinates>\n")
    output.write("<PositionAngle>0</PositionAngle>\n")
    output.write('<Picture count="1">\n')
    output.write(f"<Name>{band}</Name>\n")
    output.write("<ExposureTime>300</ExposureTime>\n")
    output.write("<Binning>1</Binning>\n")
    output.write(f"<Filter>{band}</Filter>\n")
    output.write("</Picture>\n")
    output.write("</Target>\n")
    output.write("</Request>\n\n")


def gen_rtml(
    output: str, observer: str, email: str, band: str, description: str, data: list
):
    """
    Main function of the file, generates the RTML file based on the 'generate_header' and 'generate_entry' functions.
    It's then called by main.py to generate the entries for the data from teglon.
    """
    # If there isn't any data, then throw an error
    if data is None:
        raise ValueError(
            "No data was passed in, please make sure that you're getting data from Teglon"
        )

    # Delete pointings file if it already exists and remove it
    try:
        os.remove(output)
    except:
        pass

    # Open the file to write to
    output = open(output, "w")

    generate_header(email=email, observer=observer, output=output)

    # Generate the entries for each tile
    for tile in data:
        generate_entry(
            ra=tile.ra,
            dec=tile.dec,
            priority=11000
            - tile.rank,  # This will allow up to observe the secions in order of priority
            targ_name=tile.targ_name,
            observer=observer,
            output=output,
            description=description,
            band=band,
        )
