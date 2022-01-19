from setuptools import setup

VERSION = '0.1'

DESCRIPTION = 'fexception is designed to provide cleaner useable exceptions.'
LONG_DESCRIPTION = 'fexception takes a traditional exception message and allows wrapped formatting with extra output details.'

# Setting up
setup(

    name="fexception",
    version=VERSION,
    author="IncognitoCoding",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=['fexception'],
    package_dir={'': 'src'},
    url='https://github.com/IncognitoCoding/fexception.git',
    license='MIT',
    install_requires=[
        "setuptools>=49.2.1",
    ],
    keywords=['python'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
    ],
    zip_safe=False

)
