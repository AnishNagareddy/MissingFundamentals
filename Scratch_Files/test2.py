import ahk
from ahk import AHK, Hotkey
from ahk.window import Window

if __name__ == '__main__':
    ahk = AHK()
    file_name = input("Enter File Name: ")
    script = 'ControlSetText, Edit1, {}, ahk_class #32770'.format(file_name)
    script2 = 'ControlClick, &Save, ahk_class #32770'
    ahk.run_script(script)
    ahk.run_script(script2)
