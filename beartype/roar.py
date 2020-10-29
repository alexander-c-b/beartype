#!/usr/bin/env python3
# --------------------( LICENSE                           )--------------------
# Copyright (c) 2014-2020 Cecil Curry.
# See "LICENSE" for further details.

'''
**Hear beartype roar** as it handles errors and warnings.

This submodule defines hierarchies of :mod:`beartype`-specific exceptions
and warnings emitted by the :func:`beartype.beartype` decorator.
'''

# ....................{ IMPORTS                           }....................
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# WARNING: To avoid polluting the public module namespace, external attributes
# should be locally imported at module scope *ONLY* under alternate private
# names (e.g., "from argparse import ArgumentParser as _ArgumentParser" rather
# than merely "from argparse import ArgumentParser").
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from abc import ABCMeta as _ABCMeta

# See the "beartype.__init__" submodule for further commentary.
__all__ = ['STAR_IMPORTS_CONSIDERED_HARMFUL']

# ....................{ SUPERCLASS                        }....................
class BeartypeException(Exception, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype exceptions.**

    Instances of subclasses of this exception are raised either:

    * At decoration time from the :func:`beartype.beartype` decorator.
    * At call time from the new callable generated by the
      :func:`beartype.beartype` decorator to wrap the original callable.
    '''

    pass

# ....................{ CAVE                              }....................
class BeartypeCaveException(BeartypeException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype cave exceptions.**

    Instances of subclasses of this exception are raised at usage time from
    various types published by the :func:`beartype.cave` submodule.
    '''

    pass

# ....................{ CAVE ~ NoneTypeOr                 }....................
class BeartypeCaveNoneTypeOrException(
    BeartypeCaveException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype cave** ``None`` **tuple factory
    exceptions.**

    Instances of subclasses of this exception are raised at usage time from
    the :func:`beartype.cave.NoneTypeOr` tuple factory.
    '''

    pass


class BeartypeCaveNoneTypeOrKeyException(BeartypeCaveNoneTypeOrException):
    '''
    **Beartype cave** ``None`` **tuple factory key exception.**

    This exception is raised when indexing the :func:`beartype.cave.NoneTypeOr`
    dictionary with an invalid key, including:

    * The empty tuple.
    * Arbitrary objects that are neither:

      * **Types** (i.e., :class:`beartype.cave.ClassType` instances).
      * **Tuples of types** (i.e., tuples whose items are all
        :class:`beartype.cave.ClassType` instances).
    '''

    pass


class BeartypeCaveNoneTypeOrMutabilityException(
    BeartypeCaveNoneTypeOrException):
    '''
    **Beartype cave** ``None`` **tuple factory mutability exception.**

    This exception is raised when attempting to explicitly set a key on the
    :func:`beartype.cave.NoneTypeOr` dictionary.
    '''

    pass

# ....................{ DECORATOR                         }....................
class BeartypeDecorException(BeartypeException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype decorator exceptions.**

    Instances of subclasses of this exception are raised at decoration time
    from the :func:`beartype.beartype` decorator.
    '''

    pass

# ....................{ DECORATOR ~ wrapp[ee|er]          }....................
class BeartypeDecorWrappeeException(BeartypeDecorException):
    '''
    **Beartype decorator wrappee exception.**

    This exception is raised at decoration time from the
    :func:`beartype.beartype` decorator when passed a **wrappee** (i.e., object
    to be decorated by this decorator) of invalid type.
    '''

    pass


class BeartypeDecorWrapperException(BeartypeDecorException):
    '''
    **Beartype decorator parse exception.**

    This exception is raised at decoration time from the
    :func:`beartype.beartype` decorator on accidentally generating an **invalid
    wrapper** (i.e., syntactically invalid new callable to wrap the original
    callable).
    '''

    pass

# ....................{ DECORATOR ~ hint                  }....................
class BeartypeDecorHintException(BeartypeDecorException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype decorator type hint exceptions.**

    Instances of subclasses of this exception are raised at decoration time
    from the :func:`beartype.beartype` decorator on receiving a callable
    type-hinted with one or more **invalid annotations** (i.e., annotations
    that are neither PEP-compliant nor PEP-compliant type hints supported by
    that decorator).
    '''

    pass

# ....................{ DECORATOR ~ hint : value          }....................
class BeartypeDecorHintNonPepException(BeartypeDecorHintException):
    '''
    **Beartype decorator PEP-noncompliant type hint value exception.**

    This exception is raised at decoration time from the
    :func:`beartype.beartype` decorator on receiving a callable type-hinted
    with one or more **PEP-noncompliant annotations** (i.e., annotations that
    fail to comply with :mod:`beartype`-specific semantics, including tuple
    unions and fully-qualified forward references) in a semantic context
    expecting PEP-noncompliant annotations.

    Tuple unions, for example, are required to contain *only* PEP-noncompliant
    annotations. This exception is thus raised for callables type-hinted with
    tuples containing one or more PEP-compliant items (e.g., instances or
    classes declared by the stdlib :mod:`typing` module) *or* arbitrary objects
    (e.g., dictionaries, lists, numbers, sets).
    '''

    pass

# ....................{ DECORATOR ~ hint : pep            }....................
class BeartypeDecorHintPepException(
    BeartypeDecorHintException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype decorator PEP-compliant type hint
    value exceptions.**

    Instances of subclasses of this exception are raised at decoration time
    from the :func:`beartype.beartype` decorator on receiving a callable
    annotated with one or more PEP-compliant type hints either violating an
    annotation-centric PEP (e.g., `PEP 484`_) *or* this decorator's
    implementation of such a PEP.

    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484
    '''

    pass


class BeartypeDecorHintPepUnsupportedException(
    BeartypeDecorHintPepException):
    '''
    **Beartype decorator unsupported PEP-compliant type hint exception.**

    Instances of subclasses of this exception are raised at decoration time
    from the :func:`beartype.beartype` decorator on receiving a callable
    annotated with one or more PEP-compliant type hints (e.g., instances or
    classes declared by the stdlib :mod:`typing` module) currently unsupported
    by this decorator.
    '''

    pass

# ....................{ DECORATOR ~ hint : pep : proposal }....................
class BeartypeDecorHintPep484Exception(BeartypeDecorHintPepException):
    '''
    **Beartype decorator** `PEP 484`_**-compliant type hint value exception.**

    This exception is raised at decoration time from the
    :func:`beartype.beartype` decorator on receiving a callable annotated with
    one or more PEP-compliant type hints either violating `PEP 484`_ *or* this
    decorator's implementation of `PEP 484`_.

    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484
    '''

    pass

# ....................{ DECORATOR ~ param                 }....................
class BeartypeDecorParamException(BeartypeDecorException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype decorator parameter exceptions.**

    Instances of subclasses of this exception are raised at decoration time
    from the :func:`beartype.beartype` decorator on receiving a callable
    declaring invalid parameters.
    '''

    pass


class BeartypeDecorParamNameException(BeartypeDecorParamException):
    '''
    **Beartype decorator hinted tuple item invalid exception.**

    This exception is raised at decoration time from the
    :func:`beartype.beartype` decorator on receiving a callable declaring
    parameters with invalid names.
    '''

    pass

# ....................{ DECORATOR ~ pep                   }....................
class BeartypeDecorPepException(BeartypeDecorException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype decorator Python Enhancement Proposal
    (PEP) exceptions.**

    Instances of subclasses of this exception are raised at decoration time
    from the :func:`beartype.beartype` decorator on receiving a callable
    violating a specific PEP.
    '''

    pass


class BeartypeDecorHintPep563Exception(BeartypeDecorPepException):
    '''
    **Beartype decorator** `PEP 563`_ **evaluation exception.**

    This exception is raised at decoration time from the
    :func:`beartype.beartype` decorator on failing to dynamically evaluate a
    postponed annotation of the decorated callable when `PEP 563`_ is active
    for that callable.

    .. _PEP 563:
       https://www.python.org/dev/peps/pep-0563
    '''

    pass

# ....................{ CALL                              }....................
class BeartypeCallException(BeartypeException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartyped callable exceptions.**

    Instances of subclasses of this exception are raised from the **wrapper
    function** (i.e., generated by the :func:`beartype.beartype` decorator to
    wrap the callable decorated by that decorator).
    '''

    pass

# ....................{ CALL ~ type                       }....................
class BeartypeCallCheckException(BeartypeCallException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartyped callable type exceptions.**

    Instances of subclasses of this exception are raised from wrapper functions
    generated by the :func:`beartype.beartype` decorator when either passed a
    parameter or returning an object whose value is of **unexpected type**
    (i.e., violating a type hint annotated for that parameter or return value).
    '''

    pass


class BeartypeCallCheckUnavailableTypeException(BeartypeCallCheckException):
    '''
    **Beartyped callable unavailable type exceptions.**

    This exception is raised from the :class:`beartype.cave.UnavailableType`
    class when passed to either the :func:`isinstance` or :func:`issubclass`
    builtin functions, typically due to a type defined by the
    :class:`beartype.cave` submodule being conditionally unavailable under the
    active Python interpreter.
    '''

    pass

# ....................{ CALL ~ type : pep                 }....................
class BeartypeCallCheckPepException(
    BeartypeCallCheckException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartyped callable PEP-compliant type
    exceptions.**

    Instances of subclasses of this exception are raised from wrapper functions
    generated by the :func:`beartype.beartype` decorator when either passed a
    parameter or returning an object whose value is of **unexpected
    PEP-compliant type** (i.e., violating a PEP-compliant type hint annotated
    for that parameter or return value).
    '''

    pass


class BeartypeCallCheckPepParamException(BeartypeCallCheckPepException):
    '''
    **Beartyped callable parameter PEP-compliant type exception.**

    This exception is raised from wrapper functions generated by the
    :func:`beartype.beartype` decorator when passed a parameter whose value is
    of unexpected PEP-compliant type.
    '''

    pass


class BeartypeCallCheckPepReturnException(BeartypeCallCheckPepException):
    '''
    **Beartyped callable return PEP-compliant type exception.**

    This exception is raised from wrapper functions generated by the
    :func:`beartype.beartype` decorator when returning an object whose value is
    of unexpected PEP-compliant type.
    '''

    pass

# ....................{ CALL ~ type : nonpep              }....................
class BeartypeCallCheckNonPepException(
    BeartypeCallCheckException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartyped callable PEP-noncompliant type
    exceptions.**

    Instances of subclasses of this exception are raised from wrapper functions
    generated by the :func:`beartype.beartype` decorator when either passed a
    parameter or returning an object whose value is of **unexpected
    PEP-noncompliant type** (i.e., violating a PEP-noncompliant type hint
    annotated for that parameter or return value).
    '''

    pass


class BeartypeCallCheckNonPepParamException(BeartypeCallCheckNonPepException):
    '''
    **Beartyped callable parameter PEP-noncompliant type exception.**

    This exception is raised from wrapper functions generated by the
    :func:`beartype.beartype` decorator when passed a parameter whose value is
    of unexpected PEP-noncompliant type.
    '''

    pass


class BeartypeCallCheckNonPepReturnException(BeartypeCallCheckNonPepException):
    '''
    **Beartyped callable return PEP-noncompliant type exception.**

    This exception is raised from wrapper functions generated by the
    :func:`beartype.beartype` decorator when returning an object whose value is
    of unexpected PEP-noncompliant type.
    '''

    pass

# ....................{ WARNINGS                          }....................
class BeartypeWarning(UserWarning, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype warnings.**

    Instances of subclasses of this warning are emitted either:

    * At decoration time from the :func:`beartype.beartype` decorator.
    * At call time from the new callable generated by the
      :func:`beartype.beartype` decorator to wrap the original callable.
    '''

    pass

# ....................{ PRIVATE ~ decorator               }....................
class _BeartypeDecorBeartypistryException(BeartypeDecorException):
    '''
    **Beartype decorator beartypistry exception.**

    This exception is raised at decoration time from the
    :func:`beartype.beartype` decorator when erroneously accessing the
    **beartypistry** (i.e., :class:`beartype._decor._typistry.bear_typistry`
    singleton).

    This private exception denotes a critical internal issue and should thus
    *never* be raised -- let alone exposed to end users.
    '''

    pass

# ....................{ PRIVATE ~ call                    }....................
class _BeartypeCallBeartypistryException(BeartypeCallException):
    '''
    **Beartyped callable beartypistry exception.**

    This exception is raised from wrapper functions generated by the
    :func:`beartype.beartype` decorator when erroneously accessing the
    **beartypistry** (i.e., :class:`beartype._decor._typistry.bear_typistry`
    singleton).

    This private exception denotes a critical internal issue and should thus
    *never* be raised -- let alone exposed to end users.
    '''

    pass

# ....................{ PRIVATE ~ util                    }....................
class _BeartypeUtilException(BeartypeException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype utility exceptions.**

    Instances of subclasses of this exception are raised by *most* (but *not*
    all) private submodules of the private :mod:`beartype._util` subpackage.
    These exceptions denote critical internal issues and should thus *never* be
    raised -- let alone allowed to percolate up the call stack to end users.
    '''

    pass

# ....................{ PRIVATE ~ util : raise            }....................
class _BeartypeUtilRaisePepException(_BeartypeUtilException):
    '''
    **Beartype human-readable exception raiser exception.**

    This exception is raised by the
    :func:`beartype._util.utilhinttest.pep.error.peperror.raise_pep_call_exception`
    (which raises human-readable exceptions from wrapper functions when a
    passed parameter or returned value fails a type check) when an unexpected
    failure occurs.

    This exception denotes a critical internal issue and should thus *never* be
    raised -- let alone allowed to percolate up the call stack to end users.
    '''

    pass


class _BeartypeUtilRaisePepDesynchronizationException(
    _BeartypeUtilRaisePepException):
    '''
    **Beartype human-readable exception raiser desynchronization exception.**

    This exception is raised by the
    :func:`beartype._util.utilhinttest.pep.error.peperror.raise_pep_call_exception`
    (which raises human-readable exceptions from wrapper functions when a
    passed parameter or returned value referred to as the "pith" for brevity
    fails a type check) when this pith actually appears to satisfy this type
    check, implying either:

    * The parent wrapper function generated by the :mod:`beartype.beartype`
      decorator type-checking this pith triggered a false negative by
      erroneously misdetecting this pith as failing this type check.
    * The
      :func:`beartype._util.utilhinttest.pep.error.peperror.raise_pep_call_exception`
      function re-type-checking this pith triggered a false positive by
      erroneously misdetecting this pith as satisfying this type check when in
      fact this pith fails to do so.

    This exception denotes a critical internal issue and should thus *never* be
    raised -- let alone allowed to percolate up the call stack to end users.
    '''

    pass
# ....................{ PRIVATE ~ util : cache              }..................
class _BeartypeUtilCachedException(_BeartypeUtilException, metaclass=_ABCMeta):
    '''
    Abstract base class of all **beartype caching utility exceptions.**

    Instances of subclasses of this exception are raised by private submodules
    of the private :mod:`beartype._util.cache` subpackage. These exceptions
    denote critical internal issues and should thus *never* be raised -- let
    alone allowed to percolate up the call stack to end users.
    '''

    pass


class _BeartypeUtilCachedCallableException(_BeartypeUtilCachedException):
    '''
    **Beartype memoization exception.**

    This exception is raised by the
    :func:`beartype._util.utilcache.utilcachecall.callable_cached` decorator
    when the signature of the callable being decorated is unsupported.

    This exception denotes a critical internal issue and should thus *never* be
    raised -- let alone allowed to percolate up the call stack to end users.
    '''

    pass


class _BeartypeUtilCachedFixedListException(_BeartypeUtilCachedException):
    '''
    **Beartype decorator fixed list exception.**

    This exception is raised at decoration time from the
    :func:`beartype.beartype` decorator when an internal callable erroneously
    mutates a **fixed list** (i.e., list constrained to a fixed length defined
    at instantiation time), usually by attempting to modify the length of that
    list.

    This exception denotes a critical internal issue and should thus *never* be
    raised -- let alone allowed to percolate up the call stack to end users.
    '''

    pass


class _BeartypeUtilCachedObjectTypedException(_BeartypeUtilCachedException):
    '''
    **Beartype decorator typed object exception.**

    This exception is raised at decoration time from the
    :func:`beartype.beartype` decorator when an internal callable erroneously
    acquires a **pooled typed object** (i.e., object internally cached to a
    pool of all objects of that type).

    This exception denotes a critical internal issue and should thus *never* be
    raised -- let alone allowed to percolate up the call stack to end users.
    '''

    pass
