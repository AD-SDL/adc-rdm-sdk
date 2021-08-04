from setuptools import setup, find_packages
with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'adc',
    version = '0.0.1',
    author = 'Gonzalo Martinez',
    author_email = 'gonzalo.martinez@domandtom.com',
    license = 'Argonne License',
    description = 'This tool allows us to interact with the ADC API',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/AD-SDL/adc-rdm-sdk',
    py_modules = ['adc', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        adc-auth=adc:authtoken
        adc-me=adc:me
        adc-user=adc:user
    '''
)