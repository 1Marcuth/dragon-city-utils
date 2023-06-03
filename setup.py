from setuptools import setup, find_packages

with open("README.md", "r") as file:
    readme_content = file.read()

# with open(
#     "requirements.txt",
#     mode="r",
#     encoding="UTF-16"
# ) as file:
#     requirements = [ line.split("==")[0].strip() for line in file.readlines() ]

requirements = ['anyio', 'bleach', 'certifi', 'charset-normalizer', 'docutils', 'h11', 'httpcore', 'httpx', 'idna', 'importlib-metadata', 'jaraco.classes', 'keyring', 'markdown-it-py', 'mdurl', 'more-itertools', 'pkginfo', 'pydantic', 'Pygments', 'python-filter', 'pywin32-ctypes', 'readme-renderer', 'requests', 'requests-toolbelt', 'rfc3986', 'rich', 'six', 'sniffio', 'twine', 'typing_extensions', 'urllib3', 'webencodings', 'zipp']

setup(
    name="dragon-city-utils",
    version="1.24",
    license="MIT License",
    author="Marcuth",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author_email="marcuth2006@gmail.com",
    keywords="dragoncity dcutils tools",
    description=f"Utilities and tools for things related to Dragon City",
    packages=["dcutils"] + [ "dcutils/" + x for x in find_packages("dcutils") ],
    install_requires=requirements
)