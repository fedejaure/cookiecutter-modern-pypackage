"""Console script for {{ cookiecutter.project_name }}."""
from typing import Annotated, Optional

import typer

from {{ cookiecutter.project_slug }} import __version__

app = typer.Typer()


def version_callback(value: bool) -> None:
    """Callback function for the --version option.

    Parameters:
        - value: The value provided for the --version option.

    Raises:
        - typer.Exit: Raises an Exit exception if the --version option is provided,
        printing the Awesome CLI version and exiting the program.
    """
    if value:
        typer.echo(f"{{ cookiecutter.project_name }}, version {__version__}")
        raise typer.Exit()


@app.command()
def main(
    version: Annotated[
        Optional[bool], typer.Option("--version", callback=version_callback, is_eager=True)
    ] = None,
) -> None:
    """Console script for {{ cookiecutter.project_name }}."""
    typer.echo("Replace this message by putting your code into {{ cookiecutter.project_slug }}.cli.main")
    typer.echo("See typer documentation at https://typer.tiangolo.com/")


if __name__ == "__main__":
    app()  # pragma: no cover
