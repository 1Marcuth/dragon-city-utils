from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as file:
    readme_content = file.read()

setup(
    name = "dragon-city-utils",
    version = "2.0.0",
    license = "MIT License",
    author = "Marcuth",
    long_description = readme_content,
    long_description_content_type = "text/markdown",
    author_email = "example@gmail.com",
    keywords = "dragoncity dcutils tools",
    description = "Dragon City Utils, uma coleção de ferramentas e utilitários para gerenciar ativos estáticos e realizar cálculos relacionados ao jogo Dragon City.",
    packages = ["dcutils"] + [ "dcutils/" + x for x in find_packages("dcutils") ]
)