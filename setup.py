from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as file:
    readme_content = file.read()

setup(
    name = "dragon-city-utils",
    version = "2.1.0",
    license = "MIT License",
    author = "Marcuth",
    long_description = readme_content,
    long_description_content_type = "text/markdown",
    author_email = "example@gmail.com",
    keywords = "dragoncity dcutils tools",
    description = "Dragon City Utils, a collection of tools and utilities for managing static assets and performing calculations related to the Dragon City game.",
    packages = ["dcutils"] + [ "dcutils/" + x for x in find_packages("dcutils") ]
)