#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

##############################################################################
# ensymble.py - Ensymble command line tool
# Copyright 2006 Jussi Yl�nen
#
# This file is part of Ensymble developer utilities for Symbian OS(TM).
#
# Ensymble is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ensymble is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ensymble; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
##############################################################################

import sys
import os

# Import command modules.
cmddict     = {"py2sis": None, "version": None}
for cmdname in cmddict.keys():
    cmddict[cmdname] = __import__("cmd_%s" % cmdname, globals(), locals(), [])


def main():
    pgmname     = os.path.basename(sys.argv[0])

    # Parse command line parameters.
    try:
        if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
            # No command given, print help.
            commands = []
            for cmd in cmddict.keys():
                commands.append("    %-12s %s" % (cmd, cmddict[cmd].shorthelp))
            commands.sort()
            commands = "\n".join(commands)

            print (
'''
Ensymble developer utilities for Symbian OS(TM)

usage: %(pgmname)s command [command options]...

Commands:
%(commands)s

Use '%(pgmname)s command --help' to get command specific help.
''' % locals())
            return 0

        command = sys.argv[1]
        if command not in cmddict.keys():
            raise ValueError("invalid command '%s'" % command)

        if "-h" in sys.argv[2:] or "--help" in sys.argv[2:]:
            # Print command specific help.
            longhelp = cmddict[command].longhelp
            print (
'''Ensymble developer utilities for Symbian OS(TM)

usage: %(pgmname)s %(longhelp)s''' % locals())
        else:
            # Run command.
            cmddict[command].run(pgmname, sys.argv[2:])
    except Exception, e:
        return "%s: %s" % (pgmname, str(e))

    return 0

# Call main if run as stand-alone executable.
#if __name__ == '__main__' or True:
#    sys.exit(main())

# Call main regardless, to support packing with the squeeze utility.
sys.exit(main())