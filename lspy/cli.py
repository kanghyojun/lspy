""" :mod:`lspy.cli` --- command line interface for lspy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from functools import reduce
from itertools import chain

import click

from .dig import listing_informs
from .represent import find_represent
from .filter import find_filters
from .sort import find_sort

__all__ = 'cli', 'apply_funcs',

def apply_funcs(funcs, data):
    return reduce(lambda x, y: y(x), funcs, data)


@click.command()
@click.argument('path', default='.')
@click.option('--all', 'all_', default=False, is_flag=True,
              help='Include directory entries whose names begin'
                   'with a dot (.).')
@click.option('--long', 'long_', default=False, is_flag=True,
              help='List in long format.')
@click.option('--time', 'time_', default=False, is_flag=True,
              help='sort by modification time.')
def cli(path, all_, long_, time_):
    infos = listing_informs(path)
    funcs = chain(
        find_sort(time_=time_),
        find_filters(all_=all_),
        find_represent(long_=long_)
    )
    for f in apply_funcs(funcs, infos):
        click.echo(f)
