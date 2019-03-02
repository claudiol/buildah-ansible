#!/usr/bin/python

#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# (c) 2019, Red Hat, Inc
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
module: buildah_copy
version_added: historical
short_description: buildah-copy  - Copies the contents of a file, URL, or directory into a container's working
       directory.
description:
     - buildah-copy  - Copies the contents of a file, URL, or directory into a container's working
       directory.
options:

# informational: requirements for nodes
requirements: [ buildah ]
author:
    - "Red Hat Consulting (NAPS)"
    - "Lester Claudio"
'''

EXAMPLES = '''
  - name: BUILDAH | Test output of "buildah copy <container_name/id> source destination" command
    buildah_copy:
      name: c3897c41ac18    # <=== target container
      src: '/tmp/file.conf" # <=== file in target buildah host
    register: result

  - debug: var=result.stdout_lines

  - name: BUILDAH | Test output of "buildah copy <container_name/id> source destination" command
    buildah_copy:
      name: c3897c41ac18    # <=== target container
      src: '/tmp/file.conf" # <=== file that exists on target buildah host
      dest: '/etc/file.com' # <=== destination file on target container storage 
    register: result

  - debug: var=result.stdout_lines

  - name: BUILDAH | Test output of "buildah copy <container_name/id> source " command
    buildah_copy:
      name: c3897c41ac18    # <=== target container
      src: '/tmp/file.conf" # <=== file in target buildah host
      chown: 'claudiol:claudiol' # <=== Change owner:group
    register: result

  - debug: var=result.stdout_lines


'''
def buildah_copy ( module, name, chown, quiet, src, dest ):

    if module.get_bin_path('buildah'):
        buildah_bin = module.get_bin_path('buildah')
        buildah_basecmd = [buildah_bin, 'copy']

    if chown:
        r_cmd = ['--chown']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [chown]
        buildah_basecmd.extend(r_cmd)
        
    if quiet:
        r_cmd = ['--quiet']
        buildah_basecmd.extend(r_cmd)

    if name:
        r_cmd = [name]
        buildah_basecmd.extend(r_cmd) 

    if src:
        r_cmd = [src]
        buildah_basecmd.extend(r_cmd) 

    if dest:
        r_cmd = [dest]
        buildah_basecmd.extend(r_cmd) 
        
    return module.run_command(buildah_basecmd) 


def main():

    module = AnsibleModule(
        argument_spec = dict(
            name=dict(required=True),
            chown=dict(required=False, default=""),
            quiet=dict(required=False, default="no", type="bool"),
            src=dict(required=True),
            dest=dict(required=True)
        ),
        supports_check_mode = True
    )

    params = module.params

    name = params.get('name', '')
    chown = params.get('chown', '')
    quiet = params.get('quiet', '')
    src = params.get('src', '')
    dest = params.get('dest', '')
    
    rc, out, err =  buildah_copy(module, name, chown, quiet, src, dest)

    if rc == 0:
        module.exit_json(changed=True, rc=rc, stdout=out, err = err )
    else:
        module.exit_json(changed=False, rc=rc, stdout=out, err = err )

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()

