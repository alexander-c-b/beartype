#!/usr/bin/env python3
# --------------------( LICENSE                            )--------------------
# Copyright (c) 2014-2023 Beartype authors.
# See "LICENSE" for further details.

'''
Project-wide **callable globals** (i.e., global constants describing various
well-known functions and methods).

This private submodule is *not* intended for importation by downstream callers.
'''

# ....................{ IMPORTS                            }....................
from beartype.typing import Iterator
from beartype._util.func.utilfunccodeobj import get_func_codeobj_name
from contextlib import contextmanager

# ....................{ SETS                               }....................
METHOD_NAMES_DUNDER_BINARY = frozenset((
    '__add__',
    '__and__',
    '__cmp__',
    '__divmod__',
    '__div__',
    '__eq__',
    '__floordiv__',
    '__ge__',
    '__gt__',
    '__iadd__',
    '__iand__',
    '__idiv__',
    '__ifloordiv__',
    '__ilshift__',
    '__imatmul__',
    '__imod__',
    '__imul__',
    '__ior__',
    '__ipow__',
    '__irshift__',
    '__isub__',
    '__itruediv__',
    '__ixor__',
    '__le__',
    '__lshift__',
    '__lt__',
    '__matmul__',
    '__mod__',
    '__mul__',
    '__ne__',
    '__or__',
    '__pow__',
    '__radd__',
    '__rand__',
    '__rdiv__',
    '__rfloordiv__',
    '__rlshift__',
    '__rmatmul__',
    '__rmod__',
    '__rmul__',
    '__ror__',
    '__rpow__',
    '__rrshift__',
    '__rshift__',
    '__rsub__',
    '__rtruediv__',
    '__rxor__',
    '__sub__',
    '__truediv__',
    '__xor__',
))
'''
Frozen set of the unqualified names of all **binary dunder methods** (i.e.,
methods whose names are both prefixed and suffixed by ``__``, which the active
Python interpreter implicitly calls to perform binary operations on instances
whose first operands are instances of the classes declaring those methods).
'''

# ....................{ STRINGS                            }....................
@contextmanager
def _noop_context_manager() -> Iterator[None]:
    '''
    Arbitrary :func:`contextlib.contextmanager`-based context manager defined
    solely to inspect various dunder attributes common to all such managers.
    '''

    yield


CONTEXTLIB_CONTEXTMANAGER_CODEOBJ_NAME = get_func_codeobj_name(
    _noop_context_manager)
'''
Fully-qualified name of the code object underlying the isomorphic decorator
closure created and returned by the :func:`contextlib.contextmanager` decorator.

This name enables functionality elsewhere to reliably detect when a function has
been decorated by that decorator. This is critical, as the type of *all* objects
created and returned by :func:`contextlib.contextmanager`-based context managers
is a private class of the :mod:`contextlib` module rather than the types implied
by the type hints originally annotating the returns of those context managers.
If :mod:`beartype` did *not* actively detect and intervene in this edge case,
then runtime type-checkers dynamically generated by :mod:`beartype` for those
managers would erroneously raise type-checking violations after calling those
managers and detecting a seeming type violation: e.g.,

.. code-block:: python

   >>> from beartype.typing import Iterator
   >>> from contextlib import contextmanager
   >>> @contextmanager
   ... def _noop_context_manager() -> Iterator[None]: yield
   >>> type(_noop_context_manager())
   <class 'contextlib._GeneratorContextManager'>  # <-- not an "Iterator", bro
   >>> _noop_context_manager.__qualname__
   _noop_context_manager  # <-- that looks sane... but *IS* it?
   >>> _noop_context_manager.__code__.co_qualname
   contextmanager.<locals>.helper  # <-- So. The truth is revealed at last.

As the above example demonstrates, the ``__qualname__`` dunder attribute of the
isomorphic decorator closure created and returned by the
:func:`contextlib.contextmanager` decorator publicly lies about its identity by
masquerading as the decorated generator factory function. Only the secretive
``__code__.co_qualname`` dunder attribute of that closure tells the truth.
'''
# print(f'CONTEXTLIB_CONTEXTMANAGER_CODEOBJ_NAME: {CONTEXTLIB_CONTEXTMANAGER_CODEOBJ_NAME}')


# Delete this context manager now that we no longer require it as a negligible
# safety (and possible space complexity) measure.
del _noop_context_manager
