
# Zip Manager GUI

Zip Manager GUI is a Python-based application that provides a graphical interface for creating and extracting zip files. This project was developed as a learning exercise, inspired by Ardit Sulce’s [Python Mega Course](https://www.udemy.com/course/the-python-mega-course/). Using PySimpleGUI, it allows users to select files for zipping or unzipping with an easy-to-use interface.

## Project Overview

This project includes three main Python scripts:

1. **to_zip.py**: Provides a GUI for selecting files to compress and specifying the destination for the zip file. Users can easily create zip files from their chosen files and location.
2. **from_zip.py**: Provides a GUI for selecting a `.zip` file and the destination directory, allowing users to extract files to a specified location.
3. **zip_creator.py**: A helper script that handles the core zip and unzip functionality using Python’s `zipfile` and `pathlib` libraries.

## Features

- **Create Zip Files**: Select files and compress them into a zip file at the chosen destination.
- **Extract Zip Files**: Choose a zip file to extract and specify the extraction destination.
- **User-Friendly GUI**: Built with PySimpleGUI, the interface simplifies the process of zipping and unzipping files.

## Technologies Used

- **Python**: Core language used for the project.
- **PySimpleGUI**: Used to create a graphical interface.
- **zipfile** and **pathlib** libraries: Used for handling file compression and extraction.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/otuemre/ZipManagerGUI.git
   ```
2. **Install Requirements**:
   Make sure to install `PySimpleGUI`:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Scripts**:
   - **To create a zip file**: Run `to_zip.py`.
   - **To extract a zip file**: Run `from_zip.py`.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

This project was inspired by the [Python Mega Course](https://www.udemy.com/course/the-python-mega-course/) by Ardit Sulce. Special thanks to Ardit Sulce for the educational resources that guided the development of this project.