from setuptools import setup
MAJOR = 0
MINOR = 2
MICRO = 3
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

with open('README.md') as readme:
    readme_lines = readme.readlines()

description = readme_lines[2].strip()
try:
    import pandoc
    doc = pandoc.Document()
    doc.markdown = ''.join(readme_lines)
    long_description = doc.rst.replace(r'\_\_', '__')
except ImportError:
    long_description = ''.join(readme_lines)

setup(
    name="mutablerecords",
    packages=["mutablerecords"],
    description=description,
    long_description=long_description,
    version=VERSION,
    license='Apache 2.0',
    author='Fahrzin Hemmati',
    author_email='fahhem@chainreactionmfg.com',
    url='https://github.com/chainreactionmfg/mutablerecords',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ]
)
