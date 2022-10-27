import unittest
from types import TracebackType
from typing import Any

from humanfriendly.compat import StringIO

def configure_logging(log_level=...) -> None: ...
def make_dirs(pathname) -> None: ...
def retry(func, timeout: int = ..., exc_type=...): ...
def run_cli(entry_point, *arguments, **options): ...
def skip_on_raise(*exc_types): ...
def touch(filename) -> None: ...

class CallableTimedOut(Exception): ...

class ContextManager:
    def __enter__(self): ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None = ...,
        exc_value: BaseException | None = ...,
        traceback: TracebackType | None = ...,
    ) -> None: ...

class PatchedAttribute(ContextManager):
    object_to_patch: Any
    attribute_to_patch: Any
    patched_value: Any
    original_value: Any
    def __init__(self, obj, name, value) -> None: ...
    def __enter__(self): ...

class PatchedItem(ContextManager):
    object_to_patch: Any
    item_to_patch: Any
    patched_value: Any
    original_value: Any
    def __init__(self, obj, item, value) -> None: ...
    def __enter__(self): ...

class TemporaryDirectory(ContextManager):
    mkdtemp_options: Any
    temporary_directory: Any
    def __init__(self, **options) -> None: ...
    def __enter__(self): ...

class MockedHomeDirectory(PatchedItem, TemporaryDirectory):
    def __init__(self) -> None: ...
    patched_value: Any
    def __enter__(self): ...

class CustomSearchPath(PatchedItem, TemporaryDirectory):
    isolated_search_path: Any
    def __init__(self, isolated: bool = ...) -> None: ...
    patched_value: Any
    def __enter__(self): ...
    @property
    def current_search_path(self): ...

class MockedProgram(CustomSearchPath):
    program_name: Any
    program_returncode: Any
    program_script: Any
    program_signal_file: Any
    def __init__(self, name, returncode: int = ..., script: Any | None = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args, **kw): ...

class CaptureOutput(ContextManager):
    stdin: Any
    stdout: Any
    stderr: Any
    patched_attributes: Any
    def __init__(self, merged: bool = ..., input: str = ..., enabled: bool = ...) -> None: ...
    def __enter__(self): ...
    def get_lines(self): ...
    def get_text(self): ...
    def getvalue(self): ...

class CaptureBuffer(StringIO):
    def get_lines(self): ...
    def get_text(self): ...

class TestCase(unittest.TestCase):
    def __init__(self, *args, **kw) -> None: ...
    def setUp(self, log_level=...) -> None: ...
