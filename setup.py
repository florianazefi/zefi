from setuptools import setup, find_packages

setup(
    name="zefi",
    version="0.1",
    description="Floriana's Python package for data science",
    long_description="",
    url="http://github.com/florianazefi/zefi-package",
    author="Floriana Zefi",
    author_email="florianagjzefi@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=[
        "numpy",
        "sklearn"
    ],
)
