# deepshuffle.py

A simple but powerful tool to shift letters between the whole ascii range.

* This tool will not work for caesar cipher or ROT13.

## Examples

We have a unknown text string: `§¤««®¶®±«£I`

```bash
$ echo -n "§¤««®¶®±«£I" | ./deepshuffle.py
-64 - gdkknvnqkc	
-63 - helloworld
-62 - ifmmpxpsme
```

We can see at -63 offset, the secret message is "helloworld".         


## Usage

```bash
./deepshuffle.py --help
usage: deepshuffle.py [-h] [--raw] [--get GET] [FILE [FILE ...]]

positional arguments:
  FILE               Read from file. Default STDIN

optional arguments:
  -h, --help         show this help message and exit
  --raw, -r          Print raw data
  --get GET, -g GET  Print a specific shift
```

## Install

* Python2
