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

This PyPI package is maintained by [Jeff Widman](https://github.com/jeffwidman). Previous maintainers: [Spiro](https://github.com/spiside) and [Andrew Mussey](https://github.com/amussey).


### Changelog:

Unfortunately the Cassandra project does not always increment the `cqlsh` version number, so for every
release we need to document not only the `cqlsh` version but also the `cassandra` version in which it
shipped.

#### 6.0.0b4 (Mar 9, 2022)

This packages `cqlsh` `5.0.1` from [Cassandra 4.0-beta4](https://github.com/apache/cassandra/blob/cassandra-4.0-beta4/bin/cqlsh.py):
* Now supports Python 3.
* Although this is pulled from a Cassandra `4.x` release, it should generally work against Cassandra `3.x` clusters without needing to set any flags. Upcoming releases will need to set the `--cqlversion` flag when talking with clusters < `4.0` due to this [commit](https://github.com/apache/cassandra/commit/c9d6c725dd0b4aa5693eb1c6d2221c28e9e99c6e#diff-9e4fe0cfd28004625a8006be8a0bdeab8cbdfb039449fb9501b15e8952577aaaL479). See also [CASSANDRA-16508](https://issues.apache.org/jira/browse/CASSANDRA-16508).

#### 5.0.5 (Mar 9, 2022)

This packages `cqlsh` `5.0.1` from [Cassandra 3.11.10](https://github.com/apache/cassandra/blob/cassandra-3.11.10/bin/cqlsh.py).

#### 5.0.4 (Mar 29, 2017)

This packages `cqlsh` `5.0.1` from [Cassandra 3.4.0](https://github.com/apache/cassandra/blob/cassandra-3.4/bin/cqlsh.py).


#### 5.0.3 (Mar 21, 2016)

This packages `cqlsh` `5.0.1` from [Cassandra 2.2.0](https://github.com/apache/cassandra/blob/cassandra-2.2.0/bin/cqlsh.py).


#### 4.1.1 (Feb 11, 2014)

This packages `cqlsh` `4.1.1` from [Cassandra 2.0.5](https://github.com/apache/cassandra/blob/cassandra-2.0.5/bin/cqlsh).


#### 4.1.0 (Dec 2, 2013)

This packages `cqlsh` `4.1.0` from [Cassandra 2.0.3](https://github.com/apache/cassandra/blob/cassandra-2.0.3/bin/cqlsh).


#### 4.0.1 (Oct 14, 2013)

This packages `cqlsh` `4.0.1` from [Cassandra 2.0.1](https://github.com/apache/cassandra/blob/cassandra-2.0.1/bin/cqlsh).
