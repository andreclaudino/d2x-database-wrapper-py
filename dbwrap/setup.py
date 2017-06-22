from setuptools import setup

setup(
    name='dbwrap',
    packages=['dbwrap'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'neo4j-driver',
        'neomodel'
    ],
)
