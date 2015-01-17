# lspy

implement unix `ls` command in python

## Usage

```python
$ lspy --help
Usage: lspy [OPTIONS] [PATH]

Options:
  --all   Include directory entries whose names beginwith a dot (.).
  --long  List in long format.
  ...
  --help  Show this message and exit.

$ lspy --long .
drwxr-xr-x me staff 510 1 18 03:20 lspy
-rw-r--r-- me staff 22 1 15 14:42 pytest.ini
-rw-r--r-- me staff 558 1 15 16:17 setup.py
drwxr-xr-x me staff 340 1 18 03:13 tests
```
