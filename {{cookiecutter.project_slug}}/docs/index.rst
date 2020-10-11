Welcome to {{ cookiecutter.project_name }}'s documentation!
===========================================================

.. toctree::
   :maxdepth: 2

   readme
   installation
   usage
   modules
   changelog

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

{% if cookiecutter.open_source_license != 'Not open source' %}
.. toctree::
   :hidden:

   License <license>
{% endif %}
