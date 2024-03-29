from setuptools import setup, find_packages

setup(
    name = 'yaxl',
    version = '0.0.18',
    description = 'Yet Another (Pythonic) XML Library',
    long_description = """A library for reading, writing and manipulating XML in Python.
    
* Requires only Python 2.4+
* Learnable in 15 minutes
* Simplest interface possible - minimal number of functions (1) and objects (1) exported
* XML Namespace aware
* XPath support
* Easy to create XML documents and fragments
* Easy to read in and manipulate XML documents and fragments
    """,
    author = 'Iain Lowe',
    author_email = 'yaxl@ilowe.net',
    url = 'http://www.googlecode.com/p/yaxl',
    license = 'MIT License',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',       
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML'
    ],
    packages = find_packages(),
    keywords = 'xml xpath',
    test_suite = 'yaxl._unittests',
    zip_safe = False
)
