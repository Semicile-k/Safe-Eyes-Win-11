#!/usr/bin/env python3
# Safe Eyes is a utility to remind you to take break frequently
# to protect your eyes from eye strain.

import signal
import sys
import typing

from safeeyes import translations
from safeeyes.safeeyes import SafeEyes

try:
    import gi

    gi.require_version("GLib", "2.0")
    from gi.repository import GLib
except ImportError:
    GLib = None

safe_eyes: typing.Optional[SafeEyes] = None


def main() -> None:
    """Start the Safe Eyes."""
    global safe_eyes

    # Handle Ctrl + C only if GLib exists
    if GLib is not None:
        GLib.unix_signal_add(
            GLib.PRIORITY_DEFAULT,
            signal.SIGINT,
            sigint_caught
        )

    system_locale = translations.setup()

    safe_eyes = SafeEyes(system_locale)
    safe_eyes.run(sys.argv)


def sigint_caught() -> bool:
    global safe_eyes

    if safe_eyes is not None and GLib is not None:
        GLib.idle_add(lambda: safe_eyes.quit())
    else:
        sys.exit(0)

    return GLib.SOURCE_REMOVE if GLib is not None else False


if __name__ == "__main__":
    main()