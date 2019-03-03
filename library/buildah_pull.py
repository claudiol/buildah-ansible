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
module: buildah_pull
version_added: historical
short_description: buildah-pull - Creates a new working container using a specified image as a starting point.
description:
     - Pulls an image based upon the specified image name.  Image names use a "transport":"details" format.

options:

# informational: requirements for nodes
requirements: [ buildah ]
author:
    - "Red Hat Consulting (NAPS)"
    - "Lester Claudio"
'''

EXAMPLES = '''
  - name: BUILDAH | Test "buildah pull <image_name>" command
    buildah_pull:
      name: quay.io/ipbabble/myfedoratest
    register: result

  - debug: var=result.stdout_lines


'''
def buildah_pull ( module, name, authfile, cert_dir, creds, quiet, signature_policy, tls_verify ): 

    if module.get_bin_path('buildah'):
        buildah_bin = module.get_bin_path('buildah')
        buildah_basecmd = [buildah_bin, 'pull']

    if authfile:
        r_cmd = ['--authfile']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [authfile]
        buildah_basecmd.extend(r_cmd)

    if cert_dir:
        r_cmd = ['--cert-dir']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cert_dir]
        buildah_basecmd.extend(r_cmd)

    if creds:
        r_cmd = ['--creds']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [creds]
        buildah_basecmd.extend(r_cmd)

    if signature_policy:
        r_cmd = ['--signature-policy']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [signature_policy]
        buildah_basecmd.extend(r_cmd)

    if tls_verify:
        r_cmd = ['--tls-verify']
        buildah_basecmd.extend(r_cmd)

    if quiet:
        r_cmd = ['--quiet']
        buildah_basecmd.extend(r_cmd)

    if name:
        r_cmd = [name]
        buildah_basecmd.extend(r_cmd) 
        
    return module.run_command(buildah_basecmd) 


def main():

    module = AnsibleModule(
        argument_spec = dict(
            name=dict(required=True),
            authfile=dict(required=False),
            cert_dir=dict(required=False),
            creds=dict(required=False),
            quiet=dict(required=False, default="no", type="bool"),
            signature_policy=dict(required=False),
            tls_verify=dict(required=False, default="no", type="bool")
        ),
        supports_check_mode = True
    )

    params = module.params

    name = params.get('name', '')
    authfile = params.get('authfile', '')
    cert_dir = params.get('cert_dir', '')
    creds = params.get('creds', '')
    quiet = params.get('quiet', '')
    signature_policy  = params.get('signature_policy', '')
    tls_verify = params.get('tls_verify', '')
    
    rc, out, err =  buildah_pull ( module, name, authfile, cert_dir, creds, quiet, signature_policy, tls_verify )

    if rc == 0:
        module.exit_json(changed=True, rc=rc, stdout=out, err = err )
    else:
        module.fail_json(msg = err )

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()

