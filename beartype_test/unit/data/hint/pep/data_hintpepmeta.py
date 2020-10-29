#!/usr/bin/env python3
# --------------------( LICENSE                           )--------------------
# Copyright 2014-2020 by Cecil Curry.
# See "LICENSE" for further details.

'''
**Beartype PEP-compliant type hint metadata data-driven testing submodule.**

This submodule declares lower-level metadata classes instantiated by the
higher-level :mod:`beartype_test.unit.data.hint.pep.data_hintpep` submodule.
'''

# ....................{ IMPORTS                           }....................

# ....................{ CLASSES ~ hint                    }....................
class PepHintMetadata(object):
    '''
    **PEP-compliant type hint metadata** (i.e., dataclass whose instance
    variables describe a PEP-compliant type hint with metadata applicable to
    various testing scenarios).

    Attributes
    ----------
    pep_sign : object
        **Unsubscripted** :mod:`typing` **attribute** (i.e., public attribute of
        the :mod:`typing` module uniquely identifying this PEP-compliant type
        hint, stripped of all subscripted arguments but *not* default type
        variables) if this hint is uniquely identified by such an attribute
        *or* ``None`` otherwise. Examples of PEP-compliant type hints *not*
        uniquely identified by such attributes include those reducing to
        standard builtins on instantiation such as:

        * :class:`typing.NamedTuple` reducing to :class:`tuple`.
        * :class:`typing.TypedDict` reducing to :class:`dict`.
    is_pep484_generic : bool
        ``True`` only if this PEP-compliant type hint is a **user-defined
        generic** (i.e., PEP-compliant type hint whose class subclasses one or
        more public :mod:`typing` pseudo-superclasses but *not* itself defined
        by the :mod:`typing` module). Defaults to ``False``.
    is_supported : bool
        ``True`` only if this PEP-compliant type hint is currently supported by
        the :func:`beartype.beartype` decorator. Defaults to ``True``.
    is_typevared : bool
        ``True`` only if this PEP-compliant type hint is parametrized by one or
        more **type variables** (i.e., :class:`typing.TypeVar` instances).
        Defaults to ``False``.
    piths_satisfied : Tuple[object]
        Tuple of zero or more arbitrary objects satisfying this hint when
        either passed as a parameter *or* returned as a value annotated by this
        hint. Defaults to the empty tuple.
    piths_unsatisfied_meta : Tuple[PepHintPithUnsatisfiedMetadata]
        Tuple of zero or more :class:`_PepHintPithUnsatisfiedMetadata`
        instances, each describing an object *not* satisfying this hint when
        either passed as a parameter *or* returned as a value annotated by this
        hint. Defaults to the empty tuple.
    type_origin : Optional[type]
        **Origin type** (i.e., non-:mod:`typing` class such that *all* objects
        satisfying this hint are instances of this class) originating this hint
        if this hint originates from a non-:mod:`typing` class *or* ``None``
        otherwise (i.e., if this hint does *not* originate from such a class).
        Defaults to ``None``.
    '''

    # ..................{ INITIALIZERS                      }..................
    def __init__(
        self,

        # Mandatory parameters.
        pep_sign: object,

        # Optional parameters.
        is_pep484_generic: bool = False,
        is_supported: bool = True,
        is_typevared: bool = False,
        piths_satisfied: tuple = (),
        piths_unsatisfied_meta: 'Tuple[PepHintPithUnsatisfiedMetadata]' = (),
        type_origin: 'Optional[type]' = None,
    ) -> None:
        assert isinstance(is_supported, bool), (
            f'{repr(is_supported)} not bool.')
        assert isinstance(is_pep484_generic, bool), (
            f'{repr(is_pep484_generic)} not bool.')
        assert isinstance(is_typevared, bool), (
            f'{repr(is_typevared)} not bool.')
        assert isinstance(piths_satisfied, tuple), (
            f'{repr(piths_satisfied)} not tuple.')
        assert isinstance(piths_unsatisfied_meta, tuple), (
            f'{repr(piths_unsatisfied_meta)} not tuple.')
        assert all(
            isinstance(pith_unsatisfied_meta, PepHintPithUnsatisfiedMetadata)
            for pith_unsatisfied_meta in piths_unsatisfied_meta
        ), (
            f'{repr(piths_unsatisfied_meta)} not tuple of '
            f'"PepHintPithUnsatisfiedMetadata" instances.')
        assert isinstance(type_origin, (type, type(None))), (
            f'{repr(type_origin)} neither class nor "None".')

        # Classify all passed parameters.
        self.pep_sign = pep_sign
        self.is_supported = is_supported
        self.is_pep484_generic = is_pep484_generic
        self.is_typevared = is_typevared
        self.piths_satisfied = piths_satisfied
        self.piths_unsatisfied_meta = piths_unsatisfied_meta
        self.type_origin = type_origin

    # ..................{ STRINGIFIERS                      }..................
    def __repr__(self) -> str:
        return '\n'.join((
            f'{self.__class__.__name__}(',
            f'    pep_sign={self.pep_sign},',
            f'    is_supported={self.is_supported},',
            f'    is_pep484_generic={self.is_pep484_generic},',
            f'    is_typevared={self.is_typevared},',
            f'    piths_satisfied={self.piths_satisfied},',
            f'    piths_unsatisfied_meta={self.piths_unsatisfied_meta},',
            f'    type_origin={self.type_origin},',
            f')',
        ))


class PepHintClassedMetadata(PepHintMetadata):
    '''
    **PEP-compliant class type hint metadata** (i.e.,
    dataclass whose instance variables describe a PEP-compliant type hint
    implemented by the :mod:`typing` module as a standard class
    indistinguishable from non-:mod:`typing` classes with metadata applicable
    to various testing scenarios).
    '''

    # ..................{ INITIALIZERS                      }..................
    def __init__(self, *args, **kwargs) -> None:

        # Coerce the unsubscripted "typing" attribute identifying this hint to
        # be "None" *BEFORE* initializing our superclass. This hint is
        # implemented by the "typing" module as a normal class whose
        # machine-readable representation is the standard class representation
        # "<class '{self.__class__.__name__}'>" rather than the non-standard
        # "typing" representation prefixed by "typing.".
        kwargs['pep_sign'] = None

        # Initialize our superclass.
        super().__init__(*args, **kwargs)

# ....................{ CLASSES ~ hint : unsatisfied      }....................
class PepHintPithUnsatisfiedMetadata(object):
    '''
    **PEP-compliant type hint unsatisfied pith metadata** (i.e., dataclass
    whose instance variables describe an object *not* satisfying a
    PEP-compliant type hint when either passed as a parameter *or* returned as
    a value annotated by that hint).

    Attributes
    ----------
    pith : object
        Arbitrary object *not* satisfying this hint when either passed as a
        parameter *or* returned as a value annotated by this hint.
    exception_str_match_regexes : Tuple[str]
        Tuple of zero or more r''-style uncompiled regular expression strings,
        each matching a substring of the exception message expected to be
        raised by wrapper functions when either passed or returning this
        ``pith``. Defaults to the empty tuple.
    exception_str_not_match_regexes : Tuple[str]
        Tuple of zero or more r''-style uncompiled regular expression strings,
        each *not* matching a substring of the exception message expected to be
        raised by wrapper functions when either passed or returning this
        ``pith``. Defaults to the empty tuple.
    '''

    # ..................{ INITIALIZERS                      }..................
    def __init__(
        self,

        # Mandatory parameters.
        pith: object,

        # Optional parameters.
        exception_str_match_regexes: 'Tuple[str]' = (),
        exception_str_not_match_regexes: 'Tuple[str]' = (),
    ) -> None:
        assert isinstance(exception_str_match_regexes, tuple), (
            f'{repr(exception_str_match_regexes)} not tuple.')
        assert isinstance(exception_str_not_match_regexes, tuple), (
            f'{repr(exception_str_not_match_regexes)} not tuple.')
        assert all(
            isinstance(exception_str_match_regex, str)
            for exception_str_match_regex in exception_str_match_regexes
        ), f'{repr(exception_str_match_regexes)} not tuple of regexes.'
        assert all(
            isinstance(exception_str_not_match_regex, str)
            for exception_str_not_match_regex in (
                exception_str_not_match_regexes)
        ), f'{repr(exception_str_not_match_regexes)} not tuple of regexes.'

        # Classify all passed parameters.
        self.pith = pith
        self.exception_str_match_regexes = exception_str_match_regexes
        self.exception_str_not_match_regexes = exception_str_not_match_regexes

    # ..................{ STRINGIFIERS                      }..................
    def __repr__(self) -> str:
        return '\n'.join((
            f'{self.__class__.__name__}(',
            f'    pith={self.pith},',
            f'    exception_str_match_regexes={self.exception_str_match_regexes},',
            f'    exception_str_not_match_regexes={self.exception_str_not_match_regexes},',
            f')',
        ))
