from pyre_extensions import TypeVarTuple, Unpack
from typing import Any, TypeVar, Tuple, overload
from . import ndarray

Ts = TypeVarTuple("Ts")
N = TypeVar("N", bound=int)

def randn(*args: Unpack[Ts]) -> ndarray[Unpack[Ts]]: ...
@overload
def randint(
    low: int, high: int = ..., size: Tuple[Unpack[Ts]] = ..., dtype=int
) -> ndarray[Unpack[Ts]]: ...
@overload
def randint(low: int, high: int = ..., size: N = ..., dtype=int) -> ndarray[N]: ...

seed: Any = ...
