import os
import sys
from prettytable import PrettyTable
from ahk import AHK

if sys.platform == 'win32':
    print("pipe-test.py, running on windows")
    TONAME = '\\\\.\\pipe\\ToSrvPipe'
    FROMNAME = '\\\\.\\pipe\\FromSrvPipe'
    EOL = '\r\n\0'
else:
    print("pipe-test.py, running on linux or mac")
    TONAME = '/tmp/audacity_script_pipe.to.' + str(os.getuid())
    FROMNAME = '/tmp/audacity_script_pipe.from.' + str(os.getuid())
    EOL = '\n'

print("Write to  \"" + TONAME + "\"")
if not os.path.exists(TONAME):
    print(" ..does not exist.  Ensure Audacity is running with mod-script-pipe.")
    sys.exit()

print("Read from \"" + FROMNAME + "\"")
if not os.path.exists(FROMNAME):
    print(" ..does not exist.  Ensure Audacity is running with mod-script-pipe.")
    sys.exit()

print("-- Both pipes exist.  Good.")

TOFILE = open(TONAME, 'w')
print("-- File to write to has been opened")
FROMFILE = open(FROMNAME, 'rt')
print("-- File to read from has now been opened too\r\n")


def send_command(command):
    """Send a single command."""
    print("Send: >>> \n" + command)
    TOFILE.write(command + EOL)
    TOFILE.flush()


def get_response():
    """Return the command response."""
    result = ''
    line = ''
    while True:
        result += line
        line = FROMFILE.readline()
        if line == '\n' and len(result) > 0:
            break
    return result


def do_command(command):
    """Send one command, and return the response."""
    send_command(command)
    response = get_response()
    print("Rcvd: <<< \n" + response)
    return response


def quick_test():
    """Example list of commands."""
    do_command('Help: Command=Help')
    do_command('Help: Command="GetInfo"')
    # do_command('SetPreference: Name=GUI/Theme Value=classic Reload=1')


def missing_fundamental(file_name, freq_list, duration):
    do_command("New:")
    for w in freq_list:
        tone = "Tone: Frequency={}".format(w)
        duration1 = "SelectTime: Start=0 End={}".format(duration)
        do_command("NewMonoTrack:")
        do_command(duration1)
        do_command(tone)
    do_command("SelectAll:")

    file_name1 = "ExportWav: {}".format(file_name)
    send_command(file_name1)
    print("--------------------------------------------------------------------")


def close_page():
    do_command()


def asi_file(test_name, missing_fundamental_list, signal_count):
    if os.path.exists(test_name):
        print("File already exists")
    else:
        asi = ".asi"
        test_name_asi = test_name + asi
        targetPath = os.getcwd() + "\\asi_files"
        completeName = os.path.join(targetPath, test_name_asi)
        file = open(completeName, "x")
        file.write("session=MUSHRA" + '\n')
        mul = 0
        signal_count = 2
        for num in range(1, signal_count + 1):
            file.write("# TestSignal{}".format(num) + '\n')
            # signal_file = iter(missing_fundamental_list)
            for t in range(1):
                file.write("./Originals/{}.wav REF".format(missing_fundamental_list[mul]) + '\n')
                file.write("./Originals/{}.wav Hidden_REF".format(missing_fundamental_list[mul + 1]) + '\n')
                file.write("./TestFiles/{}.wav Sys1".format(missing_fundamental_list[mul + 2]) + '\n')
                file.write("./TestFiles/{}.wav Sys2".format(missing_fundamental_list[mul + 3]) + '\n')
                file.write("./TestFiles/{}.wav Sys3".format(missing_fundamental_list[mul + 4]) + '\n')
                file.write("./TestFiles/{}.wav Sys4".format(missing_fundamental_list[mul + 5]) + '\n')
                mul += 6
        file.close()


if __name__ == '__main__':
    ahk = AHK()
    # mf_list = []
    f_list = []
    file_name_list = []
    file_freq_list = []
    file_signal_test_list = []
    file_duration_list = []
    # file_count_list = []
    t_name = input("What is the name of the test?: ")
    sig_count = input("How many Signal Tests would you like?: ")
    sig_count = int(sig_count)
    og_sig_count = sig_count
    opposite_sig_count = 1
    file_count = 0
    file_cap = 0
    while sig_count > 0:
        repeat = "Y"
        file_cap = 0
        while repeat == "Y" or repeat == "y" and file_cap < 6:
            file_cap = file_cap + 1
            print("--------------------------------------------------------------------{}".format(file_cap))
            f_name = input("File Name (Signal Test {}): ".format(opposite_sig_count))
            file_count = file_count + 1
            file_name_list.append(f_name)
            file_signal_test_list.append(opposite_sig_count)
            num_freq = input("How many frequencies will you have?: ")
            num_freq = int(num_freq)
            file_freq_list.append(num_freq)
            for i in range(1, num_freq + 1):
                freq = input("Frequency {}: ".format(i))
                f_list.append(freq)
            dt = input("Duration: ")
            file_duration_list.append(str(dt))
            missing_fundamental(f_name, f_list, dt)
            # mf_list.append(f_name)
            confirmation = input("Confirmation -> Type Anything: ")
            print("--------------------------------------------------------------------")
            script = 'ControlSetText, Edit1, {}, ahk_class #32770'.format(f_name)
            script2 = 'ControlClick, &Save, ahk_class #32770'
            ahk.run_script(script)
            ahk.run_script(script2)
            if file_cap < 6:
                repeat = input(
                    "Would you like to submit another file for Signal Test {}? (Y/N): ".format(opposite_sig_count))
            else:
                "File Limit Reached"
        # file_count_list.append(file_count)
        sig_count = sig_count - 1
        opposite_sig_count = opposite_sig_count + 1
    # Table
    dataTable = PrettyTable()
    dataTable.field_names = ["File Name", "Signal Test", "# of Frequencies", "Duration"]
    for count in range(file_count):
        dataTable.add_row([file_name_list[count], file_signal_test_list[count], file_freq_list[count],
                           file_duration_list[count]])
    print("--------------------------------------------------------")
    print("Summary of Files Made:")
    print("Number of Signal Tests: {}".format(og_sig_count))
    print(dataTable)
    print("--------------------------------------------------------")
    asi_file(t_name, file_name_list, sig_count)
