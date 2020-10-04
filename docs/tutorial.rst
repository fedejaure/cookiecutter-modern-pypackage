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

We'll also need poetry so [install that too](https://python-poetry.org/docs/#installation):

Step 2: Generate Your Package
-----------------------------

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the cookiecutter-pypackage repo:

.. code-block:: bash

    $ cookiecutter https://github.com/fedejaure/cookiecutter-modern-pypackage.git

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.


Step 3: Create a GitHub Repo
----------------------------

Go to your GitHub account and create a new repo named ``mypackage``, where ``mypackage`` matches the ``[project_slug]`` from your answers to running cookiecutter.

You will find one folder named after the ``[project_slug]``. Move into this folder, and then setup git to use your GitHub repo and upload the code:

.. code-block:: bash

    $ cd mypackage
    mypackage $ git init .
    mypackage $ git add .
    mypackage $ git commit -m "Initial skeleton."
    mypackage $ git remote add origin git@github.com:myusername/mypackage.git
    mypackage $ git push -u origin master

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
    $ poetry run inv install_hooks

Step 5: Set Up Read the Docs
----------------------------

`Read the Docs`_ hosts documentation for the open source community. Think of it as Continuous Documentation.

Log into your account at `Read the Docs`_ . If you don't have one, create one and log into it.

If you are not at your dashboard, choose the pull-down next to your username in the upper right, and select "My Projects". Choose the button to Import the repository and follow the directions.

Now your documentation will get rebuilt when you make documentation changes to your package.

.. _`Read the Docs`: https://readthedocs.org/

Step 6: Release on PyPI
-----------------------

The Python Package Index or `PyPI`_ is the official third-party software repository for the Python programming language. Python developers intend it to be a comprehensive catalog of all open source Python packages.

When you are ready, release your package the standard Python way.

See `PyPI Help`_ for more information about submitting a package.

.. _`PyPI`: https://pypi.python.org/pypi
.. _`PyPI Help`: http://peterdowns.com/posts/first-time-with-pypi.html

Having problems?
----------------

Visit our `Issues`_ page and create a new Issue. Be sure to give as much information as possible.

.. _`Issues`: https://github.com/fedejaure/cookiecutter-modern-pypackage/issues
