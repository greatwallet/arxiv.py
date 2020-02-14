from setuptools import setup

version = "0.5.1-cxt"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="arxiv",
    version=version,
    packages=["arxiv"],

    # dependencies
    install_requires=[
        'feedparser',
        'requests',
        'pytest-runner',
        'tqdm'
    ],
    tests_require=[
        "pytest",
    ],
    # metadata for upload to PyPI
    author="Xiaotian Cheng",
    author_email="cxt_tsinghua@126.com",
    description="Python wrapper for the arXiv API: http://arxiv.org/help/api/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="arxiv api wrapper academic journals papers",
    url="",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
