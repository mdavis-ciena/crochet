Crochet: Use Twisted anywhere!
==============================

Crochet is an MIT-licensed library that makes it easier to use Twisted from
regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with Twisted more
  cleanly from their threaded parts. For example, this can be useful when using
  Twisted as a `WSGI container`_.

.. _WSGI container: https://twistedmatrix.com/documents/current/web/howto/web-in-60/wsgi.html

Crochet is maintained by Itamar Turner-Trauring.

  **Note:** Crochet development is pretty slow these days because mostly it **Just Works**. PyPI shows about 30,000 downloads a month, so existing users seem happy: https://pypistats.org/packages/crochet

You can install Crochet by running::

  $ pip install crochet

Downloads are available on `PyPI`_.

Documentation can be found on `Read The Docs`_.

Bugs and feature requests should be filed at the project `Github page`_.

.. _Read the Docs: https://crochet.readthedocs.org/
.. _Github page: https://github.com/itamarst/crochet/
.. _PyPI: https://pypi.python.org/pypi/crochet


API and features
================

.. image:: https://travis-ci.org/itamarst/crochet.png?branch=master
           :target: http://travis-ci.org/itamarst/crochet
           :alt: Build Status

Crochet supports Python 2.7, 3.5, 3.6, 3.7, and 3.8 as well as PyPy and PyPy3.

Crochet provides the following basic APIs:

* Allow blocking code to call into Twisted and block until results are available
  or a timeout is hit, using the ``crochet.wait_for`` decorator.
* A lower-level API (``crochet.run_in_reactor``) allows blocking code to run
  code "in the background" in the Twisted thread, with the ability to repeatedly
  check if it's done.

Crochet will do the following on your behalf in order to enable these APIs:

* Transparently start Twisted's reactor in a thread it manages.
* Shut down the reactor automatically when the process' main thread finishes.
* Hook up Twisted's log system to the Python standard library ``logging``
  framework. Unlike Twisted's built-in ``logging`` bridge, this includes
  support for blocking `Handler` instances.

Static Type Checking
--------------------

Crochet comes with type hints for Python 3.5+.  However, due to current
limitations in ``Callable`` generic construction (see
`PEP 612 — Parameter Specification Variables`_), the arguments of a call to
a ``@run_in_reactor``-decorated function or method cannot be checked without
giving type checkers some special help.  Crochet ships with a plugin which
fills this role when the ``mypy`` static type checker is used.  It resides in
the ``crochet.mypy`` package and must be configured as described in
`Configuring mypy to use plugins`_.  For example, in a ``mypy.ini``
configuration file::

    [mypy]
    plugins = crochet.mypy

.. _PEP 612 — Parameter Specification Variables: https://www.python.org/dev/peps/pep-0612/
.. _Configuring mypy to use plugins: https://mypy.readthedocs.io/en/latest/extending_mypy.html#configuring-mypy-to-use-plugins
