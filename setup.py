from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bijoy_to_unicode_file_converter',
    version='1.1',
    description='Convert your Bijoy text file to unicode text file easily.',
    py_modules=["converter"],
    package_dir={'':'bijoy_to_unicode_file_converter'},
    long_description = long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: Freely Distributable",
    ],
    install_requires = [
        "langdetect ~= 1.0.9",
        "six ~= 1.16.0",
    ],
    url = "https://github.com/almehady/Bijoy-to-Unicode-File-Converter",
    author="Al Mehady",
    author_email="almehady@gmail.com",
    project_urls={
        'Source': 'https://github.com/almehady/Bijoy-to-Unicode-File-Converter',
    },


)


