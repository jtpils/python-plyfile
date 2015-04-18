import os

from setuptools import setup

mydir = os.path.dirname(__file__)
if mydir:
    os.chdir(mydir)

version = '0.4'
base_url = 'https://github.com/dranjan/python-plyfile'

setup(name='plyfile',
      author='Darsh Ranjan',
      version=version,
      install_requires=['numpy>=1.8'],
      description='PLY file reader/writer',
      url=base_url,
      download_url=('%s/releases/tag/v%s' % (base_url, version)),
      license='GPLv3+',
      classifiers=[
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: OS Independent',
          'Development Status :: 4 - Beta',
          'Topic :: Scientific/Engineering'
      ],
      py_modules=['plyfile'],
      keywords=['ply', 'numpy'])
