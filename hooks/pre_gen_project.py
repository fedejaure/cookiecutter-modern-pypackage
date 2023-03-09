"""Script that run before the project is generated."""
import re
import sys

NAME_REGEX = r"^[a-zA-Z][\-a-zA-Z0-9]+$"
SLUG_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


def validate_value(value: str, regex: str, fail_msg: str) -> None:
    """Validate value format."""
    if not re.match(regex, value):
        print(fail_msg)
        sys.exit(1)


if __name__ == "__main__":
    validate_value(
        "{{ cookiecutter.project_name }}",
        NAME_REGEX,
        (
            "ERROR: The project name {value} is not a valid Github repository name. "
            "Please do not use a _ and use - instead"
        ),
    )

    validate_value(
        "{{ cookiecutter.project_slug }}",
        SLUG_REGEX,
        (
            "ERROR: The project slug {value} is not a valid Python module name. "
            "Please do not use a - and use _ instead"
        ),
    )
