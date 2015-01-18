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

## Support options


```bash

--all        Include directory entries whose names begin with a dot (.).
--long       List in long format.
--time       sort by modification time.
--changed    with --long --time: sort by, and show, ctime with --long: show
             ctime and  sort  by  name otherwise: sort by ctime
--accessed   with --long --time: sort by, and show, atime with --long: show
             atime and  sort  by  name otherwise: sort by atime
--reverse    reverse order while sorting
--size       sort by file size
--recursive  list subdirectories recursively
--human      with -l, print sizes in human readable format (e.g., 1K 234M
             2G)
--help       Show this message and exit.

```
