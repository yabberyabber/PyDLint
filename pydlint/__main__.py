"""A main program for Byterun."""

import argparse
import logging

from . import execfile
from . import issue

parser = argparse.ArgumentParser(
    prog="PyDLint",
    description="Run Python programs and report Code Quality Issues at runtime.",
)
parser.add_argument(
    '-m', dest='module', action='store_true',
    help="prog is a module name, not a file name.",
)
parser.add_argument(
    '-v', '--verbose', dest='verbose', action='store_true',
    help="trace the execution of the bytecode.",
)
parser.add_argument(
    '-warn', dest='warn_mode', action='store_true',
    help="Print a warning when an issue is found"
)
parser.add_argument(
    '-strict', dest='strict_mode', action='store_true',
    help="Stop execution when an issue is found"
)
parser.add_argument(
    'prog',
    help="The program to run.",
)
parser.add_argument(
    'args', nargs=argparse.REMAINDER,
    help="Arguments to pass to the program.",
)
args = parser.parse_args()

if args.module:
    run_fn = execfile.run_python_module
else:
    run_fn = execfile.run_python_file

level = logging.DEBUG if args.verbose else logging.WARNING
logging.basicConfig(level=level)

behavior = issue.STRICT if args.strict_mode else issue.WARN

argv = [args.prog] + args.args
run_fn(args.prog, argv, behavior=behavior)
