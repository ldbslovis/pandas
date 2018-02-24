"""Base test suite for extension arrays.

These tests are intended for third-party libraries to subclass to validate
that their extension arrays and dtypes satisfy the interface. Moving or
renaming the tests should not be done lightly.

Libraries are expected to implement a few pytest fixtures to provide data
for the tests. The fixtures may be located in either

* The same module as your test class.
* A ``conftest.py`` in the same directory as your test class.

The full list of fixtures may be found in the ``conftest.py`` next to this
file.

.. code-block:: python

   import pytest
   from pandas.tests.extension.base import BaseDtypeTests


   @pytest.fixture
   def dtype():
       return MyDtype()


   class TestMyDtype(BaseDtypeTests):
       pass


Your class ``TestDtype`` will inherit all the tests defined on
``BaseDtypeTests``. pytest's fixture discover will supply your ``dtype``
wherever the test requires it. You're free to implement additional tests.
"""
from .casting import BaseCastingTests  # noqa
from .constructors import BaseConstructorsTests  # noqa
from .dtype import BaseDtypeTests  # noqa
from .getitem import BaseGetitemTests  # noqa
from .interface import BaseInterfaceTests  # noqa
from .methods import BaseMethodsTests  # noqa
from .missing import BaseMissingTests  # noqa
from .reshaping import BaseReshapingTests  # noqa