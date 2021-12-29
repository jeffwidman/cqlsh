from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="cqlsh",
    install_requires=[
        "cassandra-driver",
        "six",
    ],
)
