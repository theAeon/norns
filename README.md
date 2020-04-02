# norns

[![bioconda-badge](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io)
[![PyPI version](https://badge.fury.io/py/norns.svg)](https://badge.fury.io/py/norns)

Simple yaml-based config module.

## Installation

Via conda:

```
$ conda install norns
```

or via pip:

```
$ pip install norns
```

## Usage
Create a config file in the user condig directory
```
import norns

# yaml template
dflt = "/path/to/default.yaml"
config = norns.config("filename", default=dflt)
```

Read and update a config file
```
# read
config.keys()

>>> dict_keys(['phone_numbers', 'launch_codes', 'birthdays'])

# alter
launch_codes = config.get("launch_codes", [])
launch_codes.append(1234)

# update
config["launch_codes"] = launch_codes
config.save()
```

## Contributing

Contributions welcome! Send me a pull request or get in [touch](simon.vanheeringen@gmail.com).

## License

This module is licensed under the terms of the [MIT license](https://opensource.org/licenses/MIT).
