import click

@click.command()
@click.option('--french', default=False, help='Use French', is_flag=True)
@click.argument('name')
def hello(french, name):
    if french:
        click.echo('Bonjour {}'.format(name))
    else:
        click.echo('Hello {}'.format(name))

if __name__ == '__main__':
    hello()