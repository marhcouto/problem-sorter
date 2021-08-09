# Problem Sorter
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## General Info
- **Environments:** Linux/Windows 
- **Tools:** sqlite3, conda, python3

## Description
Problem Sorter is a small app whose purpose is to store and index files by theme. Although it works for any type of file, the app's original purpose was to store files containing exam problems/exercises. 

## Usage

To launch the app:

    python3 src/main.py 
or

    python src/main.py
    
This must be made in an environment containing the required libraries.


## Instructions

- In the search menu, you can search for exercises/exams containing exercises that associate with the themes you chose, followed by lookup of the file or elimination of its registry.
- Looking up a file means launching the default application assigned by the system to open files of such format.
- When multiple themes are selected, the files presented are the ones which associate with at least one of the themes.
- When no themes are selected, all files' paths will be displayed.
- In the insertion menu, you can insert new entries in the database, filling in the fields with the corresponding info. For one file, multiple themes can be inserted.
- When a theme no longer has files associated to it, it will be automatically eliminated.
- For insertions, if new files are selected, they will be inserted; if the chosen file already exists, its themes will be updated; same goes for themes.
- Reset buttons serve to reset the current menu to its initial state, deleting the results of a search.

