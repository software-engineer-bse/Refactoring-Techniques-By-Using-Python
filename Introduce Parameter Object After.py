class Device:
    def __init__(self, device_name, device_type):
        self.device_name = device_name
        self.device_type = device_type


def device(device_object):
    return f"Device name is {device_object.device_name} and type is {device_object.device_type}"

device_object = Device("computer", "laptop")

x = device(device_object)
print(x)