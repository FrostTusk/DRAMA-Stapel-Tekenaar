from graphics import GraphicsWindow

# I apologize for the lack of documentation, I was still a foolish novice programmer when I wrote this code.

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
    filename = "DRAMA T-tablelen MANUAL"
    outfile = open('%s.txt' % filename, 'w+')
    print("*********************************", file=outfile)
    print("Welcome to DRAMA Stapel Tekenaar!", file=outfile)
    print("*********************************", file=outfile)
    print("by Mathijs Hubrechtsen", file=outfile)
    print("", file=outfile)
    print("1. Introduction:", file=outfile)
    print("What is the DRAMA Stapel Tekenaar? Well, it is what it's name implies, it draws", end=" ", file=outfile)
    print("stapels for the DRAMA simulator used in SOCS.", file=outfile)
    print("I made this program so I could hone my skils in python/practice SOCS a bit,", end=" ", file=outfile)
    print("and I thought that maybe some people would like a program like this.", file=outfile)
    print("How does it work you ask? Well first off the user enters a few correct Toekeningstablelen.", file=outfile)
    print("After the user has done this, they simply ask the program to model what the stapel should look like.", file=outfile)
    print("It offers all the basic features you would expect: modifying T-tablelen, visualizing T-tablelen, etc.", file=outfile)
    print("The program isn't that complex: ~900 lines of code, but it does offer quite a few nifty features.", file=outfile)
    print("Seeing as you're reading this manual right now, you're probably in possession of the program,", end=" ", file=outfile)
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
    print("This is the name of the first function you want to create a toekeningstable of.", file=outfile)
    print("     The Input should be a string (bvb.: HelloWorld)", file=outfile)
    print("After entering a name, the user will be prompted to enter PAR or VAR or RES.", file=outfile)
    print("These commands stand for PARameter, VARiable or RESultaat", end=" ", file=outfile)
    print("the user should enter what kind of toekeningstable he/she wants to make.", file=outfile)
    print("     The Input should be PAR or VAR or RES (bvb. : PAR)", file=outfile)
    print("After entering both the title of the function and what kind of table the user wants,", end=" ", file=outfile)
    print("the user will need to enter the amount of elements used in the table", file=outfile)
    print("     The Input should be an integer number (bvb.: 3)", file=outfile)
    print("After entering all of this information, the user will enter the ui.", file=outfile)
    print("Here they can type HELP or DETAILS for more help on what they can do next", file=outfile)
    print("", file=outfile)
    print("3. Extra Information:", file=outfile)
    print("If you are still running into trouble , want to report a bug, or want to help", end=" ", file=outfile)
    print("me improve the DRAMA Stapel Tekenaar, ", end=" ", file=outfile)
    print("do not hesitate to contact me at mathijs.hubrechtsen@student.kuleuven.be!", file=outfile)
    print("Finally I would like to thank you again for using my program,", end=" ", file=outfile)
    print("I'm only still learning so please do give me constructive criticism if it could help me!", file=outfile)
    print("     -Mathijs Hubrechtsen", file=outfile)
    print("", file=outfile)
    print("4. Credits:", file=outfile)
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
    print("Current T-Tables written to %s.txt!" % filename)

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


# Dissect an address to see if it's a valid non-numeric, non-register DRAMA address
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


# stack_entry = final version of an entry, stack_entry will be used to draw the stack
# table = the non-final table corresponding to the entry
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
        # User bevat PAR, VAR en RES
        entry_list = sf[2: len(sf)]
        print("*********************************", file=outfile)
        print("Stack of %i. %s:" % (counter, title), file=outfile)
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


# Adds layout formatting to the stack that was written to the given file
def fix_stack_layout(filename):
    # length contains the length of the longest cell name
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
        rij = ["..."] * 2
        table.append(rij)
    return table


def add_table(table, pava):
    print("RIJ is niet de plaats van rij!")
    print("Als je de eerste rij wilt hebben moet je niet 0 invullen maar 1!")
    user = int(input("ADD how many new %s? " % pava))
    print()
    for i in range(user):
        table.append(["...", "..."])
    print("*Nieuwe table*")


def delete_table(table):
    print("RIJ is niet de plaats van rij!")
    print("Als je de eerste rij wilt hebben moet je niet 0 invullen maar 1!")
    rij = int(input("RIJ: "))
    print()
    table.pop(rij - 1)
    print("*Nieuwe table*")


def enter_table(titel, table, pava):
    print("Element betekent de data dat je op die plaats wil invoeren.")
    print("Vul EXIT in om vroegtijdig weg te gaan uit ENTER modus.")
    for i in range(len(table)):
        for j in range(2):
            print_current(titel, table, pava)
            print()
            if j == 0:
                user = input("Enter Element: ")
            elif j == 1:
                user = validInput("ENTER", table, i, j)

            if user != "EXIT":
                table[i][j] = user
            else:
                break
        if user == "EXIT":
            break
    print("*Nieuwe table*")


def modify_table(table):
    print("RIJ en KOLOM zijn niet de plaats van de rij en kolom!")
    print("Als je de eerste rij wilt hebben moet je niet 0 invullen maar 1!")
    rij = int(input("RIJ: "))
    kolom = int(input("KOLOM: "))
    if kolom - 1 == 1:
        user = validInput("MODIFY", table, rij, kolom)
        table[rij - 1][kolom - 1] = user
    else:
        user = input("NEW VALUE: ")
        table[rij - 1][kolom - 1] = user
    return

# ----------


# These Functions check if the input is valid or sort the Toekeningstabelen of the current session>

# The Difference between checkInput and validInput is that ValidInput only works if called upon to modify
# a specific element in a Function.
def checkInput(tocheck, value):
    if tocheck == "PAVA":
        pava = input("Enter PAR or VAR or RES: ")
        pava = pava.upper()
        while pava != "PAR" and pava != "VAR" and pava != "RES":
            pava = input("Enter PAR or VAR or RES: ")
            pava = pava.upper()
        return pava

    elif tocheck == "AMOUNT":
        pava = value
        amt = input("Amount of %s: " % pava)
        Test = False
        while Test is False:
            Test = True
            try:
                int(amt)
            except ValueError:
                print("That's not an int! If you want to enter for example, 3 %s," % pava, end=" ")
                print("you would enter the number: 3.")
                Test = False

            if Test is False:
                amt = input("Amount of %s: " % pava)
            else:
                amt = int(amt)
        return amt


def validInput(tocheck, table, rij, kolom):
    valid = bool
    if tocheck == "MODIFY" or tocheck == "ENTER":
        if tocheck == "MODIFY":
            user = input("NEW VALUE: ")
            valid = False
        elif tocheck == "ENTER":
            user = input("Enter Element: ")
            user = user.upper()
            if user == "EXIT":
                valid = True
            else:
                valid = False

        checkset = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        while valid is not True:
            valid = True

            usertest = list(user)
            if "(" not in usertest:
                valid = False

            if valid:
                usertest = user.split("(")
                test = usertest[0]
                try:
                    test = int(test)
                except ValueError:

                    valid = False

                if valid:
                    if -9999 > test or test > 9999:
                        valid = False

                test = usertest[1]
                if test[0] != "R":
                    valid = False
                elif test[1] not in checkset:
                    valid = False
                elif test[2] != ")":
                    valid = False

            try:
                val = int(user)
            except ValueError:
                val = user
            else:
                if 0 <= val < 9999:
                    valid = True

            if valid is not True:
                usertest = list(user)
                if len(usertest) == 2:
                    if usertest[0] != "R":
                        valid = False
                    elif usertest[1] not in checkset:
                        valid = False
                    else:
                        valid = True
                else:
                    valid = False

            if valid is not True and tocheck == "MODIFY":
                print("The input should be a valid DRAMA addresss!")
                user = validInput("MODIFY", table, rij, kolom)
            elif valid is not True and tocheck == "ENTER":
                print("The input should be a valid DRAMA addresss!")
                user = validInput("ENTER", table, rij, kolom)
    return user


def create_entry(titel, pava, table):
    entry = []
    entry.append(titel)
    entry.append(pava)
    entry.append(table)
    return entry


def create_sf(nummer, titel, table, pava):
    sf = []
    sf.append(nummer)
    sf.append(titel)
    sf.append(create_entry(titel, pava, table))
    return sf


def check_sf(sf):
    temp = sf[2: len(sf)]
    # Get the entry that was just inserted
    new_entry = temp[-1]
    new_entry_pava = new_entry[1]
    # Check if this entry already exists
    for entry_count in range(len(temp) - 1):
        entry = temp[entry_count]
        entry_pava = entry[1]
        if entry_pava == new_entry_pava:
            # +2 because counter and title are in the front.
            sf.pop(entry_count + 2)
            return
    return


def check_after_delete(sf_list, sf):
    if len(sf) == 2:
        # Delete sf
        sf_list.remove(sf)

        nummer_expect = 1
        for sf in sf_list:
            if sf[0] != nummer_expect:
                sf[0] = nummer_expect
            nummer_expect += 1
    return


def get_value(pava):
    if pava == "PAR":
        return 0
    elif pava == "VAR":
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


def sort_lijst_invoeg(sf_list, titel, pava, table):
    sf_nummer = 0
    check = True

    for sf in sf_list:
        sf_nummer = sf[0]
        sf_titel = sf[1]
        if sf_titel == titel:
            check = False
            sf.append(create_entry(titel, pava, table))
            check_sf(sf)
            sort_sf(sf)
            break
    if check:
        new_sf = create_sf(sf_nummer + 1, titel, table, pava)
        sf_list.append(new_sf)
    return

# ----------


# This Function handles the interface.
def interface(titel, pava, table, sf_list):
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
            print("5: DRUK")
            print("6: ENTER")
            print("7: EXIT")
            print("8: GET")
            print("9: GRAPHICS or G")
            print("10: HELP")
            print("11: LIJST")
            print("12: MODIFY")
            print("13: NEW")
            print("14: REMOVE")
            print("15: SAVE or S")
            print("16: STAPEL or ST")
            print("17: STANDARD or STD")
            print("TYPE DETAILS FOR DETAILS ON ALL COMMANDS")
            input("Press Enter to exit HELP!")
            print()

        elif user == "DETAILS":
            print("* DETAILS: *")
            print("FUNCTION = the function of which you are currently making a toekeningstable")
            print("SESSION = all of the functions made during a single 'session'")
            print()
            print("These Instructions modify the current function:")
            print("1: ADD = ADD a specied amount of extra rows to the current function.")
            print("3: DELETE = DELETE a specified row.")
            print("6: ENTER = ENTER the function, this will always enter the function at the very first element.")
            print("12: MODIFY =  MODIFY a specified element in the function.")
            input("Press Enter to continue")
            print()
            print("These Instructions generate a new or old function:")
            print("8: GET = GET an old function.")
            print("13: NEW = Create a NEW function.")
            print("14: REMOVE = REMOVE an old function")
            input("Press Enter to continue")
            print()
            print("These Instructions visualize or save the current function:")
            print("5: DRUK = DRUK the current function.")
            print("15: SAVE =  SAVE the current function")
            input("Press Enter to continue")
            print()
            print("These Instructions generate a standard or old session:")
            print("17: STANDARD or STD = load the STANDARD preset session ")
            input("Press Enter to continue")
            print()
            print("These Instructions visualize or save the current session")
            print("2: BURN = BURN all the functions you have saved in the current session to a specified", end=" ")
            print(".txt file, if there is no file with that name, the program will create one.")
            print("2: The program saves this .txt file in the same folder as where the program is located.")
            print("9: GRAPHICS = will GRAPHICally generate the current session with the graphics.py module.")
            print("11: LIJST = Will LIJST all the functions you have saved in the current session in the terminal.")
            input("Press Enter to continue")
            print()
            print("These Instructions will perform global actions.")
            print("4: DETAILS = I think you know what this does ;-)")
            print("5: EXIT = EXIT the program.")
            print("10: HELP = will display a list of all the currently implemented commands to HELP you")
            print("14: STAPEL =  will generate the STAPEL in a specified .txt file. (see BURN)")
            input("Press Enter to exit DETAILS!")
            print()

        elif user == "ADD":
            print("*Dit is de oude table*")
            print_current(titel, table, pava)
            add_table(table, pava)
            print_current(titel, table, pava)

        elif user == "DELETE":
            print("*Dit is de oude table*")
            print_current(titel, table, pava)
            delete_table(table)
            print_current(titel, table, pava)

        elif user == "DRUK":
            print("Dit is de Current geselecteerde table:")
            print_current(titel, table, pava)

        elif user == "ENTER":
            print("Enter de elementen van de table, startend met linksboven:")
            enter_table(titel, table, pava)
            print_current(titel, table, pava)

        elif user == "GET":
            print("Roep een oude gesavede functie op:")
            titel = input("Enter Functie Naam: ")
            pava = checkInput("PAVA", "NULL")

            found = False
            for sf in sf_list:
                if sf[1] == titel:
                    temp = sf[2: len(sf)]
                    for entry in temp:
                        if entry[1] == pava:
                            found = True
                            table = entry[2]
                            print("Current table is nu:")
                            print_current(titel, table, pava)
                            break
                    break

            if found is False:
                print("That T-table doesn't exist!")
                print("Creating new T-table with name %s-%s." % (pava, titel))
                amt = checkInput("AMOUNT", pava)
                table = make_new(amt)

        elif user == "MODIFY":
            print("*Old T-table*")
            print_current(titel, table, pava)
            modify_table(table)
            print("*New T-table*")
            print_current(titel, table, pava)

        elif user == "NEW":
            print("Make a new Function: ")
            print()
            titel = input("Enter Function name: ")
            pava = checkInput("PAVA", "NULL")
            amt = checkInput("AMOUNT", pava)
            table = make_new(amt)

        elif user == "SAVE" or user == "S":
            sort_lijst_invoeg(sf_list, titel, pava, table)

        elif user == "LIJST":
            print("*These are all the current T-tablelen*")
            print()
            print_all(sf_list)

        elif user == "GRAPHICS" or user == "G":
            sf_list_graphics(sf_list)

        elif user == "BURN":
            filename = input("Enter filename: ")
            save_to_file(filename, sf_list)

        elif user == "REMOVE":
            print("Delete an old function: ")
            titel = input("Enter Function name: ")
            pava = checkInput("PAVA", "NULL")

            found = False
            for sf in sf_list:
                if sf[1] == titel:
                    temp = sf[2: len(sf)]
                    for entry_count in range(len(temp)):
                        entry = temp[entry_count]
                        if entry[1] == pava:
                            found = True
                            sf.pop(entry_count + 2)
                            check_after_delete(sf_list, sf)
                            print("T-table with name %s-%s removed." % (pava, titel))
                            break
                    break
            if found is False:
                print("That T-table doesn't exist!")

        elif user == "STAPEL" or user == "ST":
            filename = input("Enter filename: ")
            print("Current Stapel written to %s.txt!" % filename)
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
        print("The MANUAL has been written to the file <DRAMA T-tablelen MANUAL.txt>")
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
        data = checkInput("PAVA", "NULL")
        amt = checkInput("AMOUNT", type)
        table = make_new(amt)
        interface(title, data, table, sf_list)

# ----------


main()
