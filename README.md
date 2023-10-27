# auto_gw_followup

This program takes in a list (not sure what shape they will take now) of tiles from Telgon for a given GW event and generates an RTML file that can be read by ACP Scheduler. The priority of each tile is determined by the probability of the tile containing a GW event, which is determined by Teglon. The RTML is then uploaded to our ACP scheduler, where we wait for it to observe an event.

## File structure

- `main.py` - Main file (believe it or not), pulls the rest of the functions together and executes them in the correct order
- `gen_rtml.py` - Takes the parsed data from `get_teglon_data()` and generates RTML pointings that can be uploaded
- `get_teglon_data.py` - Gets and parses data from teglon based on an event ID
- `parse_args.py` - Parses command line arguments so script can be changed manually
- `tile.py` - The structure that each tile should conform to. Has fields like RA, Dec, and Rank.
- `upload_to_acp.py` - [TODO] Uploads the RTML file to our ACP scheduler

## Next steps

- Add a listener to the slack channel to determine when an event has beem triggered
- Finish `upload_to_acp`

## How to set up the conda env

- First create a conda enviroment using the command `conda create -n gw_followup python=3.10 pip`
- While in the project's directory run the command `pip install -r requirements.txt` to install all dependencies

## Note on using `playwright`

You first must `pip install -r requirements.txt` in a new conda env running python 3.10+, then run `playwright install` to install chromium and some other dependancies.

## Secrets.py

This is where you should put the password/username for our ACP scheduler. It's gitignored for obvious reasons.
To use this, you should first create the file, then write a function named `get_xyz_login` where `xyz` is the name of the website that you're logging into. This file should return a dictionary with a `username` and a `password`.
