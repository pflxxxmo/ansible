#!/usr/bin/python

def email(variable, prefix="epam.com"):
    new_email=[]
    for element in variable:
        new_email.append(str(element.get("name") + "_" + element.get("surname") + "@" + prefix))
    return new_email

class FilterModule(object):
    def filters(self):
        return {
            'email': email,
        }
