import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arqweb-concept-queue",
    version="0.0.1",
    author="El Famoso Grupo 7",
    author_email="noggaxiii@gmail.com",
    description="Work for web architectures FCEN UBA 2020",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Trekkar/web-shifts-Server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)