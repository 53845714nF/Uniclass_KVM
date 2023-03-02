from setuptools import setup

with open("Readme.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="uniclass",
    version="1.0.0",
    description="Tool to switch on UDP-TA2-4K KVM Switch,",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sebastian",
    author_email="hackwiki2.0@gmail.com",
    license="MIT License",
    packages=['uniclass'],
    package_dir={'uniclass': 'uniclass/'},
    install_requires=[
        'pyusb'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux"
    ],
    entry_points={
        'console_scripts': [
            'uniclass = uniclass.uniclass:main'
        ]
    },
)
