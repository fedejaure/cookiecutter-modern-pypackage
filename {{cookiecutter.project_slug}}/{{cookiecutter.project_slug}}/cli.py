"""Console script for {{cookiecutter.project_slug}}."""
import click

from {{ cookiecutter.project_slug }} import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> int:
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo(
        "Replace this message by putting your code into "
        "{{cookiecutter.project_slug}}.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
