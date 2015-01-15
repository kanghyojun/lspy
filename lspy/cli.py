""" :mod:`lspy.cli` --- command line interface for lspy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from functools import reduce
from itertools import chain

import click

from .dig import listing_informs
from .represent import find_represent


def apply_funcs(funcs, data):
    return reduce(lambda x, y: y(x), funcs, data)


@click.command()
@click.argument('path', default='.')
@click.option('--all', 'all_', default=False,
              help='Include directory entries whose names begin'
                   'with a dot (.).')
@click.option('--long', 'long_', default=False,
              help='List in long format.')
def cli(path, all_, long_):
    infos = listing_informs(path)
    funcs = chain(
        find_represent(long_=long_)
    )
    for f in apply_funcs(funcs, infos):
        click.echo(f)
