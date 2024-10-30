# 0x01. Caching

## Background Context
In this project, you will learn about different caching algorithms.

## Resources
Read or watch:
- [Cache replacement policies - FIFO](#)
- [Cache replacement policies - LIFO](#)
- [Cache replacement policies - LRU](#)
- [Cache replacement policies - MRU](#)
- [Cache replacement policies - LFU](#)

## Learning Objectives
By the end of this project, you should be able to explain to anyone, without external help:

### General
- What a caching system is
- What FIFO (First In, First Out) means
- What LIFO (Last In, First Out) means
- What LRU (Least Recently Used) means
- What MRU (Most Recently Used) means
- What LFU (Least Frequently Used) means
- The purpose of a caching system
- The limitations of a caching system

## Requirements

### Python Scripts
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should follow the pycodestyle style (version 2.5).
- All files must be executable.
- The length of files will be tested using `wc`.
- All modules must have documentation (e.g., `python3 -c 'print(__import__("my_module").__doc__)'`).
- All classes must have documentation (e.g., `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All functions, inside and outside of classes, must have documentation (e.g., `python3 -c 'print(__import__("my_module").my_function.__doc__)'`).

### Documentation
Documentation should provide a meaningful description of the module, class, or method. Each piece of documentation must be a full sentence explaining the purpose of the component.

## More Info

### Parent Class: BaseCaching
All your caching classes must inherit from the `BaseCaching` class, as defined below:

```python
$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

In this project, you will implement caching algorithms by extending the `BaseCaching` class and defining `put` and `get` methods according to the caching policies.
