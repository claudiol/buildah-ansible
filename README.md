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
 - buildah_mount.py
 - buildah_pull.py
 - buildah_push.py
 - buildah_rename.py
 - buildah_rm.py
 - buildah_rmi.py
 - buildah_tag.py
 - buildah_umount.py

The targeted functionality planned will include the following:

|    buildah command             | Description              | Status |
|    ----------------            | -----------              | ------ |
|     add                        |  Add content to the container | TESTED |
|     build-using-dockerfile, bud|  Build an image using instructions in a Dockerfile | NOT TESTED |
|     commit                     |  Create an image from a working container | TESTED |
|     config                     |  Update image configuration settings | TESTED |
|     containers                 |  List working containers and their base images | TESTED |
|     copy                       |  Copy content into the container | TESTED |
|     from                       |  Create a working container based on an image | TESTED |
|     images                     |  List images in local storage | TESTED |
|     inspect                    |  Inspects the configuration of a container or image | TESTED |
|     mount                      |  Mount a working container's root filesystem | TESTED |
|     pull                       |  Pull an image from the specified location | NOT TESTED |
|     push                       |  Push an image to a specified destination | TESTED |
|     rename                     |  Rename a container | NOT TESTED |
|     rm, delete                 |  Remove one or more working containers | TESTED |
|     rmi                        |  removes one or more images from local storage | NOT TESTED |
|     tag                        |  Add an additional name to a local image | NOT TESTED |
|     umount, unmount            |  Unmounts the root file system on the specified working containers | TESTED |
|     unshare                    |  Run a command in a modified user namespace | NOT IMPLEMENTED |


Test playbooks can be found in the test-playbooks/ subdirectory.  W ewill also build unit tests for the modules so we can allow the ability to run tests on our local system.  


Issues should be added to the Issues tab and we encourage you to submit fixes at any time.

If you have any questions please direct them to claudiol@redhat.com or whenry@redhat.com

Thanks!

