# Problem Sorter
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## General Info
- **Runs on:** Linux/Windows/MacOS 
- **Tools:** sqlite3, conda, python3, tkinter

## Description
Problem Sorter is a small app whose purpose is to store and index files by theme. Although it works for any type of file, the app's original purpose was to store files containing exam problems/exercises. 

## Usage

To launch the app through python:

    python3 src/main.py 
or

    python src/main.py

To launch the app through the bash script:

    ./run.sh
    
This must be made in an environment containing the required libraries.

## Download
You can find and download a packaged version of this app for multiple OS's [here](https://github.com/marhcouto/problem-sorter-exe)


## Instructions

- You can search for exercises/exams containing exercises that associate with the themes you selected on the theme list by pressing the 'Search' button. If no theme is selected, the search will retrieve all file paths registered in the database. When multiple themes are selected, the files presented are the ones which associate with at least one of the themes.
- You can add new themes by entering their name in the left entry box and pressing the 'Add theme' button. Eliminating them is done by selecting from the theme list the themes you desired to remove and hitting the 'Remove theme' button.
- Adding new file paths to the system is done in a similar manner, but you are required to select the themes you want to associate with the file prior to clicking the 'Add problem' button. For one file, multiple themes can be selected.
- If you want to associate a file with one or more new themes, just type the name of the file and proceed as you would to add a new file.
- Reset buttons serve to reset the menu to its initial state, deleting the results of a search for example.


