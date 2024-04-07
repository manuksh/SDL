"""A utility component is a software component designed to provide general-purpose functionality that can be 
used across different parts of a system or application. It typically encapsulates reusable functions or operations 
that are not specific to any particular domain or feature.
The descriptor for a utility component would include information that describes its purpose, functionality, 
and usage. Here are some common elements that might be included in the descriptor for a utility component:

Name: The name of the utility component.
Description: A brief description of what the utility component does and its purpose.
Usage: Information about how the utility component is intended to be used and examples of scenarios where it might be useful.
Dependencies: Any external libraries or modules that the utility component relies on.
Methods or Functions: Details about the functions or methods provided by the utility component, including their names, descriptions, parameters, return types, and any side effects.
Constants or Configuration: Any constants or configuration parameters used by the utility component.
Error Handling: Information about how errors or exceptions are handled within the utility component.
Performance Considerations: Any performance considerations or limitations associated with using the utility component.
Overall, the descriptor for a utility component provides developers with the necessary information to understand how to use the utility component effectively and integrate it into their projects. It serves as documentation for both internal and external users of the utility component.

# Example
{
    "Type": "Descriptor_Utility",
    "Name": "FileUtility",
    "Description": "A utility for file management operations.",
    "Usage": "Used for reading, writing, and manipulating files.",
    "Dependencies": [
        "os",
        "sys"
    ],
    "Methods": [
        {
            "Name": "read_file",
            "Description": "Reads data from a file and returns it as a string.",
            "Parameters": [
                {
                    "Name": "file_path",
                    "Type": "str",
                    "Description": "The path to the file to be read."
                }
            ],
            "Return_Type": "str",
            "Visibility": "public"
        },
        {
            "Name": "write_file",
            "Description": "Writes data to a file.",
            "Parameters": [
                {
                    "Name": "file_path",
                    "Type": "str",
                    "Description": "The path to the file to be written."
                },
                {
                    "Name": "data",
                    "Type": "str",
                    "Description": "The data to be written to the file."
                }
            ],
            "Return_Type": "None",
            "Visibility": "public"
        },
        {
            "Name": "delete_file",
            "Description": "Deletes a file from the filesystem.",
            "Parameters": [
                {
                    "Name": "file_path",
                    "Type": "str",
                    "Description": "The path to the file to be deleted."
                }
            ],
            "Return_Type": "None",
            "Visibility": "public"
        }
    ]
}
"""

import json

class Descriptor_Utility:
    def __init__(self, name, description, usage, dependencies):
        self.type = 'Descriptor_Utility'
        self.name = name
        self.description = description
        self.usage = usage
        self.dependencies = dependencies
        self.methods = []

    def add_method(self, name, description, parameters, return_type, visibility):
        method = {
            "Name": name,
            "Description": description,
            "Parameters": parameters,
            "Return_Type": return_type,
            "Visibility": visibility
        }
        self.methods.append(method)

    def get_descriptor_dict(self):
        return {
            "Type": self.type,
            "Name": self.name,
            "Description": self.description,
            "Usage": self.usage,
            "Dependencies": self.dependencies,
            "Methods": self.methods,
        }

    def get_descriptor(self):
        return json.dumps(self.get_descriptor_dict(), indent=4)



#####################################################
## Test
def test():

    # Create an instance of Descriptor_Utility
    file_utility = Descriptor_Utility(
        name="FileUtility",
        description="A utility for file management operations.",
        usage="Used for reading, writing, and manipulating files.",
        dependencies=["os", "sys"]
    )

    # Add methods to the utility
    file_utility.add_method(
        name="read_file",
        description="Reads data from a file and returns it as a string.",
        parameters=[
            {"Name": "file_path", "Type": "str", "Description": "The path to the file to be read."}
        ],
        return_type="str",
        visibility="public"
    )

    file_utility.add_method(
        name="write_file",
        description="Writes data to a file.",
        parameters=[
            {"Name": "file_path", "Type": "str", "Description": "The path to the file to be written."},
            {"Name": "data", "Type": "str", "Description": "The data to be written to the file."}
        ],
        return_type="None",
        visibility="public"
    )

    file_utility.add_method(
        name="delete_file",
        description="Deletes a file from the filesystem.",
        parameters=[
            {"Name": "file_path", "Type": "str", "Description": "The path to the file to be deleted."}
        ],
        return_type="None",
        visibility="public"
    )

    # Print the descriptor
    print(file_utility.get_descriptor())


#####################################################
def test2():
    # Step 1: Create an instance of Descriptor_Utility without methods
    file_utility = Descriptor_Utility(
        name="FileUtility",
        description="A utility for file management operations.",
        usage="Used for reading, writing, and manipulating files.",
        dependencies=["os", "sys"]
    )

    # Step 2: Add methods one by one
    file_utility.methods.append({
        "Name": "read_file",
        "Description": "Reads data from a file and returns it as a string.",
        "Parameters": [
            {"Name": "file_path", "Type": "str", "Description": "The path to the file to be read."}
        ],
        "Return_Type": "str",
        "Visibility": "public"
    })

    file_utility.methods.append({
        "Name": "write_file",
        "Description": "Writes data to a file.",
        "Parameters": [
            {"Name": "file_path", "Type": "str", "Description": "The path to the file to be written."},
            {"Name": "data", "Type": "str", "Description": "The data to be written to the file."}
        ],
        "Return_Type": "None",
        "Visibility": "public"
    })

    file_utility.methods.append({
        "Name": "delete_file",
        "Description": "Deletes a file from the filesystem.",
        "Parameters": [
            {"Name": "file_path", "Type": "str", "Description": "The path to the file to be deleted."}
        ],
        "Return_Type": "None",
        "Visibility": "public"
    })

    # Step 3: Print the generated descriptor
    print(file_utility.get_descriptor())



if __name__ == "__main__":
    test()
    test2()   

