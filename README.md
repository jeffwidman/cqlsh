# `cqlsh`

`cqlsh` is a Python-based command-line client for running `CQL` commands on a `cassandra` cluster.

Normally it's packaged as part of the full Apache Cassandra™ installation. This repo repackages it into a standalone Python package for lighter-weight installs.

### Installing:

Install and update using [`pip`](https://pip.pypa.io/en/stable/quickstart/):
```
$ pip install -U cqlsh
```

### Running:

```
$ cqlsh --help
```

### Documentation:

Documentation is available as part of the official [Apache Cassandra™ documentation](https://cassandra.apache.org/doc/latest/tools/cqlsh.html).

### Contributing:

Because this is a repackaging of `cqlsh` from the official [Cassandra repo](https://gitbox.apache.org/repos/asf/cassandra.git), **only issues / PRs related to PyPI packaging should be opened against this repo**. If you would like to contribute to `cqlsh` itself, [find out more information here](http://wiki.apache.org/cassandra/HowToContribute).
