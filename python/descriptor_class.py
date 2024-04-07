"""A class component represents a blueprint or template for creating objects. 
It defines the attributes and behaviors that objects of that class will have. 
The descriptor for a class component typically includes the following information:

Name: The name of the class.
Description: A brief description of what the class represents or does.
Inheritance: If the class inherits from another class, this indicates the superclass or parent class.
Attributes: Details about the attributes (variables) of the class, such as their names, types, descriptions, 
default values, and visibility (public, private, protected).
Methods: Information about the methods (functions) of the class, including their names, descriptions, 
parameters, return types, and visibility.
Additionally, the descriptor may include other relevant information such as the module or package to 
which the class belongs, any interfaces implemented by the class, or any constants defined within the class.

Overall, the descriptor for a class component provides a comprehensive overview of the class structure and 
functionality.
"""

import json
#######################################################
## Descriptor_Class
class Descriptor_Class:
    def __init__(self):
        self.Type = "Descriptor_Class"
        self.Name = ""
        self.Description = ""
        self.Inheritance = ""
        self.Attributes = []
        self.Methods = []

    def add_attribute(self, name, type_, description, default, visibility):
        self.Attributes.append({
            "Name": name,
            "Type": type_,
            "Description": description,
            "Default": default,
            "Visibility": visibility
        })

    def add_method(self, name, description, parameters, return_type, visibility):
        self.Methods.append({
            "Name": name,
            "Description": description,
            "Parameters": parameters,
            "Return_Type": return_type,
            "Visibility": visibility
        })

    def get_descriptor_dict(self):
        return {
            "Type": self.Type,
            "Name": self.Name,
            "Description": self.Description,
            "Inheritance": self.Inheritance,
            "Attributes": self.Attributes,
            "Methods": self.Methods
        }
    
    def get_descriptor(self):
        return (json.dumps(self.get_descriptor_dict(), indent=4))

def test():
    # Example usage:
    template = Descriptor_Class()
    template.Name = "Valve"
    template.Description = "Represents a valve used in a process control system."
    template.Inheritance = "Component"
    template.add_attribute("state", "bool", "Represents the current state of the valve (Open or Close).", "False", "private")
    template.add_attribute("Flag", "str", "Additional flag for the valve.", "None", "protected")
    template.add_method("open", "Opens the valve and sets state to Open.", [], "None", "public")
    template.add_method("close", "Closes the valve and sets state to Close.", [], "None", "public")
    template.add_method("getState", "Returns the current state of the valve.", [], "bool", "public")

    descriptor = template.get_descriptor()
    print(descriptor)