import click

@click.command()
@click.argument('name', type=str)
def hello(name):
    click.echo('Hello {}'.format(name))

if __name__ == '__main__':
    hello()