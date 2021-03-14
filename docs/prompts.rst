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

package_tool
    The tool used to manage dependencies

Options
-------

The following package configuration options set up different features for your project.

package_tool
    Whether to create a project using Pipenv or using Poetry.

open_source_license
    Whether to add a license file. Options: ["MIT", "BSD", "ISC", "Apache Software License 2.0", "GNU General Public License v3", "Not open source"s]

command_line_interface
    Whether to create a console script using Click. Console script entry point will match the project_name. Options: ["Click", "No command-line interface"]