#!/usr/bin/python
DOCUMENTATION = '''
---
module: can_reach
description:
	- Checks if a remote server can be reached
version_added: "1.0"
options:
	host:
		description:
			- A DNS hostname or IP address
		required: true
	port:
		description:
		required:
	timeout:
requirements: [netcat]	
author: wlp
notes:
	- This is just an example
	- You 
'''
EXAMPLES = '''
	- can_reach: host=localhost port=18080 timeout=1
'''

def can_reach(module, host, port, timeout):
	nc_path = module.get_bin_path('nc', required=True)
	args = [nc_path, "-z", "-w", str(timeout), host, str(port)]
	(rc, stdout, stderr) = module.run_command(args)
	return rc==0

def main():
	module = AnsibleModule(argument_spec=dict(
					host=dict(required=True), 
					port=dict(required=True, type='int'), 
					timeout=dict(required=False, type='int', default=3)
				), supports_check_mode=True
			)

	if module.check_mode:
		module.exit_json(changed=False)
	host = module.params['host']
	port = module.params['port']
	timeout = module.params['timeout']

	if can_reach(module, host, port, timeout):
		module.exit_json(changed=False)
	else:
		msg="Could not reach %s:%s" % (host, port)
		module.fail_json(msg=msg)

from ansible.module_utils.basic import *
main()


