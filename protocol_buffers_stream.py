import serial
import struct


class ProtocolBuffersStream(object):
    def __init__(self, port='/dev/ttyUSB0', baudrate=115200):
        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate
        )

    ''' Send the size of the payload followed by the payload. Data object is simply the protocol buffers object'''
    def send(self, data_object):
        data = data_object.encode_to_bytes()
        size = len(data)
        self.ser.write(struct.pack("B", size))
        self.ser.write(data)

    ''' First receive the payload size, then read this amount of bytes and build the object. Data object is the protocol
     buffers object to populate. You should the type of object that you are going to receive'''
    def receive(self, data_object):
        response_size = struct.unpack("B", self.ser.read())
        data_object.parse_from_bytes(self.ser.read(response_size[0]))

    ''' Just close the serial connection '''
    def close(self):
        self.ser.close()