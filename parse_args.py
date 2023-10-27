import sys, re


def parse_args(args: list[str]) -> dict[str, str]:
    # Returns a dictionary of arguments passed to through the CLI.
    # How to use: --arg="value", --observer="Your Name"

    args = {}

    for arg in sys.argv[1:]:
        var = re.search("\-\-([A-Za-z]*)", arg)  # optional value assignment
        var = var.group(1)
        value = re.search("\=(.*)", arg)
        value = value.group(1) if value else None
        args[var] = value

    return args
