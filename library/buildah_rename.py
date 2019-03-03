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
module: buildah_rename
version_added: historical
short_description: Mount a working container's root filesystem
description:
     - Mount a working container's root filesystem.
options:

# informational: requirements for nodes
requirements: [ buildah ]
author:
    - "Red Hat Consulting (NAPS)"
    - "Lester Claudio"
'''

EXAMPLES = '''
  - name: BUILDAH | Test output of "buildah add <image_name>" command
    buildah_rename:
      container_name: CONTAINER-NAME-OR-ID
      new_container_name: NEW-CONTAINER-NAME
    register: result

  - debug: var=result.stdout_lines


'''
def buildah_rename ( module, container_name, new_container_name ):

    if module.get_bin_path('buildah'):
        buildah_bin = module.get_bin_path('buildah')
        buildah_basecmd = [buildah_bin, 'rename']

    if container_name:
        r_cmd = [container_name]
        buildah_basecmd.extend(r_cmd)

    if new_container_name:
        r_cmd = [new_container_name]
        buildah_basecmd.extend(r_cmd)

    return module.run_command(buildah_basecmd) 


def main():

    module = AnsibleModule(
        argument_spec = dict(
            container_name=dict(required=True),
            new_container_name=dict(required=False)
        ),
        supports_check_mode = True
    )

    params = module.params

    container_name = params.get('container_name', '')
    new_container_name = params.get('new_container_name', '')
    
    rc, out, err =  buildah_rename ( module, container_name, new_container_name )

    if rc == 0:
        module.exit_json(changed=True, rc=rc, stdout=out, err = err )
    else:
        module.fail_json(msg = err )

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()

