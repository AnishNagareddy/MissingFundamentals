import os
import sys

from prettytable import PrettyTable


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
            # missing_fundamental(f_name, f_list, dt)
            # mf_list.append(f_name)
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
