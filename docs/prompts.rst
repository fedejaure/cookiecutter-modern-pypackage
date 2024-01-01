Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

full_name
    Your full name.

email
    Your email address.

github_username
    Your GitHub username.

project_name
    The name of your new Python package project. This is used in the package name and the Github repository name, so use - insteed of spaces.

project_slug
    The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version of project_name.

project_title
    The title of your new Python project. This is used in documentation, so spaces and any characters are fine here.

project_short_description
    A 1-sentence description of what your Python package does.

version
    The starting version number of the package.

Options
-------

The following package configuration options set up different features for your project.

open_source_license
    Whether to add a license file. Options: ["MIT", "BSD", "ISC", "Apache Software License 2.0", "GNU General Public License v3", "Not open source"s]

command_line_interface
    Whether to create a console script using Typer. Console script entry point will match the project_name. Options: ["Typer", "No command-line interface"]

add_code_of_conduct
    Whether to add a Contributor Covenant Code of Conduct file.

add_contributing_file
    Whether to add a Contributing Guide file.

add_security_file
    Whether to add a Security Policy file.

add_codeowners_file
    Whether to add a CODEOWNERS file.

contact_method
    Whether to add a contact method. Used on files such of `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` and `SECURITY.md`.
