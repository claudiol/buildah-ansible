#!/usr/bin/python

#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# (c) 2012, Red Hat, Inc
# Based on yum module written by Seth Vidal <skvidal at fedoraproject.org>
# (c) 2014, Epic Games, Inc.
# Written by Lester Claudio <claudiol at redhat.com>
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import platform
import tempfile
import shutil



ANSIBLE_METADATA = {'status': ['stableinterface'],
                    'supported_by': 'core',
                    'version': '1.0'}

DOCUMENTATION = '''
---
module: buildah_rmi
version_added: historical
short_description:    buildah rmi - removes one or more images from local storage
description:
     -    buildah rmi - removes one or more images from local storage

options:

# informational: requirements for nodes
requirements: [ buildah ]
author:
    - "Red Hat Consulting (NAPS)"
    - "Lester Claudio"
'''

EXAMPLES = '''
  - name: BUILDAH | Test output of "buildah rmi <image_name>" command
    buildah_rmi:
      name: CONTAINER-ID-OR-NAME
    register: result

  - debug: var=result.stdout_lines

  - name: BUILDAH | Test output of "buildah rmi --all" command
    buildah_rmi:
      all: yes
    register: result

  - debug: var=result.stdout_lines


'''
def buildah_rmi ( module, name, all, force, prune ):

    if module.get_bin_path('buildah'):
        buildah_bin = module.get_bin_path('buildah')
        buildah_basecmd = [buildah_bin, 'rm']

    if name:
        r_cmd = [name]
        buildah_basecmd.extend(r_cmd)

    if all:
        r_cmd = ['--all']
        buildah_basecmd.extend(r_cmd)

    if force:
        r_cmd = ['--force']
        buildah_basecmd.extend(r_cmd)

    if prune:
        r_cmd = ['--prune']
        buildah_basecmd.extend(r_cmd)

    return module.run_command(buildah_basecmd) 


def main():

    module = AnsibleModule(
        argument_spec = dict(
            name=dict(required=False),
            all=dict(required=False, default="no", type="bool"),
            prune=dict(required=False, default="no", type="bool"),
            force=dict(required=False, default="no", type="bool"),
        ),
        supports_check_mode = True
    )

    params = module.params

    name = params.get('name', '')
    all = params.get('all', '')
    force = params.get('force', '')
    prune = params.get('prune', '')

    rc, out, err =  buildah_rmi ( module, name, all, force, prune )

    if rc == 0:
        module.exit_json(changed=True, rc=rc, stdout=out, err = err )
    else:
        module.fail_json(msg = err )

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()

