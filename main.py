import unittest


def log_method_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


# Decorator for mocking hardware interactions during testing
def mock_hardware(func):
    def wrapper(*args, **kwargs):
        # Implement mock behavior here
        # For example, return predefined values or raise exceptions as needed
        return func(*args, **kwargs)

    return wrapper


class MockupUVSensor:
    def __init__(self):
        self.connected = False

    @log_method_calls
    @mock_hardware
    def connect(self):
        # Simulate hardware connection logic
        self.connected = True

    @log_method_calls
    @mock_hardware
    def disconnect(self):
        # Simulate hardware disconnection logic
        self.connected = False

    @log_method_calls
    @mock_hardware
    def send_data(self, data):
        if not self.connected:
            raise RuntimeError("Not connected to hardware")
        # Simulate sending data to mockup hardware
        return f"Sent: {data}"


class TestMockupHardware(unittest.TestCase):
    @mock_hardware
    def test_connect(self):
        hardware = MockupUVSensor()
        hardware.connect()
        self.assertTrue(hardware.connected)

    @mock_hardware
    def test_disconnect(self):
        hardware = MockupUVSensor()
        hardware.connect()
        hardware.disconnect()
        self.assertFalse(hardware.connected)

    @mock_hardware
    def test_send_data(self):
        hardware = MockupUVSensor()
        hardware.connect()
        result = hardware.send_data("Hello, hardware")
        self.assertEqual(result, "Sent: Hello, hardware")


if __name__ == '__main__':
    unittest.main()
