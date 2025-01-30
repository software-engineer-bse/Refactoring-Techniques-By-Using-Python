class Device:
    def __init__(self, device_name):
        self.device_name = device_name

class Null_Device:
    def __init__(self):
        self.device_name = "Unknown"


def device(device_object):
    if device_object is None:
        device_object = Null_Device()
    print(device_object.device_name)

device_object_1 = None
device(device_object_1)