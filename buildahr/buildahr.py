import sys
import oyaml, ruamel.yaml

from oyaml import load, dump

DOCUMENTATION = '''
---
module: buildahr
version_added: historical
short_description: Creates an Ansible Playbook from a simpler YAML file:
     -  <add more here>:

# informational: requirements for nodes
requirements: [ buildah, libselinux-python ]
author:
    - "Red Hat"
    - "William Henry"
'''

EXAMPLES = '''

  - name: BUILDAHR | Generate ansible-buildah playbook "buildahr <buildahbook.yml>" command
	image:
	  name: myfedorapy
	  from: quay.io/fedora:latest
	  packages: python
	  copy: library/buildahr.py /tmp
 	  config:
	    author: ipbabble
	  cmd: python --version

  - debug: var=result.stdout_lines

'''

class Buildahfrom(object):
	yaml_tag = u'name: BUILDAH - start the new image from'

	def __init__(self, image):
		self.buildah_from = { 'name': image}
		self.register = 'from_result'

'''
def buildahr_from(buildahyaml, playbook):

	print oyaml.dump(buildahyaml['image'])
	task = list()
	task[0]['name'] = "BUILDAH -buildah from "
	task[0]['buildah_from'] = "BUILDAH -buildah from "
	task[0]['buildah_from']['name'] = buildahyaml['image']['from']
	task[0]['register'] = "from_result"
	playbook['tasks'][0] = task 
#	playbook['tasks'][0]['buildah_from'] = ""
#	playbook['tasks'][0]['buildah_from']['name'] = buildahyaml['image']['from']
	print oyaml.dump(playbook)
'''

def main():

	with open("buildahbook.yml", "r") as buildahbook:
		try:
			buildahyaml = oyaml.safe_load(buildahbook)
		except oyaml.YAMLError as ymlexcp:
			print(ymlexcp)
	try:
		print oyaml.dump(buildahyaml)
	except oyaml.YAMLError as ymlexcp:
		print(ymlexcp)

	playbook = dict()
	playbook['tasks'] = list()

	pbyaml = ruamel.yaml.YAML()
	#try:
#	if buildahyaml['image']['from'] != "":
#		buildahr_from(buildahyaml, playbook)
	#except Exception as e:
	#	raise e

	with open('buildah_playbook.yml', 'w') as outfile:
		pbyaml.register_class(Buildahfrom)
		from_image = buildahyaml['image']['from']
		print(from_image)
#	   	pbyaml.dump([Buildahfrom(from_image)], outfile)
	   	pbyaml.dump([Buildahfrom(from_image)], sys.stdout)

if __name__ == '__main__':
    main()	
    