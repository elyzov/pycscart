# pycscart

This is a Python library for interacting with [CS-Cart shopping cart](https://www.cs-cart.com) via [REST API](http://docs.cs-cart.com/4.3.x/developer_guide/api).

#### Compatibility

Compatible with CS-Cart 4.0.0 or newer. Older versions are not implemented because of no APIs in these releases.

Keep in mind, that some methods could work only for a specific release. For example, you cannot have list of vendors on CS-Cart just as you cannot have a list of storefronts on Multi-Vendor installation. 

If you find a something is broken, please submit an issue. Don't forget to
specify a version of CS-Cart and what kind of error do you have.

## Installation

#### From PyPi (recommended)
```bash
pip install pycscart
```

#### From GitHub
```bash
pip install -e git+git@github.com:gongled/pycscart.git#egg=pycscart
```

#### From source
```bash
git clone git@github.com:gongled/pycscart
python pycscart/setup.py install
```

## Documentation

API documentation is [here](https://gongled.github.io/pycscart).

Or you can build the documentation yourself:
```bash
pip install sphinx
pip install sphinx_rtd_theme
cd docs/
make html
```

The documentation will be in `gh-pages/html`:
```bash
open gh-pages/html/index.html
```

## Basic Usage

Create a `CSCartClient()` instance pointing at your CS-Cart store:
```python
>>> from pycscart import CSCartClient
>>> c = CSCartClient('http://example.com', 'admin@example.com', '2560VIl10GKpc3Hc7CNjB96U4HIW6299')
```

Then try calling some methods:
```python
>>> c.list_products()
[CSCartProduct::{}, CSCartProduct::{}, ...]
```

## License

Open source under the MIT License. See [LICENSE](LICENSE).
