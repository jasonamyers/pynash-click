import logging

import click

from logger import logger

def abort_if_false(ctx, param, value):
    """Aborts a command that requires confirmation if the user does not
    confirm

    :param ctx: An instance of the command context
    :type ctx: object
    :param param: An instance of a command param for which confirmation is \
    required.
    :type param: object
    :param value: Either Y or N
    :type value: string
    """
    if not value:
        logger.debug('Not confirmed')
        ctx.abort()
    logger.debug('Confirmed')

@click.group()
@click.option('--debug', default=False, help='Show detailed logging',
              is_flag=True)
@click.pass_context
def cli(ctx, debug):
    """Sets up the base command options and group
    """
    if debug:
        logger.setLevel(logging.DEBUG)


@cli.group('repository', short_help='used to manipulation repositories')
@click.pass_context
def repository(ctx):
    """Establishes the repository command group.
    """

@repository.command('create', short_help='used to create repositories')
@click.argument('name')
@click.option('--package_name', default='', help='The name of the package in '
              'the repo', required=False)
@click.option('--git_url', default='', envvar='GIT_URL',
              help='The git url', required=False)
@click.option('--is_cloned', default=False, help='Flag the repo as a clone',
              is_flag=True)
@click.option('--base_url', default='', help='The PULP url', required=False)
@click.pass_context
def repository_create(ctx, name, package_name, git_url, is_cloned, base_url):
    """Create subcommand for the repository group
    """
    logger.debug('Creating repository: %s', name)
    if name == 'error':
        logger.error('Bad things happened')
        click.echo(click.style('Error', fg='red'))
        ctx.abort()
    logger.debug('Created repository: %s', name)
    click.echo(click.style('Repository created', fg='green'))

@repository.command('delete', short_help='used to delete repositories')
@click.argument('name')
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to delete the repo?',
              help='Answer Confirmation')
@click.pass_context
def repository_delete(ctx, name):
    """Delete subcommand for the repository group
    """
    logger.debug('Deleting repository: %s', name)
    logger.debug('Deleted repository: %s', name)
    click.echo(click.style('Repository deleted', fg='green'))

@cli.group('composite', short_help='used to manipulation composites')
@click.pass_context
def composite(ctx):
    """ Establishes the composite command group
    """

@composite.command('create', short_help='used to create composites')
@click.argument('name')
@click.option('--repo', '-r', multiple=True, help='A repo to include in the '
              'composite')
@click.option('--base', '-b', is_flag=True, help='Mark this composite as a '
              'base', default=False)
@click.pass_context
def composite_create(ctx, name, repo, base):
    """Create subcommand for the composite group
    """
    logger.debug('Creating composite: %s', name)
    if name == 'error':
        logger.error('Bad things')

        click.echo(click.style('Error', fg='red'))
        ctx.abort()

    logger.debug('Created composite: %s', name)
    click.echo(click.style('Composite created', fg='green'))

@composite.command('delete', short_help='used to delete composites')
@click.argument('name')
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to delete the composite?',
              help='Answer Confirmation')
@click.pass_context
def composite_delete(ctx, name):
    """Delete subcommand for the composite group
    """
    logger.debug('Deleting composite: %s', name)
    logger.debug('Deleted composite: %s', name)
    click.echo(click.style('Composite deleted', fg='green'))


if __name__ == '__main__':
    cli(obj={})