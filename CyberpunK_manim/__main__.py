import json

import click
import requests
from click_default_group import DefaultGroup

from . import convert

@click.group(cls=DefaultGroup, default="present", default_if_no_args=True)
# @click.version_option(__version__, "-v", "--version")
@click.help_option("-h", "--help")
def cli() -> None:
    """
    CyberpunK Manim command-line utilities.

    If no command is specified, defaults to `present`.
    """

# cli.add_command(convert.convert)
# cli.add_command(present)
# cli.add_command(checkhealth)
# cli.add_command(init)
# cli.add_command(list_scenes)
# cli.add_command(render)
# cli.add_command(wizard)

if __name__ == "__main__":
    cli()