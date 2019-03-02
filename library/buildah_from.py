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
def buildah_from ( module, host, authfile, cap_add, cap_drop, cert_dir, cgroup_parent, cidfile, cni_config_dir, cni_plugin_path, cpu_period, cpu_quota, cpu_shares, cpuset_cpus, cpuset_mems, creds, ipc, isolation, memory, memory_swap, name, network, pid, pull, pull_always, quiet, security_options, shm_size, signature_policy, tls_verify, ulimit, userns, userns_uid_map, userns_gid_map, userns_uid_map_user, userns_gid_map_group, uts, volume ):

    if module.get_bin_path('buildah'):
        buildah_bin = module.get_bin_path('buildah')
        buildah_basecmd = [buildah_bin, 'from']

    if host:
        r_cmd = ['--add_host']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [host]
        buildah_basecmd.extend(r_cmd)

    if authfile:
        r_cmd = ['--authfile']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [authfile]
        buildah_basecmd.extend(r_cmd)

    ## REVISIT - Multiple Entries
    if cap_add:
        r_cmd = ['--cap_add']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cap_add]
        buildah_basecmd.extend(r_cmd)

    ## REVISIT - Multiple Entries
    if cap_drop:
        r_cmd = ['--cap_drop']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [host]
        buildah_basecmd.extend(r_cmd)

    if cert_dir:
        r_cmd = ['--cert_dir']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cert_dir]
        buildah_basecmd.extend(r_cmd)

    if cgroup_parent:
        r_cmd = ['--cgroup_parent']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cgroup_parent]
        buildah_basecmd.extend(r_cmd)

    if cidfile:
        r_cmd = ['--cidfile']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cidfile]
        buildah_basecmd.extend(r_cmd)

    if cni_config_dir:
        r_cmd = ['--cni_config_dir']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cni_config_dir]
        buildah_basecmd.extend(r_cmd)

    if cni_plugin_path:
        r_cmd = ['--cni_plugin_path']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cni_plugin_path]
        buildah_basecmd.extend(r_cmd)

    if cpu_period:
        r_cmd = ['--cpu_period']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpu_period]
        buildah_basecmd.extend(r_cmd)

    if cpu_quota:
        r_cmd = ['--cpu_quota']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpu_quota]
        buildah_basecmd.extend(r_cmd)

    if cpu_shares:
        r_cmd = ['--cpu_shares']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpu_shares]
        buildah_basecmd.extend(r_cmd)

    if cpuset_cpus:
        r_cmd = ['--cpuset_cpus']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpuset_cpus]
        buildah_basecmd.extend(r_cmd)

    if cpuset_mems:
        r_cmd = ['--cpuset_mems']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cpuset_mems]
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

    if memory_swap:
        r_cmd = ['--memory_swap']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [memory_swap]
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

    if pull_always:
        r_cmd = ['--pull_always']
        buildah_basecmd.extend(r_cmd)

    if quiet:
        r_cmd = ['--quiet']
        buildah_basecmd.extend(r_cmd)

    if security_options:
        r_cmd = ['--security_opt']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [security_options]
        buildah_basecmd.extend(r_cmd)

    if shm_size:
        r_cmd = ['--shm_size']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [shm_size]
        buildah_basecmd.extend(r_cmd)

    if signature_policy:
        r_cmd = ['--signature_policy']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [signature_policy]
        buildah_basecmd.extend(r_cmd)

    if tls_verify:
        r_cmd = ['--tls_verify']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [tls_verify]
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

    if userns_uid_map:
        r_cmd = ['--userns_uid_map']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [userns_uid_map]
        buildah_basecmd.extend(r_cmd)

    if userns_gid_map:
        r_cmd = ['--userns_gid_map']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [userns_gid_map]
        buildah_basecmd.extend(r_cmd)

    if userns_uid_map_user:
        r_cmd = ['--userns_uid_map_user']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [userns_uid_map_user]
        buildah_basecmd.extend(r_cmd)

    if userns_gid_map_group:
        r_cmd = ['--userns_gid_map_group']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [userns_gid_map_group]
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
            cap_add=dict(required=False),
            cap_drop=dict(required=False),
            cert_dir=dict(required=False),
            cgroup_parent=dict(required=False),
            cidfile=dict(required=False),
            cni_config_dir=dict(required=False),
            cni_plugin_path=dict(required=False),
            cpu_period=dict(required=False, type="int"),
            cpu_quota=dict(required=False, type="int"),
            cpu_shares=dict(required=False, type="int"),
            cpuset_cpus=dict(required=False),
            cpuset_mems=dict(required=False),
            creds=dict(required=False),
            ipc=dict(required=False),
            isolation=dict(required=False),
            memory=dict(required=False),
            memory_swap=dict(required=False),
            net=dict(required=False),
            pid=dict(required=False),
            pull=dict(required=False),
            pull_always=dict(required=False),
            quiet=dict(required=False, default="no", type="bool"),
            security_options=dict(required=False),
            shm_size=dict(required=False),
            signature_policy=dict(required=False),
            tls_verify=dict(required=False),
            ulimit=dict(required=False),
            userns=dict(required=False),
            userns_uid_map=dict(required=False),
            userns_gid_map=dict(required=False),
            userns_uid_map_user=dict(required=False),
            userns_gid_map_group=dict(required=False),
            uts=dict(required=False),
            volume=dict(required=False)
        ),
        supports_check_mode = True
    )

    params = module.params

    name = params.get('name', '')
    host = params.get('host', '')
    authfile = params.get('authfile', '')
    cap_add = params.get('cap_add', '')
    cap_drop = params.get('cap_drop', '')
    cert_dir = params.get('cert_dir', '')
    cgroup_parent = params.get('cgroup_parent', '')
    cidfile = params.get('cidfile', '')
    cni_config_dir = params.get('cni_config_dir', '')
    cni_plugin_path = params.get('cni_plugin_path', '')
    cpu_period = params.get('cpu_period', '')
    cpu_quota = params.get('cpu_quota', '')
    cpu_shares = params.get('cpu_shares', '')
    cpuset_cpus = params.get('cpuset_cpus', '')
    cpuset_mems = params.get('cpuset_mems', '')
    creds = params.get('creds', '')
    ipc = params.get('ipc', '')
    isolation = params.get('isolation', '')
    memory = params.get('memory', '')
    memory_swap = params.get('memory_swap', '')
    network = params.get('network', '')
    pid = params.get('pid', '')
    pull = params.get('pull', '')
    pull_always = params.get('pull_always', '')
    quiet = params.get('quiet', '')
    security_options = params.get('security_options', '')
    shm_size = params.get('shm_size', '')
    signature_policy = params.get('signature_policy', '')
    tls_verify = params.get('tls_verify', '')
    ulimit = params.get('ulimit', '')
    userns = params.get('userns', '')
    userns_uid_map = params.get('userns_uid_map', '')
    userns_gid_map = params.get('userns_gid_map', '')
    userns_uid_map_user = params.get('userns_uid_map_user', '')
    userns_gid_map_group = params.get('userns_gid_map_group', '')
    uts = params.get('uts', '')
    volume = params.get('volume', '')

    
    rc, out, err =  buildah_from ( module, host, authfile, cap_add, cap_drop, cert_dir, cgroup_parent, cidfile, cni_config_dir, cni_plugin_path, cpu_period, cpu_quota, cpu_shares, cpuset_cpus, cpuset_mems, creds, ipc, isolation, memory, memory_swap, name, network, pid, pull, pull_always, quiet, security_options, shm_size, signature_policy, tls_verify, ulimit, userns, userns_uid_map, userns_gid_map, userns_uid_map_user, userns_gid_map_group, uts, volume )

    if rc == 0:
        module.exit_json(changed=True, rc=rc, stdout=out, err = err )
    else:
        module.fail_json(msg=err) 

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()

