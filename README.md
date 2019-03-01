# Ansible Module: buildah-ansible

## Description

This is an Ansible Module implementation for the buildah tool.

Buildah is a newly released command line tool for efficiently and quickly building Open Container Initiative (OCI) compliant images and containers. Buildah simplifies the process of creating, building and updating images while decreasing the learning curve of the container environment.

The buildah Ansible module will allow us to automate the "buildah" process to build OCI compliant images and containers.

The following modules are being developed:
 - buildah_add.py
 - buildah_commit.py
 - buildah_config.py
 - buildah_containers.py
 - buildah_copy.py
 - buildah_from.py
 - buildah_images.py
 - buildah_inspect.py

Test playbooks can be found in the test-playbooks/ subdirectory.  W ewill also build unit tests for the modules so we can allow the ability to run tests on our local system.  


Issues should be added to the Issues tab and we encourage you to submit fixes at any time.

If you have any questions please direct them to claudiol@redhat.com or whenry@redhat.com

Thanks!

