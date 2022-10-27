from typing import TextIO

__all__ = ["getpass", "getuser", "GetPassWarning"]

def getpass(prompt: str = ..., stream: TextIO | None = ...) -> str: ...
def getuser() -> str: ...

class GetPassWarning(UserWarning): ...
