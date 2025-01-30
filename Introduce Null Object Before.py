class Device:
    def __init__(self, device_name):
        self.device_name = device_name

def device(device_object):
    print(device_object.device_name)

device_object_1 = Device("Computer")
device(device_object_1)