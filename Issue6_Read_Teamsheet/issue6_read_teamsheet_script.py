# Script to specifically handle pyduck #6

# Imports
import string
# import os

# print(os.getcwd())

def issue6_read_teamsheet(teamsheet_file_name):

    with open(teamsheet_file_name, 'r') as f:
        # Acceptance criteria 1:  print number of lines in file
        # printing lines is simple and doesn't need a separate function
        lines = f.readlines()
        num_lines = len(lines)
        print("Acceptance Criteria 1, num lines: " + str(num_lines), end="\n\n")

        # Acceptance criteria 2:  print the last line
        print("Acceptance Criteria 2, last line: " + str(lines[num_lines-1]), end="\n\n")
        
        # Acceptance criteria 3:  print the line that contains Pokemon
        # print(lines[10])
        print("Acceptance Criteria 3, Pokemon lines: ", end="\n")
        print_line_after_blank_line(lines)
        print("\n")

def print_line_after_blank_line(lines):
    num_lines = len(lines)
    i = 0
    while i < num_lines:
        if i == 0:
            line_no_newline = lines[i].rstrip()
            print(line_no_newline)
        if lines[i] == "\n":
            line_no_newline = lines[i+1].rstrip()
            print(line_no_newline)
        i=i+1

# For whatever reason I need to reference the current directory
f_name = "Issue6_Read_Teamsheet/test.txt"
issue6_read_teamsheet(f_name)