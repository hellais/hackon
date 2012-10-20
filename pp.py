# -*- encoding: utf-8 -*-
#
# Project parser
# **************
#
# :authors: Arturo "hellais" Filastò <art@fuffa.org>
# :licence: see LICENSE

"""
I take as input a hackon project descriptor and to stuff with it.
"""

from __future__ import print_function, with_statement
import json
import sys
def load_from_descriptor(descriptor_file):
    file_name = descriptor_file.split('/')[-1]
    shortname = '.'.join(file_name.split('.')[:-1])
    with open(descriptor_file) as fp:
        descriptor = json.load(fp)
    return shortname, descriptor

def list_project(descriptor_file):
    shortname, descriptor = load_from_descriptor(descriptor_file)
    print("* %s (%s)" % (shortname, descriptor['name']))
    print("  type: %s" % descriptor['type'])
    print("  homepage: %s" % descriptor['homepage'])
    #print("  bugs: %s" % descriptor['bug_tracker'])

def process_dependencies(fp, descriptor):
    print("Processing deps %s" % descriptor)
    deps = descriptor['dependencies']

    fp.write("DEBIAN_DEPENDENCIES=")
    if 'debian' in deps:
        debian_dependencies = " ".join(deps['debian'])
        fp.write("(%s)" % debian_dependencies)
    fp.write("\n")

    fp.write("ARCH_DEPENDENCIES=")
    arch_dependencies = ""
    if 'arch' in deps:
        arch_dependencies = " ".join(deps['arch'])
        fp.write("(%s)" % arch_dependencies)
    fp.write("\n")


def init_project(descriptor_file, out_file):
    shortname, descriptor = load_from_descriptor(descriptor_file)
    with open(out_file, "w+") as fp:
        fp.write('SHORTNAME="%s"\n' % shortname)
        fp.write('NAME="%s"\n' % descriptor['name'])
        fp.write('TYPE="%s"\n' % descriptor['type'])
        fp.write('HOMEPAGE="%s"\n' % descriptor['homepage'])
        fp.write('GITREPO="%s"\n' % descriptor['git_repo'])
        fp.write('HACKONPAGE="%s"\n' % descriptor['hackon_page'])
        fp.write('BUGTRACKER="%s"\n' % descriptor['bug_tracker'])

        if 'dependencies' in descriptor:
            process_dependencies(fp, descriptor)

if sys.argv[1] == "init":
    init_project(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "list":
    list_project(sys.argv[2])
