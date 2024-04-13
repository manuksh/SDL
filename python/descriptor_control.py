"""A "control" descriptor typically refers to a component or entity within a software system that manages or regulates the flow of data, 
processes, or interactions. The purpose of a control descriptor is to describe such control components in a structured manner, providing 
essential information about their functionality, behavior, and usage within the system.

Here are some key aspects that a control descriptor might cover:

Name: The name or identifier of the control component.
Description: A brief overview of the purpose and functionality of the control.
Input/Output: Details about the inputs and outputs that the control component processes or generates.
Processing Logic: Information about the algorithms, rules, or logic implemented by the control component to process data or perform actions.
Dependencies: Any external resources, libraries, or services that the control component relies on.
Error Handling: How the control component handles errors, exceptions, or unexpected conditions during execution.
Concurrency and Synchronization: If applicable, details about how the control component manages concurrency and synchronization of operations.
Event Handling: How the control component responds to and handles events or triggers from other parts of the system.
Lifecycle Management: Information about the lifecycle of the control component, including initialization, execution, and termination.
Configuration: Any configurable parameters or settings that control the behavior of the component.
Security Considerations: Security measures and best practices relevant to the control component, such as access control or data encryption.
Performance Considerations: Factors affecting the performance of the control component and strategies for optimization if needed.
Overall, the control descriptor helps developers understand the role and behavior of control components within a software system, facilitating e
ffective integration, configuration, and management of these components. It serves as documentation to guide the development, maintenance, and operation of the system.

### Example 1
{
    "Type": "Descriptor_Control",
    "Name": "TemperatureControl",
    "Description": "Manages temperature regulation in a heating system.",
    "Inputs": [
        {
            "Name": "desired_temperature",
            "Type": "float",
            "Description": "The target temperature to maintain."
        },
        {
            "Name": "current_temperature",
            "Type": "float",
            "Description": "The current temperature sensed by the system."
        }
    ],
    "Outputs": [
        {
            "Name": "heater_status",
            "Type": "bool",
            "Description": "Indicates whether the heater is active."
        }
    ],
    "Processing_Logic": "Compares the desired temperature with the current temperature and activates/deactivates the heater accordingly.",
    "Dependencies": [
        "Temperature Sensor",
        "Heater Control Module"
    ],
    "Error_Handling": "Handles errors related to sensor malfunction, heater failure, or invalid input values.",
    "Concurrency_Synchronization": "Ensures thread-safe access to shared resources and prevents race conditions.",
    "Event_Handling": "Triggers events based on temperature changes or system failures.",
    "Lifecycle_Management": "Initializes components during system startup, monitors temperature continuously, and shuts down gracefully when not needed.",
    "Configuration": "Allows adjustment of temperature thresholds and control parameters.",
    "Security_Considerations": "Ensures secure communication between components and prevents unauthorized access to sensitive data.",
    "Performance_Considerations": "Optimizes control algorithms for fast response times and minimal energy consumption."
}

"""

import json
#######################################################
## Descriptor_Control
class Descriptor_Control():
    def __init__(self, name, description, Functions, Parameters):
        self.type = "Descriptor_Control"
        self.name = name
        self.description = description
        self.inputs = []
        self.outputs = []   

    def add_input(self, name, type, description):
        self.inputs.append({        
            "Name": name,
            "Type": type,
            "Description": description
            })      
    
    def add_output(self, name, type, description):  
        self.outputs.append({        
            "Name": name,
            "Type": type,
            "Description": description
            })      
        
    def get_descriptor_dict(self):      
        return {
            'Type': self.type,
            'Name': self.name,
            'Description': self.description,
            'Inputs': self.inputs,
            'Outputs': self.outputs
        }       
    def get_descriptor(self):
        return json.dumps(self.get_descriptor_dict(), indent=4) 
def test(): 
    # Create an instance of Descriptor_Control
    control_descriptor = Descriptor_Control(
        name="TemperatureControl",
        description="Manages temperature regulation in a heating system.",
        Functions={
            "desired_temperature": "float",
            "current_temperature": "float"
        },
        Parameters={
            "heater_status": "bool"
        }
    )
    # Add inputs and outputs
    control_descriptor.add_input(name="desired_temperature", type="float", description="The target temperature to maintain.")
    control_descriptor.add_input(name="current_temperature", type="float", description="The current temperature sensed by the system.")
    control_descriptor.add_output(name="heater_status", type="bool", description="Indicates whether the heater is active.")
    print(control_descriptor.get_descriptor())          

if __name__ == "__main__":
    test()  

