#######################################################
## Descriptor_Service
class Descriptor_Control(Descriptor_Abstract):
    def __init__(self, name, description, Functions, Parameters):
        super().__init__(name, description) # Call the parent class constructor
        self.data['Functions'] = Functions
        self.data['Parameters'] = Parameters
