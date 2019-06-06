import os
import re
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='mbfbiolucidaclient',
    version=find_version('src', 'mbf', '__init__.py'),
    packages=[''],
    package_dir={'': 'src'},
    url='https://github.com/hsorby/mbfbiolucidaclient',
    license='Apache Software License',
    author='Hugh Sorby',
    author_email='h.sorby@auckland.ac.nz',
    description='Simple client for the MBF Biolucida API.'
)
