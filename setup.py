from setuptools import setup, find_packages

setup(
    name='tog',
    version='1.0.0',
    description='Basic terms of genetics.',
    long_description=open('README.md').read().strip(),
    url='http://www.github.com/gisk-rev/tog.git',
    author='Marco Campani',
    author_email='m.campani85@gmail.com',
    packages=find_packages(),
    install_requires=['pandas'],
    keywords=['python', 'bioinformatics', 'genetics'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bioinformatics',
        'Programming Language :: Python :: 3.13',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
