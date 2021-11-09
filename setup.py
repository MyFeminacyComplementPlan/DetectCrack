import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="detect_crack",
    version="0.1.0",
    author="MyFeminacyComplmentPlan",
    author_email="myfeminacycomplementplan@gmail.com",
    description="Detect cracks on the road, roof or buildings (beta).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MyFeminacyComplementPlan/DetectCrack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['detect_crack = DetectCrack.detect_crack:detect_crack']
    },
    python_requires='>=3.7',
)

