""" :mod:`lspy.cli` --- command line interface for lspy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import click

from .dig import listing_informs
from .represent import only_names

@click.group()
def cli():
    pass


@cli.command()
@click.argument('path', default='.')
@click.option('--a', default=False, type=bool)
def find(a, path):
    infos = listing_informs(path)
    for name in only_names(infos):
        print(name)
