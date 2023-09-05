"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Cookiecutter Testing."""


if __name__ == "__main__":
    main(prog_name="cookiecutter-testing")  # pragma: no cover
