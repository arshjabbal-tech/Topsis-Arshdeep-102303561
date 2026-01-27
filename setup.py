# setup.py

import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
  long_description=README,
  long_description_content_type='text/markdown',
  name = 'Topsis-Arshdeep-102303561',       
  version = '1.1.1',     
  license='MIT',     
  url='https://github.com/arshjabbal-tech/Topsis-Arshdeep-102303561.git',
  description='A Python package to find TOPSIS for MCDM (Multi-Criteria Decision Analysis Method)',
  author = 'Arshdeep Kaur',
  author_email = 'arshdeep11380@gmail.com',      
  keywords = ['TOPSIS', 'MCDM'],   
  install_requires=[            
          'numpy',
          'pandas',
          'logging',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
  ],
  packages=find_packages(),
  include_package_data=True,
  entry_points={
    'console_scripts': [
      'topsis-arshdeep=topsis_arshdeep.main:main',
    ],
  },
)