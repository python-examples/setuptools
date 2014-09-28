
from setuptools import setup
setup(
    name='mymodule',
    packages=['mymodule'],
    entry_points={
        'console_scripts' : [
            'mycommand = mymodule.script:main',
        ]
    },
    install_requires=[
        'requests',
    ]
)