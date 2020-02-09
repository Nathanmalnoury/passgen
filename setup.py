import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="passutil",  # Replace with your own username
    version="0.0.1",
    author="Nathan Malnoury",
    author_email="n.malnoury@gmail.com",
    description="A basic password manager / password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nathanmalnoury/passgen",
    packages=setuptools.find_packages(),
    install_requires=[
        "click",
        "cryptography",
        "pyperclip",
    ],
    include_package_data=True,
    data_files=[('passutil/data', ['passutil/data/conf_passgen.ini', 'passutil/data/passgen_files.json'])],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
    ],
    python_requires='>=3.7',
)
