Game of Life Viewer
==================

This is a simple game of life viewer.
It was written in Python using Tk as the graphical user interface toolkit.

The viewer keeps reading from a text file with the grid. Every time the content of the file changes the grid is automatically updated.

Usage
-----

### General usage:

```
 $ ./gol-viewer.py
```

It will read from a file named 'input.txt' in the same directory.

### Changing the input file name:

```
 $ ./gol-viewer.py -f anotherName.in
```

It will read from a file name 'anotherName.in' in the same directory.
Note here that the file extension can be anything, as long as the content of the file is a standard ASCII text.

### Changing the location of the input file:

```
 $ ./gol-viewer.py -f ../upperDirectory/world.txt
```

```
 $ ./gol-viewer.py -f /tmp/game-of-life/output/anything.txt
```

Note that it is possible to use a relative or absolute path, but the file name is mandatory.

### Changing the grid size

```
 $ ./gol-viewer.py -r 100 -c 100
```

It will create a grid with 100 rows and 100 columns.
By default if no value is given the grid will have 10 rows and 10 columns.

### General Help:

```
 $ ./gol-viewer.py -h
```

Input File Format
-----------------

Currently the viewer supports ASCII text file.
The representation of a cell in the worls is a single char that can be either a 0 or a 1 for a live cell.

- [ ] Add support for '.' and '*' as in the original kata
