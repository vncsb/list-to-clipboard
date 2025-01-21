# What is this software?

list-to-clipboard (or l2c) is a simple python program which purpose is to make it easy to search and copy some value based on a list, it comes from my experience from doing pentest related work and always be struggling copying and pasting things around, so I just wanted to store these values in a file and have them easily accessible to my clipboard. This is not a clipboard manager.

l2c uses [rofi](https://github.com/davatorium/rofi) to show your list and allow filtering and selecting.

## Features

- List files history
- Add entry and select other files directly on rofi
- Browse history (TODO)
- Edit and delete entries (TODO)
- Pass list via stdin (TODO)
- Use as library (TODO)

## Installation

For now just clone this repo, go to its root and install it locally with pip, example: 

```bash
pip install .
``` 

Example with uv:

```bash
uv tool install .
```

Remember that you need to have [rofi](https://github.com/davatorium/rofi) installed and available in your path and that the application will be available as `l2c` in your terminal! 

## Usage

When parsing a file, `l2c` expects an entry per line and a separator to indicate which part is the value to be copied and which is the description, the default separator is `|||`, so an example file could look like this:

```
value to be copied|||description
value1|||description that will be filtered as well
```

So when parsing a file you can do:
```bash
 l2c -f your_file
```

If you just want to open the last file you parsed:
```bash
l2c
```

If there is no file in the history the rofi filebrowser will be used so that you can select a file in the filesystem.
