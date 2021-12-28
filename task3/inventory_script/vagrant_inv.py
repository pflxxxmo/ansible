import vagrant
import os
import json


def main():
    stack = vagrant.Vagrant(os.getcwd())
    vms_info = stack.status()
    for vm in vms_info:
        if vm.state == "running":
            print(json.dumps({
                "vagrant": {
                    "hosts": [
                        vm.name
                    ],
                    "state": [
                        vm.state
                    ]
                }
            }))

if __name__ == '__main__':  
    main()
