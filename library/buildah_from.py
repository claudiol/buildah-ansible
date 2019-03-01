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
module: buildah_from
version_added: historical
short_description: Creates a new working container, either from scratch or using a specified image as a starting point.
description:
     -  Creates  a working container based upon the specified image name.  If the supplied image name is "scratch" a new empty container is created.  Image names use a "transport":"details" format.
options:

# informational: requirements for nodes
requirements: [ buildah ]
author:
    - "Red Hat Consulting (NAPS)"
    - "Lester Claudio"
'''

EXAMPLES = '''

  - name: BUILDAH | Test output of "buildah from <image_name>" command
    buildah_add:
      heading: no
    register: result

  - debug: var=result.stdout_lines

'''
def buildah_from ( module, host, authfile, cap-add, cap-drop, cert-dir, cgroup-parent, cidfile, cni-config-dir, cni-plugin-path, cpu-period, cpu-quota, cpu-shares, cpuset-cpus, cpuset-mems, creds, ipc, isolation, memory, memory-swap, name, network, pid, pull, pull-always, quiet, security-opt, shm-size, signature-policy, tls-verify, ulimit, userns, userns-uid-map, userns-gid-map, userns-uid-map-user, userns-gid-map-group, uts, volume ): 

    if module.get_bin_path('buildah'):
        buildah_bin = module.get_bin_path('buildah')
        buildah_basecmd = [buildah_bin, 'from']

    if host:
        r_cmd = ['--add-host']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [host]
        buildah_basecmd.extend(r_cmd)

    if authfile:
        r_cmd = ['--authfile']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [authfile]
        buildah_basecmd.extend(r_cmd)

    ## REVISIT - Multiple Entries
    if cap-add:
        r_cmd = ['--cap-add']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cap-add]
        buildah_basecmd.extend(r_cmd)

    ## REVISIT - Multiple Entries
    if cap-drop:
        r_cmd = ['--cap-drop']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [host]
        buildah_basecmd.extend(r_cmd)

    if cert-dir:
        r_cmd = ['--cert-dir']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cert-dir]
        buildah_basecmd.extend(r_cmd)

    if cgroup-parent:
        r_cmd = ['--cgroup-parent']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cgroup-parent]
        buildah_basecmd.extend(r_cmd)

    if cidfile:
        r_cmd = ['--cidfile']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cidfile]
        buildah_basecmd.extend(r_cmd)

    if cni-config-dir:
        r_cmd = ['--cni-config-dir']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cni-config-dir]
        buildah_basecmd.extend(r_cmd)

    if cni-plugin-path:
        r_cmd = ['--cni-plugin-path']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cni-plugin-path]
        buildah_basecmd.extend(r_cmd)

    if cpu-period:
        r_cmd = ['--cpu-period']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpu-period]
        buildah_basecmd.extend(r_cmd)

    if cpu-quota:
        r_cmd = ['--cpu-quota']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpu-quota]
        buildah_basecmd.extend(r_cmd)

    if cpu-shares:
        r_cmd = ['--cpu-shares']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpu-shares]
        buildah_basecmd.extend(r_cmd)

    if cpuset-cpus:
        r_cmd = ['--cpuset-cpus']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpuset-cpus]
        buildah_basecmd.extend(r_cmd)

    if cpuset-mems:
        r_cmd = ['--cpuset-mems']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpuset-mems]
        buildah_basecmd.extend(r_cmd)

    if creds:
        r_cmd = ['--creds']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [creds]
        buildah_basecmd.extend(r_cmd)

    if ipc:
        r_cmd = ['--ipc']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [ipc]
        buildah_basecmd.extend(r_cmd)

    if isolation:
        r_cmd = ['--isolation']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [isolation]
        buildah_basecmd.extend(r_cmd)

    if memory:
        r_cmd = ['--memory']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [memory]
        buildah_basecmd.extend(r_cmd)

    if memory-swap:
        r_cmd = ['--memory-swap']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [memory-swap]
        buildah_basecmd.extend(r_cmd)

    if network:
        r_cmd = ['--net']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [network]
        buildah_basecmd.extend(r_cmd)

    if pid:
        r_cmd = ['--pid']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [pid]
        buildah_basecmd.extend(r_cmd)

    if pull:
        r_cmd = ['--pull']
        buildah_basecmd.extend(r_cmd)

    if pull-always:
        r_cmd = ['--pull-always']
        buildah_basecmd.extend(r_cmd)

    if quiet:
        r_cmd = ['--quiet']
        buildah_basecmd.extend(r_cmd)

    if security-opt:
        r_cmd = ['--security-opt']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [security-opt]
        buildah_basecmd.extend(r_cmd)

    if shm-size:
        r_cmd = ['--shm-size']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [shm-size]
        buildah_basecmd.extend(r_cmd)

    if signature-policy:
        r_cmd = ['--signature-policy']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [signature-policy]
        buildah_basecmd.extend(r_cmd)

    if tls-verify:
        r_cmd = ['--tls-verify']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [tls-verify]
        buildah_basecmd.extend(r_cmd)

    if ulimit:
        r_cmd = ['--ulimit']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [ulimit]
        buildah_basecmd.extend(r_cmd)

    if userns:
        r_cmd = ['--userns']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [userns]
        buildah_basecmd.extend(r_cmd)

    if userns-uid-map:
        r_cmd = ['--userns-uid-map']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [userns-uid-map]
        buildah_basecmd.extend(r_cmd)

    if userns-gid-map:
        r_cmd = ['--userns-gid-map']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [userns-gid-map]
        buildah_basecmd.extend(r_cmd)

    if userns-uid-map-user:
        r_cmd = ['--userns-uid-map-user']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [userns-uid-map-user]
        buildah_basecmd.extend(r_cmd)

    if userns-gid-map-group:
        r_cmd = ['--userns-gid-map-group']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [userns-gid-map-group]
        buildah_basecmd.extend(r_cmd)

    if uts:
        r_cmd = ['--uts']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [uts]
        buildah_basecmd.extend(r_cmd)

    if volume:
        r_cmd = ['--volume']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [volume]
        buildah_basecmd.extend(r_cmd)

    if name:
        r_cmd = [name]
        buildah_basecmd.extend(r_cmd) 

    return module.run_command(buildah_basecmd) 


def main():

    module = AnsibleModule(
        argument_spec = dict(
            name=dict(required=True),
            host=dict(required=False),
            authfile=dict(required=False, default=""),
            cap-add=dict(required=False),
            cap-drop=dict(required=False),
            cert-dir=dict(required=False),
            cgroup-parent=dict(required=False),
            cidfile=dict(required=False),
            cni-config-dir=dict(required=False),
            cni-plugin-path=dict(required=False),
            cpu-period=dict(required=False, type="int"),
            cpu-quota=dict(required=False, type="int"),
            cpu-shares=dict(required=False, type="int"),
            cpuset-cpus=dict(required=False),
            cpuset-mems=dict(required=False),
            creds=dict(required=False),
            ipc=dict(required=False),
            isolation=dict(required=False),
            memory=dict(required=False),
            memory-swap=dict(required=False),
            net=dict(required=False),
            pid=dict(required=False),
            pull=dict(required=False),
            pull-always=dict(required=False),
            quiet=dict(required=False, default="no", type="bool"),
            security-options=dict(required=False),
            shm-size=dict(required=False),
            signature-policy=dict(required=False),
            tls-verify=dict(required=False),
            ulimit=dict(required=False),
            userns=dict(required=False),
            userns-uid-map=dict(required=False),
            userns-gid-map=dict(required=False),
            userns-uid-map-user=dict(required=False),
            userns-gid-map-group=dict(required=False),
            uts=dict(required=False),
            volume=dict(required=False)
        ),
        supports_check_mode = True
    )

    params = module.params

    name = params.get('name', '')
    host = params.get('host', '')
    authfile = params.get('authfile', '')
    cap-add = params.get('cap-add', '')
    cap-drop = params.get('cap-drop', '')
    cert-dir = params.get('cert-dir', '')
    cgroup-parent = params.get('cgroup-parent', '')
    cidfile = params.get('cidfile', '')
    cni-config-dir = params.get('cni-config-dir', '')
    cni-plugin-path = params.get('cni-plugin-path', '')
    cpu-period = params.get('cpu-period', '')
    cpu-quota = params.get('cpu-quota', '')
    cpu-shares = params.get('cpu-shares', '')
    cpuset-cpus = params.get('cpuset-cpus', '')
    cpuset-mems = params.get('cpuset-mems', '')
    creds = params.get('creds', '')
    ipc = params.get('ipc', '')
    isolation = params.get('isolation', '')
    memory = params.get('memory', '')
    memory-swap = params.get('memory-swap', '')
    net = params.get('net', '')
    pid = params.get('pid', '')
    pull = params.get('pull', '')
    pull-always = params.get('pull-always', '')
    quiet = params.get('quiet', '')
    security-options = params.get('security-options', '')
    shm-size = params.get('shm-size', '')
    signature-policy = params.get('signature-policy', '')
    tls-verify = params.get('tls-verify', '')
    ulimit = params.get('ulimit', '')
    userns = params.get('userns', '')
    userns-uid-map = params.get('userns-uid-map', '')
    userns-gid-map = params.get('userns-gid-map, '')
    userns-uid-map-user = params.get('userns-uid-map-user', '')
    userns-gid-map-group = params.get('userns-gid-map-group', '')
    uts = params.get('uts', '')
    volume = params.get('volume', '')

    
    rc, out, err =  buildah_from ( module, host, authfile, cap-add, cap-drop, cert-dir, cgroup-parent, cidfile, cni-config-dir, cni-plugin-path, cpu-period, cpu-quota, cpu-shares, cpuset-cpus, cpuset-mems, creds, ipc, isolation, memory, memory-swap, name, network, pid, pull, pull-always, quiet, security-opt, shm-size, signature-policy, tls-verify, ulimit, userns, userns-uid-map, userns-gid-map, userns-uid-map-user, userns-gid-map-group, uts, volume )

    if rc == 0:
        module.exit_json(changed=True, rc=rc, stdout=out, err = err )
    else:
        module.fail_json(msg=err) 

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()

