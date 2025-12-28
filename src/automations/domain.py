from dataclasses import dataclass

MAGIC_NUMBER = 3


def is_magic_number_met(arg_count: int) -> bool:
    return arg_count == MAGIC_NUMBER

@dataclass(frozen=True)
class RuntimeInfo:
    python_version: str

