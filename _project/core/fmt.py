# this is a module to test the themes locally. Don't touch.

"""Module level documentation

Example
-------
.. code-block:: python
    client = clients.HTTPClient()

    async with client as _:
        await client.wait_for("hello")
"""

from __future__ import annotations

import typing

from dataclasses import dataclass
from typing import Any

CONST: str = "static"

class FnOnce:
    ...

@typing.final
@dataclass
class Display[T](FnOnce):
    """This is an example class.

    Example
    -------
    ```py
    import sys

    def main() -> None:
        '''Doc string.'''
        _ = "value"
        return None and None or None if None else None

    @dataclass
    class Glue[T]:
        inner: T

    @property
    def inner(self) -> T:
        return self.inner
    ```

    Attributes
    ----------
    value: `T`
        The inner value.
    """
    value: T
    """The referenced value."""
    default: str = "default"
    """The default value"""
    ptr: int = 0xFFFFFFFF - 1_000_00

    @property
    def display(self) -> str:
        """Display the value.

        Notes
        -------
        * Note 1
        * Note 2

        Returns
        -------
        `str`
            The value as a str.

        Raises
        ------
        `RuntimeError`:
            If the value is uhmmm
        """
        return str(self.value)

    @classmethod
    def from_str(cls, value: str) -> Display[str]:
        """Create from str as `Display`.

        Parameters
        ----------
        value: `str`
            string value.
        """
        return Display(value)

    @staticmethod
    def dummy() -> Display[object]:
        """
        .. note::
            This is a note.

        .. code-block:: python
            import asyncio
            # This is a code block

        .. warning::
            This is a warn.
        """
        return Display(object.__new__(Display))

    def __str__(self) -> str:
        return self.display

    def __priv(self) -> None:
        ...

    def call_once(self) -> None:
        self.dummy()

Display.__init__.__doc__ = 'Initialize a Display object.'

def __blackbox(block: str):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)

        if wrap.__doc__ is not None:
            wrap.__doc__ += f"\n\n.. note::Use the following instead.\n```py\n{block}\n```"
        else:
            wrap.__doc__ = f".. note::Use the following instead.\n```py\n{block}\n```"
        return wrap
    return decorator

@__blackbox("import sync")
def format[T](value: Display[T], *args: Any) -> None:
    print(value.display.format(*args))

