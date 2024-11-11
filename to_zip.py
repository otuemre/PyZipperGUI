import PySimpleGUI as Sg
import zip_creator as zc

label1 = Sg.Text("Select files to compress: ")
input1 = Sg.Input(key="input1")
choose_button1 = Sg.FilesBrowse("Choose", key="file_paths")

label2 = Sg.Text("Select destination folder: ")
input2 = Sg.Input(key="input2")
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

compress_button = Sg.Button("Compress")
exit_button = Sg.Button("Exit")

success_msg = Sg.Text(key="msg")

layout = [
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [compress_button, exit_button, success_msg]
]

window = Sg.Window("Zip File Creator", layout=layout)

while True:
    event, value = window.read()
    files = value["file_paths"].split(";")
    to_folder = value["folder"]

    match event:
        case "Compress":
            zc.create_archive(file_paths=files, to_folder_path=to_folder)
            window["input1"].update(value="")
            window["input2"].update(value="")
            window["msg"].update(value="Compression completed successfully!")

        case Sg.WIN_CLOSED | "Exit":
            break

window.close()
