from descriptors.descriptor_class import Descriptor_Class
from descriptors.descriptor_service import Descriptor_Service
from descriptors.descriptor_listener import Descriptor_Listener
t={}
valvclass=Descriptor_Class()
valvclass.Name="Valve"
valvclass.Description="Represents a valve used in a process control system."
valvclass.Inheritance="Component"  
valvclass.add_attribute("state", "bool", "Represents the current state of the valve (Open or Close).", "False", "private")  
valvclass.add_attribute("Flag", "str", "Additional flag for the valve.", "None", "protected")
valvclass.add_method("open", "Opens the valve and sets state to Open.", [], "None", "public")
valvclass.add_method("close", "Closes the valve and sets state to Close.", [], "None", "public")
valvclass.add_method("getState", "Returns the current state of the valve.", [], "bool", "public")   
print(valvclass.get_descriptor())

l=Descriptor_Listener()
l.