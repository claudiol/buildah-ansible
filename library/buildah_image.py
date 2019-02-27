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
module: buildah
version_added: historical
short_description: Allows the creation of Open Container Initiative (OCI) containers using the buildah command
description:
     - Creates, removes, and lists OCI containers using the buildah container manager. 
options:




  name:
    description:
      - "Package name, or package specifier with version, like C(name-1.0). When using state=latest, this can be '*' which means run: yum -y update. You can also pass a url or a local path to a rpm file (using state=present).  To operate on several packages this can accept a comma separated list of packages or (as of 2.0) a list of packages."
    required: true
    default: null
    aliases: [ 'pkg' ]
  exclude:
    description:
      - "Package name(s) to exclude when state=present, or latest"
    required: false
    version_added: "2.0"
    default: null
  list:
    description:
      - Various (non-idempotent) commands for usage with C(/usr/bin/ansible) and I(not) playbooks. See examples.
    required: false
    default: null
  state:
    description:
      - Whether to install (C(present) or C(installed), C(latest)), or remove (C(absent) or C(removed)) a package.
    required: false
    choices: [ "present", "installed", "latest", "absent", "removed" ]
    default: "present"
  enablerepo:
    description:
      - I(Repoid) of repositories to enable for the install/update operation.
        These repos will not persist beyond the transaction.
        When specifying multiple repos, separate them with a ",".
    required: false
    version_added: "0.9"
    default: null
    aliases: []
  disablerepo:
    description:
      - I(Repoid) of repositories to disable for the install/update operation.
        These repos will not persist beyond the transaction.
        When specifying multiple repos, separate them with a ",".
    required: false
    version_added: "0.9"
    default: null
    aliases: []
  conf_file:
    description:
      - The remote yum configuration file to use for the transaction.
    required: false
    version_added: "0.6"
    default: null
    aliases: []
  disable_gpg_check:
    description:
      - Whether to disable the GPG checking of signatures of packages being
        installed. Has an effect only if state is I(present) or I(latest).
    required: false
    version_added: "1.2"
    default: "no"
    choices: ["yes", "no"]
    aliases: []
  update_cache:
    description:
      - Force updating the cache. Has an effect only if state is I(present)
        or I(latest).
    required: false
    version_added: "1.9"
    default: "no"
    choices: ["yes", "no"]
    aliases: []
  validate_certs:
    description:
      - This only applies if using a https url as the source of the rpm. e.g. for localinstall. If set to C(no), the SSL certificates will not be validated.
      - This should only set to C(no) used on personally controlled sites using self-signed certificates as it avoids verifying the source site.
      - Prior to 2.1 the code worked as if this was set to C(yes).
    required: false
    default: "yes"
    choices: ["yes", "no"]
    version_added: "2.1"
notes:
  - When used with a loop of package names in a playbook, ansible optimizes
    the call to the yum module.  Instead of calling the module with a single
    package each time through the loop, ansible calls the module once with all
    of the package names from the loop.
  - In versions prior to 1.9.2 this module installed and removed each package
    given to the yum module separately. This caused problems when packages
    specified by filename or url had to be installed or removed together. In
    1.9.2 this was fixed so that packages are installed in one yum
    transaction. However, if one of the packages adds a new yum repository
    that the other packages come from (such as epel-release) then that package
    needs to be installed in a separate task. This mimics yum's command line
    behaviour.
  - 'Yum itself has two types of groups.  "Package groups" are specified in the
    rpm itself while "environment groups" are specified in a separate file
    (usually by the distribution).  Unfortunately, this division becomes
    apparent to ansible users because ansible needs to operate on the group
    of packages in a single transaction and yum requires groups to be specified
    in different ways when used in that way.  Package groups are specified as
    "@development-tools" and environment groups are "@^gnome-desktop-environment".
    Use the "yum group list" command to see which category of group the group
    you want to install falls into.'
# informational: requirements for nodes
requirements: [ yum ]
author:
    - "Ansible Core Team"
    - "Seth Vidal"
'''

EXAMPLES = '''
- name: install the latest version of Apache
  yum:
    name: httpd
    state: latest
- name: remove the Apache package
  yum:
    name: httpd
    state: absent
- name: install the latest version of Apache from the testing repo
  yum:
    name: httpd
    enablerepo: testing
    state: present
- name: install one specific version of Apache
  yum:
    name: httpd-2.2.29-1.4.amzn1
    state: present
- name: upgrade all packages
  yum:
    name: '*'
    state: latest
- name: install the nginx rpm from a remote repo
  yum:
    name: http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
    state: present
- name: install nginx rpm from a local file
  yum:
    name: /usr/local/src/nginx-release-centos-6-0.el6.ngx.noarch.rpm
    state: present
- name: install the 'Development tools' package group
  yum:
    name: "@Development tools"
    state: present
- name: install the 'Gnome desktop' environment group
  yum:
    name: "@^gnome-desktop-environment"
    state: present
'''

# 64k.  Number of bytes to read at a time when manually downloading pkgs via a url
BUFSIZE = 65536

def_qf = "%{name}-%{version}-%{release}.%{arch}"
rpmbin = None


def buildah_list_images ( module, name, json, truncate, digests, format, filter, heading ):

    if module.get_bin_path('buildah'):
        buildah_bin = module.get_bin_path('buildah')
        buildah_basecmd = [buildah_bin, 'images']

    if json:
        r_cmd = ['--json']
        buildah_basecmd.extend(r_cmd)

    if truncate != True:
        r_cmd = ['--no-trunc']
        buildah_basecmd.extend(r_cmd)

    if format != "":
        r_cmd = ['--format']
        buildah_basecmd.extend(r_cmd)
        r_cmd = "'{{.ID}} {{.Name}} {{.Digest}} {{.CreatedAt}} {{.Size}}'"
        buildah_basecmd.extend(r_cmd)

    if digests:
        r_cmd = ['--digests']
        buildah_basecmd.extend(r_cmd)

    if heading:
        r_cmd = ['--noheading']
        buildah_basecmd.extend(r_cmd)
        
    if name:
        r_cmd = [name]
        buildah_basecmd.extend(r_cmd)
        

    return module.run_command(buildah_basecmd) 


def main():

    module = AnsibleModule(
        argument_spec = dict(
            name=dict(required=True), 
            json=dict(required=False, default="no", type='bool'),
            truncate=dict(required=False, default="yes", type='bool'),
            digests=dict(required=False, default="no", type='bool'),
            format=dict(required=False, default=""),
            filter=dict(required=False, default=""),
            heading=dict(required=False, default="yes")
        ),
        required_one_of = [['name','str']],
        mutually_exclusive = [['name','str']],
        supports_check_mode = True
    )

    params = module.params

    id = params.get('name', '') 
    json = params.get('json', '')
    truncate = params.get('truncate', '')
    digests = params.get('digests', '')
    format = params.get('format', '')
    filter = params.get('filter', '')
    heading = params.get('heading', '')
    
    rc, out, err =  buildah_list_images(module, id, json, truncate, digests, format, filter, heading)

    if rc == 0:
        module.exit_json(changed=True, rc=rc, stdout=out, err = err )
    else:
        module.exit_json(changed=False, rc=rc, stdout=out, err = err )

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()

