import PySimpleGUI as Sg
from zip_creator import unzipper

Sg.theme("DarkBlue")

archive_label = Sg.Text("Select Archive: ")
archive_input = Sg.Input()
archive_button = Sg.FileBrowse("Choose", key="archive")

folder_label = Sg.Text("Select destination directory: ")
folder_input = Sg.Input()
folder_button = Sg.FolderBrowse("Choose", key="folder")

un_zip_btn = Sg.Button("Unzip")
output_label = Sg.Text("", key="output")

first_column = [
    [archive_label], [folder_label]
]
second_column = [
    [archive_input, archive_button], [folder_input, folder_button]
]

layout = [
    [Sg.Column(first_column), Sg.Column(second_column)],
    [un_zip_btn, output_label]
]

window = Sg.Window("Unzipper", layout=layout)

while True:
    event, values = window.read()

    try:
        archive_path = values["archive"]
        to_folder_path = values["folder"]

        unzipper(archive_path=archive_path, to_folder_path=to_folder_path)
        window["output"].update(value="Extraction Completed!", text_color="green")

    except TypeError:
        window["output"].update(value="Please select the destination!", text_color="red")
    except FileNotFoundError:
        window["output"].update(value="Please select the destination of folders!", text_color="red")
    except:
        window["output"].update(value="Unrecognized error!", text_color="red")

    if event in (Sg.WIN_CLOSED, 'Exit'):
        break

window.close()
