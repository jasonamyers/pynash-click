import click

@click.command()
@click.argument('source', nargs=-1, required=True)
@click.argument('dest', nargs=1)
def copy(source, dest):
    for fn in source:
        click.echo('move %s to folder %s' % (fn, dest))

if __name__ == '__main__':
    copy()