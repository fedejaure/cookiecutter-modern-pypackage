Tutorial
========

.. note:: Did you find any of these instructions confusing? `Edit this file`_
          and submit a pull request with your improvements!

.. _`Edit this file`: https://github.com/fedejaure/cookiecutter-modern-pypackage/blob/master/docs/tutorial.rst

To start with, you will need a `GitHub account`_ and an account on `PyPI`_. Create these before you get started on this tutorial. If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at `GitHub Help`_.

.. _`GitHub account`: https://github.com/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`GitHub Help`: https://help.github.com/


Step 1: Install Cookiecutter
----------------------------

Install cookiecutter:

.. code-block:: bash

    $ pip install cookiecutter

We'll also need poetry so `install that too`_.

.. _`install that too`: https://python-poetry.org/docs/#installation

Step 2: Generate Your Package
-----------------------------

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the cookiecutter-pypackage repo:

.. code-block:: bash

    $ cookiecutter gh:fedejaure/cookiecutter-modern-pypackage --checkout v2.3.1

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.


Step 3: Create a GitHub Repo
----------------------------

Go to your GitHub account and create a new repo named ``mypackage``, where ``mypackage`` matches the ``[project_name]`` from your answers to running cookiecutter.

You will find one folder named after the ``[project_name]``. Move into this folder, and then setup git to use your GitHub repo and upload the code:

.. code-block:: bash

    $ cd mypackage
    mypackage $ git init .
    mypackage $ git add .
    mypackage $ git commit -m "Initial skeleton."
    mypackage $ git remote add origin git@github.com:myusername/mypackage.git
    mypackage $ git push -u origin main

Where ``myusername`` and ``mypackage`` are adjusted for your username and package name.

You'll need a ssh key to push the repo. You can `Generate`_ a key or `Add`_ an existing one.

.. _`Generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`Add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

Step 4: Install Dev Requirements
--------------------------------

You should still be in the folder containing the ``pyproject.toml`` file.

Install the new project's local development requirements inside a virtual environment using poetry:

.. code-block:: bash

    $ poetry install
    $ poetry run inv install-hooks

Step 5: Set Up Codecov
----------------------

`Codecov`_ provides highly integrated tools to group, merge, archive, and compare coverage reports. 

Log into your account at `Codecov`_. If you don't have one, create one and log into it.

Click on `Add new repository`. Choose the desired one. Then follow the instructions to setup the `CODECOV_TOKEN` on the github secrets.

Install the `Codecov`_ github App.

Now your coverage reports will be generated when a new PR is created.

.. _`Codecov`: https://codecov.io/

Step 6: Set Up Read the Docs
----------------------------

`Read the Docs`_ hosts documentation for the open source community. Think of it as Continuous Documentation.

Log into your account at `Read the Docs`_ . If you don't have one, create one and log into it.

If you are not at your dashboard, choose the pull-down next to your username in the upper right, and select "My Projects". Choose the button to Import the repository and follow the directions.

Now your documentation will get rebuilt when you make documentation changes to your package.

.. _`Read the Docs`: https://readthedocs.org/

Step 7: Release on PyPI and TestPyPI
------------------------------------

The Python Package Index or `PyPI`_ is the official third-party software repository for the Python programming language. Python developers intend it to be a comprehensive catalog of all open source Python packages.

`TestPyPI`_ is a separate instance of the Python Package Index (`PyPI`_) that allows you to try out the distribution tools and process without worrying about affecting the real index.

Log into your account at `PyPI`_ and `TestPyPI`_. Go to Account Settings and generate an API tokens. 

Go to the repository settings on GitHub, and add tow secrets named `PYPI_TOKEN` and `TEST_PYPI_TOKEN` with the tokens that you just generated.

Release your package by pushing a new tag.

.. _`PyPI`: https://pypi.python.org/pypi
.. _`TestPyPI`: https://test.pypi.org/

Having problems?
----------------

Visit our `Issues`_ page and create a new Issue. Be sure to give as much information as possible.

.. _`Issues`: https://github.com/fedejaure/cookiecutter-modern-pypackage/issues
