from setuptools import setup, find_packages

setup(
    name='complex',
    author='Jason Myers',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click==3.3',
    ],
    description='A description',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    entry_points='''
    [console_scripts]
    complex=complex.command:cli
    '''
)
