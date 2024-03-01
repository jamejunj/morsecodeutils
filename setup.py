import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "morseutils",
    version = "0.0.4",
    author = "Jirakit Jirapongwanich",
    author_email = "jame.jpwn@gmail.com",
    description = "A morsecode translator and player package. \nIt can translate a message to morse code and play the morse code as sound. \nThe player is only support on Windows",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/jamejunj/morsecodeutils",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)