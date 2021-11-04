import PySimpleGUI as sg
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
layout =    [[sg.Input(key='FILE', enable_events=True, visible=True)],
            [sg.FileBrowse(target='FILE')],
            [sg.Text('Start', size=(15, 1)), sg.InputText()],
            [sg.Text('End', size=(15, 1)), sg.InputText()],
            [sg.OK('OK')]]

window = sg.Window('Select', layout, size=(200, 200))

while True:
    event, values = window.Read()
    if event == "OK":
        filename = os.path.basename(values['FILE'])
        split_tup = os.path.splitext(filename)
        file_extension = split_tup[1]
        a = int(values[0])
        b = int(values[1])
        ffmpeg_extract_subclip(values['FILE'], a*60, b*60, filename+'-'+values[0]+'to'+values[1]+"-TRIM"+file_extension)
