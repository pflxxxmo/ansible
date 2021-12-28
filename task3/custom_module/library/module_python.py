#!/usr/bin/env python

from ansible.module_utils.basic import *

def main():
  module = AnsibleModule(
    argument_spec = dict(
      msg       = dict(required=True, type='str')
    )
  )

  msg = module.params["msg"]

  results = {}

  results.update({
    "changed": True,
    "msg": msg
  })

  module.exit_json(**results)
  
main()
