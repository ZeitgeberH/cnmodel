from __future__ import print_function
import pdb
"""
Run unit tests for cnmodel
"""

import os, sys
import pytest

def main():
    # Make sure we look for cnmodel here first.
    path = os.path.dirname(__file__)
    sys.path.insert(0, path)


    # Allow user to audit tests with --audit flag
    import cnmodel
    if '--audit' in sys.argv:
        sys.argv.remove('--audit')
        sys.argv.append('-s') # needed for cli-based user interaction
        cnmodel.AUDIT_TESTS = True

    # generate test flags
    flags = sys.argv[1:]
    flags.append('-v')
    tb = [flag for flag in flags if flag.startswith('--tb')]
    if len(tb) == 0:
        flags.append('--tb=short')

    add_path = True
    for flag in flags:
        if os.path.isdir(flag) or os.path.isfile(flag):
            add_path = False
            break
    if add_path:
        flags.append('cnmodel/')

    # ignore the an cache
    flags.append('--ignore=cnmodel/an_model/cache/')

    # Start tests.
    print("Testing with flags: %s" % " ".join(flags))
    pdb.set_trace()
    pytest.main(flags)



if __name__ == '__main__':
    main()