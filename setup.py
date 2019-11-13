import setuptools

setuptools.setup(
    name="ecwalletsdk",
    version="0.0.1",
    author="Mudit Marda",
    author_email="muditmarda109@gmail.com",
    description="EC wallet client sdk",
    long_description="A python micro-library of ECDSA functions for generation of keypairs, signing and verification.",
    long_description_content_type="text/markdown",
    url="https://github.com/vaultbank/python-ec-client-sdk",
    packages=["ec_wallet"],
    install_requires=[
        "fastecdsa==1.7.5",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)