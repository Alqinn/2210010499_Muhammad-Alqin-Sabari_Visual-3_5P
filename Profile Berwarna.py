import PySimpleGUI as sg
sg.theme("Black")
sg.theme_text_color("#F5F5DC")
windos = sg.Window('Profile Berwarna', 
    [[sg.Text('NPM :2210010499'),],
        [sg.Text('Nama :Muhammad Alqin Sabari')], 
        [sg.Text('kelas :5P reguler Banjarmasin')],
        [sg.Text('matkul : pempgraman Visual')],
    ],size=(500,200)).read(close=True)
event, values=window.read()
window.close()