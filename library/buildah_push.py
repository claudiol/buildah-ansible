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
module: buildah_mount
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
    buildah_push:
      name: IMAGE
      quiet: yes
    register: result

  - debug: var=result.stdout_lines


'''
def buildah_push ( module, name, dest, authfile, cert-dir, quiet, signature-policy, tls-verify ): 

    if module.get_bin_path('buildah'):
        buildah_bin = module.get_bin_path('buildah')
        buildah_basecmd = [buildah_bin, 'push']

    if authfile:
        r_cmd = ['--authfile']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [authfile]
        buildah_basecmd.extend(r_cmd)

    if cert-dir:
        r_cmd = ['--cert-dir']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cert-dir]
        buildah_basecmd.extend(r_cmd)

    if authfile:
        r_cmd = ['--creds']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [creds]
        buildah_basecmd.extend(r_cmd)

    if signature-policy:
        r_cmd = ['--signature-policy']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [signature-policy]
        buildah_basecmd.extend(r_cmd)

    if tls-verify:
        r_cmd = ['--tls-verify']
        buildah_basecmd.extend(r_cmd)

    if quiet:
        r_cmd = ['--quiet']
        buildah_basecmd.extend(r_cmd)

    if name:
        r_cmd = [name]
        buildah_basecmd.extend(r_cmd) 

    if dest:
        r_cmd = [dest]
        buildah_basecmd.extend(r_cmd) 

    return module.run_command(buildah_basecmd) 


def main():

    module = AnsibleModule(
        argument_spec = dict(
            name=dict(required=True),
            dest=dict(required=False),
            authfile=(required=False),
            cert-dir=(required=False),
            creds=(required=False),
            quiet=(required=False, default="no", type="bool"),
            signature-policy=(required=False),
            tls-verify=dict(required=False, default="no", type="bool")
        ),
        supports_check_mode = True
    )

    params = module.params

    name = params.get('name', '')
    dest = params.get('dest', '')
    authfile = params.get('authfile', '')
    cert-dir = params.get('cert-dir', '')
    creds = params.get('creds', '')
    quiet = params.get('creds', '')
    signature-policy  = params.get('signature-policy', '')
    tls-verify = params.get('tls-verify', '')
    
    rc, out, err =  buildah_push ( module, name, dest, authfile, cert-dir, quiet, signature-policy, tls-verify )

    if rc == 0:
        module.exit_json(changed=True, rc=rc, stdout=out, err = err )
    else:
        module.fail_json(msg = err )

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()

