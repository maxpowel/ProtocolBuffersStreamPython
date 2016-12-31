Protocol Buffers Stream for python
==================================
How to install
---------------
pip install protocol_buffers_stream

What is this?
-------------
A helper tool for send and receive easily protocol buffers objects.
Used with [library](https://github.com/maxpowel/ProtocolBuffersStream) for arduino communication

Why?
-----
Nowadays the communication between machines is very common. This is not an
easy task but the libraries handle this, at least for most common cases.

For example everyone knows JSON. In python you only have to create a 
dictionary and serialize it with one function. Also, you receive a string
an build the dictionary with other function. So easy. But what about
for protocol buffers? There is not a simple way like that but this is the
objective of this library

Motivation
----------
This library was designed and made an easy way to communicate IOT devices.
These devices are usually low consumption, low memory and slow cpu. This is
the reason why we can't use JSON (for example), because JSON requires a high
amount of memory (1kb of memory is nothing for a home computer, but it is a
very big amount of memory for this IOT devices). The alternative is
use a binary format.

When using a binary format, other problems appears. For example, some devices
 uses 8bit integer, others 16bit even 32bit. Someone uses little endian while
 others use big endian. This is not a problem when all devices are the same
 but my intention is not to be worried about that. I don't want to know who is
 in the other side of the wire. This is why I like protocol buffers. All this
 huge complexity disappears, and it is handled by an efficient way.
 
Another thing is the transmission channel. The TCP/IP stack that we are use to work with
is wonderful, but too heavy for this little devices. In the other hand, all of these
devices has serial ports and because we use a binary format, we don't need a big bandwidth so serial port is nice.
Other advantage is that serial port can be used (transparently for us) for short distances (RS232)
 or large distances (RS485). This is why this library use a serial port.

If you like arduino, I also made the [library](https://github.com/maxpowel/ProtocolBuffersStream) for that.

How to use
----------
The first step is define your proto model and compile it (using the protocol buffers library for python).
Check (https://developers.google.com/protocol-buffers/) if you dont know what I'm talking about.

Sending data:

```python
messenger = ProtocolBuffersStream(port, baudrate)
message = MyProtocolBuffersObject()
message.name = "Foo"
message.value = 69
message.send(message)
```

Receiving data
```python
messenger = ProtocolBuffersStream(port, baudrate)
message = MyProtocolBuffersObject()
message.receive(message)
print(message.name)
print(message.value)
```
