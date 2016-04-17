# jsonlike [![Build Status](https://travis-ci.org/shaunvxc/jsonlike.svg?branch=master)](https://travis-ci.org/shaunvxc/jsonlike) [![PyPI version](https://badge.fury.io/py/jsonlike.svg)](https://badge.fury.io/py/jsonlike)
###Why?
Sometimes, especially when working with `JSON` data from the web, you will find that the data format is not quite JSON and thus have to do a little bit of fighting with it in order to successfully call `json.loads()`.  

The goal of this package is to expose & abstract the oft-used functionality required to do this.

###Usage
```python
import jsonlike
jsonlike.loads(invalid_json_string)
```

Currently, `jsonlike.loads` will
* strip out bad escape characters
* strip out HTML content with JSON values
* add missing commas
* correct errors due to nested `"`'s

##### Strip response callback wrappers
```python
import jsonlike
jsonlike.unwrap_and_load("callback({"a": ""hello""})") # yields {"a":"hello"}
```
For JSON surrounded by a callback wrapper, calling `unwrap_and_load` will use the `unwrapper` library to strip away the callback, before returning `loads()` on the remaining content.

###Installation
`$ pip install jsonlike`

## Contributing
1. Fork it ( https://github.com/shaunvxc/envy/fork )
1. Create your feature branch (`git checkout -b new-feature`)
1. Commit your changes (`git commit -am 'Add some feature'`)
1. Run the tests (`make test`)
1. Push change to the branch (`git push origin new-feature`)
1. Create a Pull Request

