import click

@click.command()
@click.option('--lang', default='english', help='A language to use (Engish, French)', multiple=True)
@click.argument('name')
def hello(name, lang):
    supported_langs = ['french', 'english']
    unsupported = [x for x in lang if x not in supported_langs]
    if unsupported:
        raise click.BadParameter('We don\'t support: {}'.format(', '.join(unsupported)))
    if 'french' in lang:
        click.echo('Bonjour {}'.format(name))
    if 'english' in lang:
        click.echo('Hello {}'.format(name))

if __name__ == '__main__':
    hello()