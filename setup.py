from setuptools import setup

with open("README.md", "r") as file:
    readme_content = file.read()

setup(
    name="encurtanet",
    version="1.0",
    license="MIT License",
    author="Marcuth",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author_email="marcuth2006@gmail.com",
    keywords="dragoncity dcutils tools",
    description=f"Utilities and tools for things related to Dragon City",
    packages=["encurtanet"],
    install_requires=["httpx", "pydantic", "python-filter"],
)