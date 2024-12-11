import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hex-skeleton-domain",  # Replace with your actual package name
    version="0.0.1",  # Start with a version number
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(
        exclude=("tests",)
    ),  # Finds all packages within your project, exclude the tests directory so they are not included in distribution
    install_requires=[
        # List your project's dependencies here
        # Example: "Flask==2.2.2",
    ],  # This is important for dependency management
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or your preferred license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Specify your supported Python versions
    test_suite="tests",  # For running tests via setup.py
)
