# auto_gw_followup

This program takes in a list (not sure what shape they will take now) of tiles from Telgon for a given GW event and generates an RTML file that can be read by ACP Scheduler. The priority of each tile is determined by the probability of the tile containing a GW event, which is determined by Teglon. The RTML is then uploaded to our ACP scheduler, where we wait for it to observe an event.

## File structure

- `main.py` - Main file (believe it or not), pulls the rest of the functions together and executes them in the correct order
- `gen_rtml.py` - Takes the data from teglon and generates RTML pointings that can be uploaded
- `get_teglon_data.py` - [TODO] Gets data from teglon
- `parse_args.py` - Parses command line arguments so script can be changed manually
- `tile.py` - The structure that each tile should conform to
- `upload_to_acp_py` - [TODO] Uploads the RTML file to our ACP scheduler

## Note on using `playwright`

You first must `pip install -r requirements.txt` in a new conda env running python 3.10+, then run `playwright install` to install chromium and some other dependancies.

## Secrets.py

This is where you should put the password/username for our ACP scheduler. It's gitignored for obvious reasons.
To use this, you should first create the file, then write a function named `get_xyz_login` where `xyz` is the name of the website that you're logging into. This file should return a dictionary with a `username` and a `password`.
