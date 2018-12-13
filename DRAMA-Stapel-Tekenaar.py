#from graphics import GraphicsWindow

# I apologize for the lack of documentation, I was still a foolish, novice programmer when I wrote this code.

# ----------
# Notation:
# Entry is an Assignment Table with more information.
# sf means stack frame, it includes all the data necessary to write a stack frame.
# sf differs from a set of Assignment Tables in that and sf needs more information: counter/title.
# ----------

# ----------
# Data Structures:
# sf_list = [ sf = [counter, title, entry = [ title, data = ("PAR"|"VAR"|"RES"), table = [...] ], more entries...],
#                   more sf...]
# stack = stack = [ sf = [counter, title, par_entry = [flag, memory_cell = [offset, name], more memory_cell...],
#                         var_entry, res_entry], more sf... ]
# ----------

# The next functions generate things.


# This function downloads the manual to the folder in which the user has saved the program.
def manual():
    filename = "DRAMA Stapel Tekenaar ManualL"
    outfile = open('%s.txt' % filename, 'w+')
    print("*********************************", file=outfile)
    print("Welcome to DRAMA Stapel Tekenaar!", file=outfile)
    print("*********************************", file=outfile)
    print("by Mathijs Hubrechtsen", file=outfile)
    print("", file=outfile)
    print("1. Introduction:", file=outfile)
    print("What is the DRAMA Stapel Tekenaar? Well, it is what it's name implies, it draws", end=" ", file=outfile)
    print("Stacks for the DRAMA simulator used in SOCS.", file=outfile)
    print("I made this program so I could hone my skils in python and practice SOCS,", end=" ", file=outfile)
    print("I also thought that maybe some people would like a program like this.", file=outfile)
    print("How does it work you ask? Well first off the user enters a few correct Assignment Tables.", file=outfile)
    print("After the user has done this, they simply ask the program to model what the Stack should look like.",
          file=outfile)
    print("It offers all the basic features you would expect: modifying Tables, visualizing Tables, etc.",
          file=outfile)
    print("The program isn't that complex: ~950 lines of code, but it does offer quite a few nifty features.",
          file=outfile)
    print("Seeing as you're reading this manual right now, you're probably in possession of the program,", end=" ",
          file=outfile)
    print("so why not try it out! ;-)", file=outfile)
    print("Anyways, thank you for using my program and I hope it will be of some use to you!", file=outfile)
    print("", file=outfile)
    print("2. MANUAL:", file=outfile)
    print("The DRAMA Stapel Tekenaar does not have a GUI, instead it uses", end=" ", file=outfile)
    print("a Terminal-esque UI where the user enters commands in", end=" ", file=outfile)
    print("the terminal/input box of Pycharm.", file=outfile)
    print("When the user starts the program he/she will be asked to press enter.", file=outfile)
    print("The user can also enter MANUAL to download the MANUAL you are now reading.", file=outfile)
    print("After pressing enter, they will be asked to enter a Function name.", file=outfile)
    print("This is the name of the first Function you want to create an Assignment Table of.", file=outfile)
    print("     The Input should be a string (bvb.: HelloWorld)", file=outfile)
    print("After entering a name, the user will be prompted to enter PAR or VAR or RES.", file=outfile)
    print("These commands stand for PARameter, VARiable or RESult", end=" ", file=outfile)
    print("the user should enter what kind of Assignment Table he/she wants to make.", file=outfile)
    print("     The Input should be PAR or VAR or RES (bvb. : PAR)", file=outfile)
    print("After entering both the title of the Function and what kind of Table the user wants,", end=" ", file=outfile)
    print("the user will need to enter the amount of elements used in the Table", file=outfile)
    print("     The Input should be an integer number (bvb.: 3)", file=outfile)
    print("After entering all of this information, the user will enter the ui.", file=outfile)
    print("Here they can type HELP or DETAILS for more help on what they can do next", file=outfile)
    print("", file=outfile)
    print("3. Extra Information:", file=outfile)
    print("If you are still running into trouble , want to report a bug, or want to help", end=" ", file=outfile)
    print("me improve the DRAMA Stapel Tekenaar, ", end=" ", file=outfile)
    print("do not hesitate to contact me on github!", file=outfile)
    print("Finally I would like to thank you again for using my program,", end=" ", file=outfile)
    print("     -Mathijs Hubrechtsen", file=outfile)
    print("", file=outfile)
    print("*********************************", file=outfile)
    outfile.close()


def gen_std():
    sf_list = [[1, 'Test1', ['Test1', 'PAR', [["PARA3", '1(R8)'], ["PARA2", '2(R8)'], ["PARA1", '3(R8)'], ]],
               ['Test1', 'VAR', [["VARA1", '-4(R8)'], ["VARA2", '-3(R8)'], ["VARA3", '-2(R8)']]],
               ['Test1', 'RES', [["RES1", '4(R8)']]]],
               [2, 'Test2', ['Test2', 'PAR', [["PARA3", '1(R8)'], ["PARA2", '2(R8)'], ["PARA1", '3(R8)'], ]],
               ['Test2', 'VAR', [["VARA1", '-4(R8)'], ["VARA2", '-2(R8)']]],
               ['Test2', 'RES', [["RES1", '4(R8)']]]]]
    return sf_list


def create_entry(title, data, table):
    entry = list()
    entry.append(title)
    entry.append(data)
    entry.append(table)
    return entry


def create_sf(counter, title, table, data):
    sf = list()
    sf.append(counter)
    sf.append(title)
    sf.append(create_entry(title, data, table))
    return sf

# ----------

# These functions save or visualize either the currently selected stack frame
# or all the stack frames of the current session.


def print_current(title, table, data):
    print()
    print("%s:" % title)
    print(data, "|", end=" ")
    print("address")
    for i in range(len(table)):
        for j in range(2):
            if j == 0:
                print(table[i][j], "|", end=" ")
            if j == 1:
                print(table[i][j])
    print()
    return


def print_all(sf_list):
    for sf in sf_list:
        counter = sf[0]
        title = sf[1]
        print("*********************************")
        print("Tables of %i. %s:" % (counter, title))
        entry_list = sf[2: len(sf)]
        for entry in entry_list:
            print_current(title, entry[2], entry[1])
    return


def save_to_file(filename, sf_list):
    outfile = open('%s.txt' % filename, 'w+')
    print("Current Assignment Tables written to %s.txt!" % filename)

    for sf in sf_list:
        counter = sf[0]
        title = sf[1]
        print("*********************************", file=outfile)
        print("Tables of %i. %s:" % (counter, title), file=outfile)
        print("", file=outfile)
        entry_list = sf[2: len(sf)]
        for entry in entry_list:
            data = entry[1]
            table = entry[2]
            print("     ", "%s%s%s" % ("*", data, "*"), "|", end=" ", file=outfile)
            print("*address*", file=outfile)
            for i in range(len(table)):
                for j in range(2):
                    if j == 0:
                        print("     ", table[i][j], "|", end=" ", file=outfile)
                    if j == 1:
                        print(table[i][j], file=outfile)
            print("", file=outfile)
    outfile.close()
    return


def sf_list_graphics(sf_list):
    width_max = 7
    length = 50
    for sf in sf_list:
        entry_list = sf[2: len(sf)]
        for entry in entry_list:
            table = entry[2]
            length += len(table) * 25 + 25
            length += 50
            for i in range(len(table)):
                for j in range(2):
                    string = str(table[i][j])
                    if len(string) > width_max:
                        width_max = len(string)

    width = 2 * (25 + width_max * 10 + 25)
    posy = 50
    win = GraphicsWindow(50 + width + 50, length + 100)
    canvas = win.canvas()

    for sf in sf_list:
        user = sf[2: len(sf)]
        for entry in user:
            canvas.setTextAnchor("nw")
            canvas.drawText(50, posy - 20, " %s-%s:" % (entry[0], entry[1]))
            table = entry[2]

            height = len(table) * 25 + 25
            canvas.drawRect(50, posy, width, height)
            canvas.drawLine(50 + width / 2, posy, 50 + width / 2, posy + height)

            canvas.setTextAnchor("center")
            for j in range(2):
                if j == 0:
                    canvas.drawText(50 + width / 4 + j * (width / 2), posy + 12.5, "*" + entry[1] + "*")
                else:
                    canvas.drawText(50 + width / 4 + j * (width / 2), posy + 12.5, "*address*")
            posy += 25
            canvas.drawLine(50, posy, 50 + width, posy)

            for i in range(len(table)):
                for j in range(2):
                    canvas.drawText(50 + width / 4 + j * (width / 2), posy + 12.5, table[i][j])
                posy += 25
                canvas.drawLine(50, posy, 50 + width, posy)
            posy += 50
    win.wait()
    return

# ----------

# The next functions handle drawing ascii stacks.


# Dissect an address to see if it's a valid non-numeric, non-register DRAMA address.
def dissect(address):
    address = str(address)
    try:
        int(address)
    except ValueError:
        if address == "...":
            return False
        if address[0] == "R":
            return False
        token = address.split("(")
        index_register = token[1]
        if index_register[1] != "8":
            return False
        return token[0]

    return False


# stack_entry = final version of an Entry, stack_entry will be used to draw a section of the Stack Frame
# table = the non-final Assignment Table corresponding to the Entry
def update_entry(stack_entry, table):
    for i in range(len(table)):
        # Dissect the address
        string = dissect(table[i][1])
        if string is not False:
            stack_entry.append([string, table[i][0]])
            stack_entry[0] += 1
    return


def make_stack(sf_list):
    stack = []
    for sf in sf_list:
        counter = sf[0]
        title = sf[1]
        entry_list = sf[2: len(sf)]
        par_entry = [0]
        var_entry = [0]
        res_entry = [0]
        for entry in entry_list:
            temp = []
            data = entry[1]
            table = entry[2]
            if data == "PAR":
                update_entry(par_entry, table)
            elif data == "VAR":
                update_entry(var_entry, table)
            elif data == "RES":
                update_entry(res_entry, table)

        temp.append(counter)
        temp.append(title)
        temp.append(par_entry)
        temp.append(var_entry)
        temp.append(res_entry)
        stack.append(temp)
    return stack


def burn_stack(stack, filename):
    outfile = open('%s.txt' % filename, 'w+')
    changed = False
    lowest_address = int

    for sf in stack:
        counter = sf[0]
        title = sf[1]
        entry_list = sf[2: len(sf)]
        print("*********************************", file=outfile)
        print("Stack Frame of %i. %s:" % (counter, title), file=outfile)
        print("", file=outfile)

        # VARIABLES FIRST (START AT TOP OF STACK)
        var = entry_list[1]
        if var[0] != 0:
            # Remove flag
            var = var[1: len(var)]
            # Current is the topmost memory cell of the stack (lowest address)
            current = var[0]
            for memory_cell in var:
                if int(memory_cell[0]) < int(current[0]):
                    current = memory_cell
            var.remove(current)
            print("|%s" % current[1], file=outfile)

            # Write output
            lowest_address = int(current[0])
            while not var == []:
                lowest_address += 1
                current = [lowest_address, ""]
                for memory_cell in var:
                    if int(memory_cell[0]) == int(current[0]):
                        current = memory_cell
                        changed = True
                if changed:
                    var.remove(current)
                    changed = False
                print("|%s" % current[1], file=outfile)

            # Make sure we end at -2(R8)
            while lowest_address < -2:
                current = [lowest_address, ""]
                lowest_address += 1
                print("|%s" % current[1], file=outfile)

        # Mandatory instructions
        current = [-1, "TKA"]
        print("|%s" % current[1], file=outfile)
        current = [-0, "VORIGE R8"]
        print("|%s" % current[1], file=outfile)

        # PARAMETERS NEXT
        # Similar to VARIABLES
        par = entry_list[0]
        if par[0] != 0:
            par = par[1: len(par)]
            current = par[0]
            for memory_cell in par:
                if int(memory_cell[0]) < int(current[0]):
                    current = memory_cell
            par.remove(current)
            print("|%s" % current[1], file=outfile)

            lowest_address = int(current[0])
            while not par == []:
                lowest_address += 1
                current = [lowest_address, ""]
                for memory_cell in par:
                    if int(memory_cell[0]) == int(current[0]):
                        current = memory_cell
                        changed = True
                if changed:
                    par.remove(current)
                    changed = False
                print("|%s" % current[1], file=outfile)

        # RESULTS LAST
        # Similar to VARIABLES
        res = entry_list[2]
        if res[0] != 0:
            res = res[1: len(res)]
            current = res[0]
            for memory_cell in res:
                if int(memory_cell[0]) < int(current[0]):
                    current = memory_cell
            res.remove(current)

            if entry_list[0][0] != 0:
                lowest_address += 1
                while lowest_address < int(current[0]):
                    lowest_address += 1
                    print("", file=outfile)
            print("|%s" % current[1], file=outfile)

            lowest_address = int(current[0])
            while not res == []:
                lowest_address += 1
                current = [lowest_address, ""]
                for memory_cell in res:
                    if int(memory_cell[0]) == int(current[0]):
                        current = memory_cell
                        res.remove(current)
                print("|%s" % current[1], file=outfile)

        print("_", file=outfile)
    outfile.close()
    return


# Adds layout formatting to the stack frame that was written to the given file
def fix_stack_layout(filename):
    # length contains the length of the longest memory cell name
    length = 0
    outfile = open('%s.txt' % filename, 'r')
    for line in outfile:
        if line[0] == "|":
            if len(line) - 1 > length:
                length = len(line) - 1

    outfile.close()
    burn_stack_temp(filename, length)
    return


def burn_stack_temp(filename, length):
    outfile = open('%s.txt' % filename, 'r')
    temp = open('%s.txt' % "temp", 'w+')
    hold = False
    v8 = False
    for line in outfile:
        if line[0] == "|":
            remainder = length - (len(line) - 1)
            spaces = remainder // 2
            string = spaces * " "

            if line[1:len(line) + 1] == "TKA\n":
                hold = True
            elif line[1:len(line) + 1] == "VORIGE R8\n" and hold:
                hold = False
                v8 = True

            if remainder % 2 == 0:
                if v8:
                    print("| %s%s%s |  <-- R8" % (string, line[1: len(line) - 1], string), file=temp)
                    v8 = False
                else:
                    print("| %s%s%s |" % (string, line[1: len(line) - 1], string), file=temp)
                string = (length + 2) * "-"
                print("+%s+" % string, file=temp)

            else:
                user = spaces + 1
                user *= " "
                if v8:
                    print("| %s%s%s |  <-- R8" % (string, line[1: len(line) - 1], user), file=temp)
                    v8 = False
                else:
                    print("| %s%s%s |" % (string, line[1: len(line) - 1], user), file=temp)
                string = (length + 2) * "-"
                print("+%s+" % string, file=temp)

        elif line == "\n":
            string = (length + 2) * "-"
            print("", file=temp)
            print("+%s+" % string, file=temp)

        elif line[0] == "_":
            print("", file=temp)

        else:
            print("%s" % line[0:len(line) - 1], file=temp)

    outfile.close()
    temp.close()
    copy_temp(filename)
    return


# Copies the temporary file to the final file
def copy_temp(filename):
    outfile = open('%s.txt' % filename, 'w+')
    temp = open('%s.txt' % "temp", 'r')

    for line in temp:
        print("%s" % line[0: len(line) - 1], file=outfile)

    outfile.close()
    temp.close()
    clean_temp()
    return


# Cleans the temporary file
def clean_temp():
    temp = open('%s.txt' % "temp", 'w+')
    temp.close()
    return

# ----------

# These functions change the currently selected stack frame.


def make_new(amt):
    table = []
    for i in range(amt):
        row = ["..."] * 2
        table.append(row)
    return table


def add_table(table, data):
    print("ROW is not the programmer's interpretation of row!")
    print("ROW starts with 1!")
    user = int(input("ADD how many new %s? " % data))
    print()
    for i in range(user):
        table.append(["...", "..."])
    print("*This is the new Assignment Table*")


def delete_table(table):
    print("ROW is not the programmer's interpretation of row!")
    print("ROW starts with 1!")
    row = int(input("ROW: "))
    print()
    table.pop(row - 1)
    print("*This is the new Assignment Table*")


def enter_table(title, table, data):
    print("Value means the data that you would like to enter in the current Table cell.")
    print("Type EXIT to EXIT ENTER mode.")
    for i in range(len(table)):
        for j in range(2):
            print_current(title, table, data)
            print()
            if j == 0:
                user = input("Enter Value: ")
            elif j == 1:
                user = valid_input("ENTER", table, i, j)

            if user != "EXIT":
                table[i][j] = user
            else:
                break
        if user == "EXIT":
            break
    print("*This is the new Assignment Table*")


def modify_table(table):
    print("ROW and COLUMN are not the programmer's interpretation of row and column!")
    print("ROW and COLUMN start at 1!")
    row = int(input("ROW: "))
    column = int(input("COLUMN: "))
    if column - 1 == 1:
        user = valid_input("MODIFY", table, row, column)
        table[row - 1][column - 1] = user
    else:
        user = input("NEW VALUE: ")
        table[row - 1][column - 1] = user
    return

# ----------


# These functions check if the input is valid or sort the stack frames of the current session.

# The Difference between check_input and valid_input is that Valid_input only works if called upon to modify
# a specific element in a stack frame entry.
def check_input(mode, value):
    if mode == "DATA":
        data = input("Enter PAR or VAR or RES: ")
        data = data.upper()
        while data != "PAR" and data != "VAR" and data != "RES":
            data = input("Enter PAR or VAR or RES: ")
            data = data.upper()
        return data

    elif mode == "AMOUNT":
        data = value
        amt = input("Amount of %s: " % data)
        test = False
        while test is False:
            test = True
            try:
                int(amt)
            except ValueError:
                print("That's not an int! If you want to enter for example, 3 %s," % data, end=" ")
                print("you would enter the number: 3.")
                test = False

            if test is False:
                amt = input("Amount of %s: " % data)
            else:
                amt = int(amt)
        return amt


def valid_input(mode, table, row, column):
    valid = bool
    if mode == "MODIFY" or mode == "ENTER":
        if mode == "MODIFY":
            user = input("NEW VALUE: ")
            valid = False
        elif mode == "ENTER":
            user = input("Enter value: ")
            user = user.upper()
            if user == "EXIT":
                valid = True
            else:
                valid = False

        check_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        while valid is not True:
            valid = True

            user_test = list(user)
            if "(" not in user_test:
                valid = False

            if valid:
                user_test = user.split("(")
                test = user_test[0]
                try:
                    test = int(test)
                except ValueError:

                    valid = False

                if valid:
                    if -9999 > test or test > 9999:
                        valid = False

                test = user_test[1]
                if test[0] != "R":
                    valid = False
                elif test[1] not in check_set:
                    valid = False
                elif test[2] != ")":
                    valid = False

            try:
                val = int(user)
            except ValueError:
                pass
            else:
                if 0 <= val < 9999:
                    valid = True

            if valid is not True:
                user_test = list(user)
                if len(user_test) == 2:
                    if user_test[0] != "R":
                        valid = False
                    elif user_test[1] not in check_set:
                        valid = False
                    else:
                        valid = True
                else:
                    valid = False

            if valid is not True and mode == "MODIFY":
                print("The input should be a valid DRAMA address!")
                user = valid_input("MODIFY", table, row, column)
            elif valid is not True and mode == "ENTER":
                print("The input should be a valid DRAMA address!")
                user = valid_input("ENTER", table, row, column)
    return user


def check_sf(sf):
    temp = sf[2: len(sf)]
    # Get the entry that was just inserted
    new_entry = temp[-1]
    new_entry_data = new_entry[1]
    # Check if this entry already exists
    for entry_count in range(len(temp) - 1):
        entry = temp[entry_count]
        entry_data = entry[1]
        if entry_data == new_entry_data:
            # +2 because counter and title are still in front.
            sf.pop(entry_count + 2)
            return
    return


def check_after_delete(sf_list, sf):
    if len(sf) == 2:
        sf_list.remove(sf)

        number_expect = 1
        for sf in sf_list:
            if sf[0] != number_expect:
                sf[0] = number_expect
            number_expect += 1
    return

# ----------

# These functions handle sorting.


def get_value(data):
    if data == "PAR":
        return 0
    elif data == "VAR":
        return 1
    else:
        return 2


def sort_sf(sf):
    # Sorting max of 3 elements,
    # Only 1 element
    if len(sf) <= 3:
        return

    for i in range(2, len(sf)):
        # only consider values in unsorted part of the sf
        for j in range(i, len(sf)):
            # sf[i][2] should be lowest value in sf
            if get_value(sf[i][1]) > get_value(sf[j][1]):
                temp = sf[i]
                sf[i] = sf[j]
                sf[j] = temp
    return


def sorted_insert(sf_list, title, data, table):
    sf_counter = 0
    flag = True

    for sf in sf_list:
        if sf[0] > sf_counter:
            sf_counter = sf[0]
        sf_title = sf[1]
        if sf_title == title:
            flag = False
            sf.append(create_entry(title, data, table))
            check_sf(sf)
            sort_sf(sf)
            break

    if flag:
        new_sf = create_sf(sf_counter + 1, title, table, data)
        sf_list.append(new_sf)
    return

# ----------


# This function handles the interface.
def interface(title, data, table, sf_list):
    user = "START"
    while user != "EXIT":
        print()
        print("Enter HELP for list of commands")
        user = input("What do you want to do? ")
        user = user.upper()
        print("COMMAND: ", user)
        print()
        if user == "HELP":
            print("* HELP *")
            print("To enter a command do NOT type the NUMBER of the command but the NAME")
            print("1: ADD")
            print("2: BURN")
            print("3: DELETE")
            print("4: DETAILS")
            print("5: PRINT")
            print("6: ENTER")
            print("7: EXIT")
            print("8: GET")
            print("9: GRAPHICS or G")
            print("10: HELP")
            print("11: LIST or LS")
            print("12: MODIFY")
            print("13: NEW")
            print("14: REMOVE")
            print("15: SAVE or S")
            print("16: STACK or ST")
            print("17: STANDARD or STD")
            print("TYPE DETAILS FOR DETAILS ON ALL COMMANDS")
            input("Press Enter to exit HELP!")
            print()

        elif user == "DETAILS":
            print("* DETAILS: *")
            print("FUNCTION = the Function of which you are making an Allocation Table")
            print("SESSION = all of the Functions made during a single 'session'")
            print()
            print("These Instructions modify the current Allocation Table:")
            print("1: ADD = ADD a specified amount of extra rows to the current Allocation Table.")
            print("3: DELETE = DELETE a specified row.")
            print("6: ENTER = ENTER the Allocation Table, "
                  "this will always enter the Allocation Table at the very first element.")
            print("12: MODIFY =  MODIFY a specified element in the Allocation Table.")
            input("Press Enter to continue")
            print()
            print("These Instructions generate a new or old Function/Allocation Table:")
            print("8: GET = GET an old Function/Allocation Table.")
            print("13: NEW = Create a NEW Function/Allocation Table.")
            print("14: REMOVE = REMOVE an old Function.")
            input("Press Enter to continue")
            print()
            print("These Instructions visualize or save the current Allocation Table::")
            print("5: PRINT = PRINT the current Allocation Table.")
            print("15: SAVE =  SAVE the current Allocation Table.")
            input("Press Enter to continue")
            print()
            print("These Instructions generate sessions:")
            print("17: STANDARD or STD = load the STANDARD preset session ")
            input("Press Enter to continue")
            print()
            print("These Instructions visualize or save the current session")
            print("2: BURN = BURN all the Functions you have saved in the current session to a specified", end=" ")
            print(".txt file, if there is no file with that name, the program will create one.")
            print("2: The program saves this .txt file in the same folder as where the program is located.")
            print("9: GRAPHICS = will GRAPHICally generate the current session with the graphics.py module.")
            print("11: LIST = Will LIST all the Functions you have saved in the current session in the terminal.")
            input("Press Enter to continue")
            print()
            print("These Instructions will perform global actions.")
            print("4: DETAILS = I think you know what this does ;-)")
            print("5: EXIT = EXIT the program.")
            print("10: HELP = will display a list of all the currently implemented commands to HELP you")
            print("14: STACK =  will generate the STACK in a specified .txt file. (similar to BURN)")
            input("Press Enter to exit DETAILS!")
            print()

        elif user == "ADD":
            print("*This is the old Assignment Table*")
            print_current(title, table, data)
            add_table(table, data)
            print_current(title, table, data)

        elif user == "DELETE":
            print("*This is the old Assignment Table*")
            print_current(title, table, data)
            delete_table(table)
            print_current(title, table, data)

        elif user == "PRINT":
            print("This is the currently selected Assignment Table:")
            print_current(title, table, data)

        elif user == "ENTER":
            print("Enter the values of the Assignment Table, starting top left:")
            enter_table(title, table, data)
            print_current(title, table, data)

        elif user == "GET":
            print("Get a previously saved Function/Assignment Table")
            title = input("Enter Function name: ")
            data = check_input("DATA", "NULL")

            found = False
            for sf in sf_list:
                if sf[1] == title:
                    temp = sf[2: len(sf)]
                    for entry in temp:
                        if entry[1] == data:
                            found = True
                            table = entry[2]
                            print("Current Assignment Table is now:")
                            print_current(title, table, data)
                            break
                    break

            if found is False:
                print("That Assignment Table doesn't exist!")
                print("Creating a new Assignment Table with name %s-%s." % (data, title))
                amt = check_input("AMOUNT", data)
                table = make_new(amt)

        elif user == "MODIFY":
            print("*This is the old Assignment Table*")
            print_current(title, table, data)
            modify_table(table)
            print("*This is the new Assignment Table*")
            print_current(title, table, data)

        elif user == "NEW":
            print("Make a new Function/Assignment Table: ")
            print()
            title = input("Enter Function name: ")
            data = check_input("DATA", "NULL")
            amt = check_input("AMOUNT", data)
            table = make_new(amt)

        elif user == "SAVE" or user == "S":
            sorted_insert(sf_list, title, data, table)

        elif user == "LIST" or user == "LS":
            print("*These are all the current Functions*")
            print()
            print_all(sf_list)

        elif user == "GRAPHICS" or user == "G":
            sf_list_graphics(sf_list)

        elif user == "BURN":
            filename = input("Enter filename: ")
            save_to_file(filename, sf_list)

        elif user == "REMOVE":
            print("Remove an entire stack frame: ")
            title = input("Enter Function name: ")
            data = check_input("DATA", "NULL")

            found = False
            for sf in sf_list:
                if sf[1] == title:
                    temp = sf[2: len(sf)]
                    for entry_count in range(len(temp)):
                        entry = temp[entry_count]
                        if entry[1] == data:
                            found = True
                            sf.pop(entry_count + 2)
                            check_after_delete(sf_list, sf)
                            print("Assignment Table with name %s-%s removed." % (data, title))
                            break
                    break
            if found is False:
                print("Assignment Table doesn't exist!")

        elif user == "STACK" or user == "ST":
            filename = input("Enter filename: ")
            print("Current Stack written to %s.txt!" % filename)
            stapel = make_stack(sf_list)
            burn_stack(stapel, filename)
            fix_stack_layout(filename)

        elif user == "STANDARD" or user == "STD":
            sf_list = gen_std()

    return

# ----------


#  The "main" function.
def main():
    sf_list = []
    print("*********************************")
    print("Welcome to DRAMA Stapel Tekenaar!")
    print("*********************************")
    print("TYPE MANUAL FOR MANUAL!")
    print()
    user = input("Press enter to start or type MANUAL to download the manual! ")
    user = user.upper()
    while user == "MANUAL":
        print("The MANUAL has been written to the file <DRAMA Stapel Tekenaar Manual.txt>")
        manual()
        print()
        user = input("Press enter to start or type MANUAL to download the manual! ")
        user = user.upper()

    if user == "STD":
        print("LOADING WITH STANDAARD SETTINGS")
        title = "TESTERINO"
        data = "PAR"
        amt = 1
        table = make_new(amt)
        sf_list = gen_std()
        interface(title, data, table, sf_list)

    else:
        print()
        title = input("Enter Function name: ")
        data = check_input("DATA", "NULL")
        amt = check_input("AMOUNT", data)
        table = make_new(amt)
        interface(title, data, table, sf_list)

# ----------


main()
