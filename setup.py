import setuptools
from pip._internal.req import parse_requirements
from pip._internal.network.session import PipSession


install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.requirement) for ir in install_reqs]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
print(setuptools.find_packages())

setuptools.setup(
    name="TFMultiImage",
    version="1.0.2",
    author="Noupin",
    author_email="author@example.com",
    description="Package for easy image conversion.",
    install_requires=reqs,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Noupin/TFMultiImage",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    py_modules=setuptools.find_packages(),   
)