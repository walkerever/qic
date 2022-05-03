import pathlib
from setuptools import setup,find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="qic",
    version="1.1.15",
    description="data(JSON/XML/YAML) command line query tools with interactive mode.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/laowangv5/qic",
    author="Yonghang Wang",
    author_email="wyhang@gmail.com",
    license="Apache 2",
    classifiers=["License :: OSI Approved :: Apache Software License"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[ "wcwidth", "pyyaml", "xmltodict", "dicttoxml", "pygments", "prompt_toolkit","json_to_html" ],
    keywords=[ "json","yaml","xml","query","jq", "dq", "dsq", "dsquery","qic", "dataquery", "json query", "xml query", "yaml query", "jello", "jq", ],
    entry_points={ "console_scripts": 
        [ 
            "qic=qic:dsq_main", 
        ] 
    },
)
