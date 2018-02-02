from setuptools import find_packages, setup
import re

def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']

setup(
    name='sptygenre',
    version=get_version('sptygenre/__init__.py'),
    description='Draws wordclouds for genres in spotify playlists',
    url='https://github.com/sublinus/sptygenre',
    author='Gabriel Sailer',
    author_email='sublinus@riseup.net',
    license='MIT',
    packages=find_packages(),
    python_requires='>= 2.7',
    install_requires=[
        'matplotlib >= 2.1.1',
        'setuptools',
        'spotipy >= 2.4.4',
        'wordcloud >= 1.3.1'
    ],
    test_requires=['pytest', 'mock'],
    entry_points={
        'console_scripts': [
            'sptygenre = sptygenre.__main__:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Sound/Audio :: Analysis', 
        'Topic :: Scientific/Engineering :: Information Analysis',
    ]
    )