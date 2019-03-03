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
module: buildah_cofig
version_added: historical
short_description: Updates one or more of the settings kept for a container.

description:
     - Updates one or more of the settings kept for a container.

options:

# informational: requirements for nodes
requirements: [ buildah ]
author:
    - "Red Hat Consulting (NAPS)"
    - "Lester Claudio"
'''

EXAMPLES = '''

  - name: BUILDAH | Test output of "buildah add --noheading <image_name>" command
    buildah_add:
      heading: no
    register: result

  - debug: var=result.stdout_lines

'''
def buildah_config ( module, name, annotation, arch, author, cmd,
                   comment, created_by, domain, entrypoint,
                   env, healthcheck, healthcheck_interval,
                   healthcheck_retries, healthcheck_start_period,
                   healthcheck_timeout, history_comment,
                   hostname, label, onbuild, os, port, shell,
                   stop_signal, user, volume, workingdir):

    if module.get_bin_path('buildah'):
        buildah_bin = module.get_bin_path('buildah')
        buildah_basecmd = [buildah_bin, 'config']

    if annotation:
        r_cmd = ['--annotation']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [annotation]
        buildah_basecmd.extend(r_cmd)
        
    if arch:
        r_cmd = ['--arch']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [arch]
        buildah_basecmd.extend(r_cmd)

    if author:
        r_cmd = ['--author']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [author]
        buildah_basecmd.extend(r_cmd)

    if cmd:
        r_cmd = ['--cmd']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [cmd]
        buildah_basecmd.extend(r_cmd)

    if comment:
        r_cmd = ['--comment']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [comment]
        buildah_basecmd.extend(r_cmd)

    if created_by:
        r_cmd = ['--created-by']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [created_by]
        buildah_basecmd.extend(r_cmd)

    if domain:
        r_cmd = ['--domainname']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [domain]
        buildah_basecmd.extend(r_cmd)

    if entrypoint:
        r_cmd = ['--entrypoint']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [entrypoint]
        buildah_basecmd.extend(r_cmd)

    if env:
        r_cmd = ['--env']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [env]
        buildah_basecmd.extend(r_cmd)

    if healthcheck:
        r_cmd = ['--healthcheck']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [healthcheck]
        buildah_basecmd.extend(r_cmd)

    if healthcheck_interval:
        r_cmd = ['--healthcheck-interval']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [healthcheck_interval]
        buildah_basecmd.extend(r_cmd)

    if healthcheck_retries:
        r_cmd = ['--healthcheck-retries']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [healthcheck_retries]
        buildah_basecmd.extend(r_cmd)

    if healthcheck_start_period:
        r_cmd = ['--healthcheck-start-period']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [healthcheck_start_period]
        buildah_basecmd.extend(r_cmd)

    if healthcheck_timeout:
        r_cmd = ['--healthcheck-timeout']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [healthcheck_timeout]
        buildah_basecmd.extend(r_cmd)

    if history_comment:
        r_cmd = ['--history-comment']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [history_comment]
        buildah_basecmd.extend(r_cmd)

    if hostname:
        r_cmd = ['--hostname']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [hostname]
        buildah_basecmd.extend(r_cmd)

    if label:
        r_cmd = ['--label']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [label]
        buildah_basecmd.extend(r_cmd)

    ## REVISIT
    if onbuild:
        r_cmd = ['--onbuild']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [onbuild]
        buildah_basecmd.extend(r_cmd)

    if os:
        r_cmd = ['--os']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [os]
        buildah_basecmd.extend(r_cmd)

    if port:
        r_cmd = ['--port']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [port]
        buildah_basecmd.extend(r_cmd)

    if shell:
        r_cmd = ['--shell']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [shell]
        buildah_basecmd.extend(r_cmd)

    if stop_signal:
        r_cmd = ['--stop-signal']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [stop_signal]
        buildah_basecmd.extend(r_cmd)

    if user:
        r_cmd = ['--user']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [user]
        buildah_basecmd.extend(r_cmd)

    if volume:
        r_cmd = ['--volume']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [volume]
        buildah_basecmd.extend(r_cmd)

    if workingdir:
        r_cmd = ['--workingdir']
        buildah_basecmd.extend(r_cmd)
        r_cmd = [workingdir]
        buildah_basecmd.extend(r_cmd)

    if name:
        r_cmd = [name]
        buildah_basecmd.extend(r_cmd) 

        
    return module.run_command(buildah_basecmd) 


def main():

    module = AnsibleModule(
        argument_spec = dict(
            name=dict(required=True),
            annotation=dict(required=False, default=""),
            arch=dict(required=False, default=""),
            author=dict(required=False, default=""),
            cmd=dict(required=False, default=""),
            comment=dict(required=False, default=""),
            created_by=dict(required=False, default=""),
            domain=dict(required=False, default=""),
            entrypoint=dict(required=False, default=""),
            env=dict(required=False, default=""),
            healthcheck=dict(required=False, default="NONE"),
            healthcheck_interval=dict(required=False, type="int"),
            healthcheck_retries=dict(required=False, type="int"),
            healthcheck_start_period=dict(required=False, type="int"),
            healthcheck_timeout=dict(required=False, type="int"),
            history_comment=dict(required=False, default=""),
            hostname=dict(required=False, default=""),
            label=dict(required=False, default=""),
            onbuild=dict(required=False),
            os=dict(required=False),
            port=dict(required=False),
            shell=dict(required=False),
            stop_signal=dict(required=False),
            user=dict(rquired=False),
            volume=dict(required=False),
            workingdir=dict(required=False)
        ),
        supports_check_mode = True
    )

    params = module.params

    name = params.get('name', '')
    annotation = params.get('annotation', '')
    arch = params.get('arch', '')
    author = params.get('author', '')
    cmd = params.get('cmd', '')
    comment = params.get('comment', '')
    created_by = params.get('created_by', '')
    domain = params.get('domain', '')
    entrypoint = params.get('entrypoint', '')
    env = params.get('env', '')
    healthcheck = params.get('env', '')
    healthcheck_interval=params.get('heathcheck_interval', '')
    healthcheck_retries=params.get('healthecheck_retries', '')
    healthcheck_start_period=params.get('healcheck_start_period','')
    healthcheck_timeout=params.get('healthcheck_timeout','')
    history_comment=params.get('history_comment', '')
    hostname=params.get('hostname','')
    label=params.get('label', '')
    onbuild=params.get('onbuild','')
    os=params.get('os', '')
    port=params.get('port', '')
    shell=params.get('shell', '')
    stop_signal=params.get('stop_signal', '')
    user=params.get('user','')
    volume=params.get('volume', '')
    workingdir=params.get('workingdir', '')
    

    
    rc, out, err =  buildah_config(module, name, annotation, arch, author, cmd,
                                   comment, created_by, domain, entrypoint,
                                   env, healthcheck, healthcheck_interval,
                                   healthcheck_retries, healthcheck_start_period,
                                   healthcheck_timeout, history_comment,
                                   hostname, label, onbuild, os, port, shell,
                                   stop_signal, user, volume, workingdir)

    if rc == 0:
        module.exit_json(changed=True, rc=rc, stdout=out, err = err )
    else:
        module.exit_json(changed=False, rc=rc, stdout=out, err = err )

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()





