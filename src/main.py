#!/usr/bin/env python
import sys
import PySimpleGUI as sg
import merge
import assay_editor

sg.set_options(auto_size_buttons=True, font='Any 12')
sg.ChangeLookAndFeel('Dark')

layout = [
    [sg.T('What do you want to do?')],
    [sg.B('Customize Assay', key='Customize'), sg.B('Merge Assays', key='Merge')]]
window = sg.Window('SPIRO Assay Customizer', layout=layout)

event, values = window.read()

if event == 'Customize':
    window.close()
    assay_editor.start_editor()
elif event == 'Merge':
    window.close()
    merge.start_merge()
