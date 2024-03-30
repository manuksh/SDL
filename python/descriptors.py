import os
import json

def test():
    service = Descriptor_Service(
        name='Service TCP',
        description='Description of the service component.',
        endpoint='URL or endpoint of the service.',
        methods={
            'GET': 'Retrieve data from the service.',
            'POST': 'Submit data to the service.',
            'PUT': 'Update existing data in the service.',
            'DELETE': 'Delete data from the service.'
        }
    )
        
    print(service.get_descriptor())  





#######################################################
## Abstract Descriptor Class 
class Descriptor_Abstract:
    def __init__(self, name, description):
        self.type = self.__class__.__name__  # Set type to the class name
        self.data = {
                    'Name':name, 
                    'Description': description
                    }


    def get_data(self):
        reVal = {'Type': self.type, **self.data}
        return reVal
    
    def get_descriptor(self):
        return json.dumps(self.get_data(), indent=4)
    

#######################################################
## Descriptor_Class
class Descriptor_Class(Descriptor_Abstract):
    def __init__(self, name, description, members=None, methods=None):
        super().__init__(name, description) # Call the parent class constructor
        self.data = {
            'Members' : members,
            'Methods' : methods
        }

# Create an instance of Descriptor_Class
CLASS = Descriptor_Class(
    name='Valve of the process1',
    description='Describes the valve in the context of the river flow control.',
    members=[
        {'state': 'boolean, Open|Close'},
        {'Flag': 'value2'}
    ],
    methods=[
        {'open': 'Open the valve and set state=Open'},
        {'close': 'Close the Valve and set the state=Close'},
        {'getState': 'get state value of the valve'}
    ]
)

#######################################################
## Descriptor_Service
class Descriptor_Service(Descriptor_Abstract):
    type = "Service"
    def __init__(self, name, description, endpoint, methods):
        super().__init__(name, description) # Call the parent class constructor
        self.data['Endpoint'] = endpoint
        self.data['Methods']=methods
        
#######################################################
## Descriptor_Service
class Descriptor_Control(Descriptor_Abstract):
    def __init__(self, name, description, Functions, Parameters):
        super().__init__(name, description) # Call the parent class constructor
        self.data['Functions'] = Functions
        self.data['Parameters'] = Parameters



SERVICE = Descriptor_Service(
    name='Logging and Monitoring Services',
    description= """After logging, collect all operation which is done by the user.
    User can selelc products but do not complete transaction, theis nee dto be logged.
    User can complete the transaction, this need to be logged.
    """,
    endpoint='URL or endpoint of the service.',
    methods={
        'GET': 'Retrieve data from the service.',
        'POST': 'Submit data to the service.',
        'PUT': 'Update existing data in the service.',
        'DELETE': 'Delete data from the service.'
    }
)
#######################################################
## Descriptor_Utility
class Descriptor_Utility(Descriptor_Abstract):
    def __init__(self, name, description, usage):
        super().__init__(name, description) # Call the parent class constructor
        self.data['Usage'] = usage


UTILITY = Descriptor_Utility(
    name="File Utility",
    description="Utility for file management operations.",
    usage="Used for reading, writing, and manipulating files."
)

#######################################################
## Descriptor_Listener
class Descriptor_Listener(Descriptor_Abstract):
    def __init__(self, name, description, event_type, source, target):
        super().__init__(name, description) # Call the parent class constructor
        self.data={
                'Event_Type': event_type,
                'Source': source,
                'Target': target
                }
 
# Instantiate Descriptor_Listener
LISTENER = Descriptor_Listener(
    name='Example Listener',
    description='Description of the example listener.',
    event_type='Type of the event',
    source='Source of the event',
    target='Target of the event'
)

#######################################################
## Descriptor_Event
class Descriptor_Event(Descriptor_Abstract):
    def __init__(self, name, description, event_type, source, target, data):
        super().__init__(name, description) # Call the parent class constructor
        self.data={
                'Event_Type': event_type,
                'Source': source,
                'Target': target,
                'Data': data
                }

EVENT = Descriptor_Event(
    name='Interrupt Event',
    description='Description of the example event.',
    event_type='Type of the event',
    source='Source of the event',
    target='Target of the event',
    data={'key1': 'value1', 'key2': 'value2'}  # Data associated with the event
)


#######################################################
## Descriptor_Module
class Descriptor_Module(Descriptor_Abstract):
    def __init__(self, name, description, dependencies, functions):
        super().__init__(name, description)  # Call the parent class constructor
        self.data = {
            "Dependencies": dependencies,
            "Functions": functions
        }


# Example instantiation of Descriptor_Module
MODULE = Descriptor_Module(
    name="Data Processing Module",
    description="Module for processing data received from sensors.",
    dependencies=["numpy", "pandas"],
    functions=[
        {
            "name": "process_data",
            "description": "Function to process raw sensor data.",
            "parameters": {
                "input_data": "Raw sensor data to be processed.",
                "options": "Optional parameters for customizing the processing."
            },
            "return_type": "dict"
        },
        {
            "name": "analyze_data",
            "description": "Function to analyze processed data.",
            "parameters": {
                "processed_data": "Data processed by the process_data function.",
                "options": "Optional parameters for customizing the analysis."
            },
            "return_type": "dict"
        }
    ]
)

#######################################################
## Descriptor_Function
class Descriptor_Function(Descriptor_Abstract):
    def __init__(self, name, description, parameters, return_type):
        super().__init__(name, description)
        self.data = {
            "Parameters": parameters,
            "Return_Type": return_type
        }

FUNCTION = Descriptor_Function(
        name="Process Data",
        description="Calculate furier fast transform from input data",
        return_type="dict",
        parameters={
            "inout_atr": "string, input from sensors",
            "options": "Optional parameters for customizing the processing"
        }
        
    )


#######################################################
## Descriptor_Function
class Descriptor_Interface(Descriptor_Abstract):
    def __init__(self, name, description, methods):
        super().__init__(name, description)  # Call the parent class constructor
        self.data["Methods"] = methods

# Example instantiation
INTERFACE = Descriptor_Interface(
    name="Data Processor Interface",
    description="Interface for processing data with various methods.",
    methods={
        "process_data": "Method to process input data.",
        "analyze_data": "Method to analyze processed data.",
        "visualize_data": "Method to visualize data."
    }
)
################################################################
#descriptor = event.generate_descriptor()
#print(descriptor)

def test():
    print(CLASS.get_descriptor())
    print(SERVICE.get_descriptor())
    print(UTILITY.get_descriptor())
    print(LISTENER.get_descriptor())
    print(EVENT.get_descriptor())
    print(MODULE.get_descriptor())
    print(FUNCTION.get_descriptor())
    print(INTERFACE.get_descriptor())


if __name__ == '__main__':
    test()
