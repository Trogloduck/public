< [[Python]]

`pip install`: installing something from https://pypi.org/

/!\\ careful what package I install: it can run code as soon as it is installed 
and there is **no moderation on pypi.org**!

Every package has a "setup.py" file that runs as soon as we run the `pip install the_package` command

Check content of setup.py: download and examine it in VSCode (no `pip install`)

### Create and import homemade packages

1. Write `my_function()` in `my_module.py`
2. Save `my_module.py` in folder `my_packages`
3. Save empty `__init__.py` in `my_packages
4. In main script, `from my_packages.my_module import my_function`
