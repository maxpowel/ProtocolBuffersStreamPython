from distutils.core import setup
setup(
    name='protocol_buffers_stream',
    packages=['.'],
    version='1.0',
    description='Send and receive protocol buffers objects easily',
    author='Alvaro Garcia Gomez',
    author_email='maxpowel@gmail.com',
    url='https://github.com/maxpowel/ProtocolBuffersStreamPython',
    download_url='https://github.com/maxpowel/ProtocolBuffersStreamPython/archive/master.zip',
    keywords=['config', 'configuration', 'yml', 'json'],
    classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System', 'Topic :: Utilities'],
    install_requires=['protobuf3', 'pyserial']
)
