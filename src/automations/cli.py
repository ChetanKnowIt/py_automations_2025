import sys

from automations.controller import run


def main() -> None:
    args = sys.argv[1:]

    print("magic number is set")
    print(
        f"Hello from automations! "
        f"we have so many ideas starting from 1 since 0 is the file name itself! -> {len(args)}"
    )

    result = run(args)

    if result is None:
        print("magic number not met! can't proceed")
        return

    print("inside controller with magic number:", args)
    print(f"Greetings from {result.python_version}")

