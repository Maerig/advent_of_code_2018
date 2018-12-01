import sys


def show_progress(p):
    sys.stdout.write(f"\rProgress: {100 * p:.0f}%")
    sys.stdout.flush()
