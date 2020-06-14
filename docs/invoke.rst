Invoke
======

The generated project is ready to run some useful tasks like formatting, linting, testing.

To do this we use pyinvoke_ to wrap up the required commands.

.. _pyinvoke: http://www.pyinvoke.org/

Execute `inv[oke] --list` to see the list of available commands.

.. code-block:: bash

   $ poerty shell
   $ inv[oke] --list
   Available tasks:

     clean           Run all clean sub-tasks.
     clean-build     Clean up files from package building.
     clean-docs      Clean up files from documentation builds.
     clean-python    Clean up python file artifacts.
     clean-tests     Clean up files from testing.
     coverage        Create coverage report.
     docs            Build documentation.
     flake8          Run flake8.
     format          Format code.
     hooks           Run pre-commit hooks.
     install-hooks   Install pre-commit hooks.
     lint            Run all linting.
     mypy            Run mypy.
     safety          Run safety.
     tests           Run tests.
     version         Bump version.
