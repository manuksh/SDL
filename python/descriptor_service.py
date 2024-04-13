"""A service component typically refers to a software component that provides specific functionality or 
features to other parts of a software system or to external systems. It can be an integral part of a 
larger application or system architecture, providing services such as data processing, communication, 
or business logic.
For a service component descriptor, you would typically include information about the service's name, 
description, endpoints (if applicable), methods or operations provided by the service, parameters or 
inputs required for each method, and any additional metadata that describes its behavior or usage.

Here's an example of what a service component descriptor might include:

{
    "Type": "Descriptor_Service",
    "Name": "Data Processing Service",
    "Description": "Provides data processing capabilities for analyzing and transforming data.",
    "Endpoint": "http://example.com/data-processing",
    "Methods": {
        "GET": "Retrieve data from the service.",
        "POST": "Submit data for processing.",
        "PUT": "Update existing data.",
        "DELETE": "Delete data from the service."
    },
    "Parameters": {
        "Input_Data": "The data to be processed.",
        "Options": "Optional parameters for customizing the processing."
    }
}

"""

import json

class Descriptor_Service:
    def __init__(self, name, description, endpoint, methods, parameters):
        self.type = "Descriptor_Service"
        self.name = name
        self.description = description
        self.endpoint = endpoint
        self.methods = methods
        self.parameters = parameters
    
    def get_descriptor_dict(self):
        descriptor = {
            "Type": self.type,
            "Name": self.name,
            "Description": self.description,
            "Endpoint": self.endpoint,
            "Methods": self.methods,
            "Parameters": self.parameters
        }
        return descriptor
    
    def get_descriptor(self):
        return (json.dumps(self.get_descriptor_dict(), indent=4))


def test():
    # Example usage:
    service_descriptor = Descriptor_Service(
        name="Data Processing Service",
        description="Provides data processing capabilities for analyzing and transforming data.",
        endpoint="http://example.com/data-processing",
        methods={
            "GET": "Retrieve data from the service.",
            "POST": "Submit data for processing.",
            "PUT": "Update existing data.",
            "DELETE": "Delete data from the service."
        },
        parameters={
            "Input_Data": "The data to be processed.",
            "Options": "Optional parameters for customizing the processing."
        }
    )

    print (service_descriptor.get_descriptor())


if __name__ == "__main__":
    test()


