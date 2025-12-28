from automations.domain import RuntimeInfo, is_magic_number_met
from automations.system import get_python_sys_version


def run(args: list[str]) -> RuntimeInfo | None:
    if not is_magic_number_met(len(args)):
        return None

    return RuntimeInfo(
        python_version=get_python_sys_version()
    )

