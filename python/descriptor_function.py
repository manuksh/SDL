""" A function descriptor is used to describe the characteristics and behavior of a function in a software system. 
It provides information about the function's name, description, parameters, return type, visibility, and any other relevant details. 
Function descriptors are typically used in software documentation, code generation, and system analysis to provide a 
clear understanding of the functions available within a system or module.

Here are some common elements that might be included in a function descriptor:
    Name: The name of the function.
    Description: A brief description of what the function does and its purpose.
    Parameters: Details about the parameters accepted by the function, including their names, types, and descriptions.
    Return Type: The type of value returned by the function.
    Visibility: The visibility or accessibility of the function (e.g., public, private, protected).
    Side Effects: Any side effects or changes made by the function when called.
    Error Handling: Information about how errors or exceptions are handled within the function.
    Performance Considerations: Any performance considerations or limitations associated with using the function.

Overall, function descriptors help developers understand how to use functions effectively within a software system and serve as 
valuable documentation for maintaining and extending the system over time.

## Example
descriptor = FunctionDescriptor(
    name="calculate",
    description="Calculates the sum of two numbers.",
    parameters=[
        {"Name": "num1", "Type": "int", "Description": "The first number."},
        {"Name": "num2", "Type": "int", "Description": "The second number."}
    ],
    return_type="int",
    visibility="public"
)

"""
import json
#######################################################
## Descriptor_Function
class Descriptor_Function():
    def __init__(self, name, description, return_type, visibility="public"):
        self.type = "Descriptor_Function"
        self.name = name
        self.description = description
        self.parameters = []
        self.return_type = return_type
        self.visibility = visibility

    def add_parameter(self, name, type, description):
        self.parameters.append({
            "Name": name,
            "Type": type,
            "Description": description
            })


    def get_descriptor_dict(self):
        return {
            'Type': self.type,
            'Name': self.name,
            'Description': self.description,
            'Parameters': self.parameters,
            'visibility': self.visibility
        }

    def get_descriptor(self):
        return json.dumps(self.get_descriptor_dict(), indent=4)

def test():
# Create an instance of Descriptor_Function
    function_descriptor = Descriptor_Function(
        name="calculate_sum",
        description="Calculates the sum of two numbers.",
        return_type="int",
        visibility="public"
    )

    # Add parameters to the function descriptor
    function_descriptor.add_parameter(name="num1", type="int", description="The first number.")
    function_descriptor.add_parameter(name="num2", type="int", description="The second number.")

    # Print the function descriptor
    print(function_descriptor.get_descriptor())

test()