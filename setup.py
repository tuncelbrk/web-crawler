import os
import setuptools

version = '0.0.1'
annotated_version = os.getenv('IMAGE_TAG_PUSH')

setuptools.setup(
    name="",
    version=annotated_version,
    author="",
    author_email="",
    description="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[]
)
