import sys

if sys.version_info >= (3, 5):
    from typing import Any, Callable, Generic, Optional, TypeVar
    from twisted.python.failure import Failure

    _T = TypeVar("_T")
    _T_co = TypeVar("_T_co", covariant=True)
    _F = TypeVar("_F", bound=Callable[..., Any])
    def setup() -> None: ...
    def run_in_reactor(
        function: Callable[..., _T]
    ) -> Callable[..., EventualResult[_T]]: ...
    class EventualResult(Generic[_T_co]):
        def cancel(self) -> None: ...
        def wait(self, timeout: float) -> _T_co: ...
        def stash(self) -> int: ...
        def original_failure(self) -> Optional[Failure]: ...
    class TimeoutError(Exception): ...
    def retrieve_result(result_id: int) -> EventualResult[object]: ...
    def no_setup() -> None: ...
    def wait_for(timeout: float) -> Callable[[_F], _F]: ...
    class ReactorStopped(Exception): ...
    __version__: str
