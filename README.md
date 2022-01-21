# Missing Fundamentals

Additional line of information text about what the project does. Your introduction should be around 2 or 3 sentences. Don't go overboard, people won't read it.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed the latest version of [Audacity](https://www.audacityteam.org/download/)

Before you run this program, follow these steps:
1. Ensure mod-script-pipe is downloaded in Audacity (follow this [Link](https://manual.audacityteam.org/man/scripting.html) and look at the "Enable mod-script-pipe" section)
2. If you don't have a python enviroment, make sure to install it first (in the terminal)
```
python3 -m venv local_python_environment
```
3. Run te requirments for the software (in the terminal):
```
pip install -r requirements.txt
```

## Running the Program

To run the program:
1. Have Audacity Running 
2. Run this in your terminal (at the location of the the pipe_test.py file):
```
<python pipe_test.py>
```
3. Input the name for the project 
4. Input the amount of signal tests
5. For each signal input:
    * Number of Frequencies 
    * The Hz for each of the frequencies 
    * The duration of the signal (seconds)
    * _Remember it is 6 signals per test (REF,Hidden_REF,and 4 more signals)_
6. After running the scripts, the program will ask you confirmation to save (type in anything)
   * In audacity a window will pop up to configure where to save. Go to the TestFiles folder and click save. You will only have to do this once.
7. After finishing inputting all your files, you will get a summary of the signals and an ASI file in the asi_files folder

## Contact

If you want to contact me for any help you can reach me at nagaredd@usc.edu.
