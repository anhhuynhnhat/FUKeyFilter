FILE_NAME = "Input.txt"  # Input file name
OUTPUT_FILE_NAME = "Output.txt"  # Output file name

DELIMETER_INPUT = "|"  # Separation between questions and answers in input file
DELIMETER_OUTPUT = DELIMETER_INPUT  # Separation between questions and answers in output file
KEYBANK = {}
WRONG_FORMAT = "This file is wrong format"
CORRECT_FORMAT = "FU KEY FILTER\n--- Correct format ---\n--- Start processing ---"

"""
Add questions to the dictionary
"""

def add_to_dictionary(mode, key, value):
    if (mode == 1):
        KEYBANK[key] = value
    elif (mode == 2):
        KEYBANK[value] = key


"""
Burn data to line by line
"""

def write_data(mode):
    if (mode == 1):
        with open(OUTPUT_FILE_NAME, 'w') as f:
            for key, value in KEYBANK.items():
                f.write("%s%s%s\n" % (key, DELIMETER_OUTPUT, value))
    elif (mode == 2):
        with open(OUTPUT_FILE_NAME, 'w') as f:
            for key, value in KEYBANK.items():
                f.write("%s%s%s\n" % (key, DELIMETER_OUTPUT, value))


"""
Call function after selecting the format of the question. 
The add_to_dictionary function uses the mode parameter to invert the Key and Value characters in the dictionary
"""

def handle_each_sentence(mode):
    allQuestionCounter = 1
    realQuestionCounter = 0
    duplicateQuestionCounter = 0
    result = -1

    with open(FILE_NAME) as fp:
        line = fp.readline().rstrip()

        while line:
            key, value = line.split(DELIMETER_INPUT)

            if (key in KEYBANK):
                duplicateQuestionCounter += 1
            else:
                add_to_dictionary(mode, key, value)
                realQuestionCounter += 1
            line = fp.readline().rstrip()
            allQuestionCounter += 1
            result = 1
    return result


"""
Read each line from the file,
Count the number of occurrences of the question
Check with the question already exists in the question bank
"""

def handling(mode):
    result = -1
    if (mode == 1):
        result = handle_each_sentence(mode)

    elif (mode == 2):
        result = handle_each_sentence(mode)

    return result


"""
Check the format of the file
Each question must be in one line and delimiter between the question and the answer.
"""

def check_format_of_key_file():
    with open(FILE_NAME) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if (line.find(DELIMETER_INPUT) == -1):
                return -1
            line = fp.readline()
            cnt += 1
        return cnt


"""
Show the message to the screen
Depending on the status code
1 is wrong format
2 is properly formatted and
3 begins processing of complete and statistical reports
"""

def show_result_to_screen(status):
    if (status is 0):
        print(WRONG_FORMAT)
    elif (status is 1):
        print(CORRECT_FORMAT)
    elif (status is 2):
        # print("Statistics of converted lines: {}/{}\nOutput path: {}\nFinish - Exit program".format())
        print("Finish")
    elif (status is 3):
        print("You only get 1 or 2")


"""
Select mode. 
1 is <question> | <answer> 
2 is <answer> | <question>
Equivalent to position 1 | 2
"""

def choose_mode():
    choose = -1
    try:
        choose = int(input("FORMAT: 1|2\nSo, in your key file. Question is 1 or 2\nYour choice: "))
        return choose
    except ValueError:
        return choose


"""
After selecting the mode, this function handles the question and answer that the user has selected. 
Consistent with the format of the input file
"""

def processed_according_to_selected_mode(fileStatus, mode):
    if (fileStatus == -1):
        show_result_to_screen(0)

    else:
        show_result_to_screen(1)

        while True:
            result = handling(mode)
            if (result == 1):
                show_result_to_screen(2)
                write_data(mode)
                break


"""
The center of the program, used to call function functions
First, the file format check function is called
Push the message out to the screen
Start processing and writing data to the file
"""

def fu_filter_key_center():
    fileStatus = check_format_of_key_file()
    mode = choose_mode()

    if (mode == 1):
        processed_according_to_selected_mode(fileStatus, mode)

    elif (mode == 2):
        processed_according_to_selected_mode(fileStatus, mode)
    else:
        show_result_to_screen(3)


if __name__ == '__main__':
    fu_filter_key_center()
