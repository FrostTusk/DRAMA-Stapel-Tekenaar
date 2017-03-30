from graphics import GraphicsWindow
# ----------
# function = a function in python
# Function = the toekeningstabel of the current function in DRAMA.
# ----------


# This function downloads the manual to the folder in which the user has saved the program.
def manual():
    filename = "DRAMA T-Tabellen MANUAL"
    outfile = open('%s.txt' % filename, 'w+')
    print("*********************************", file=outfile)
    print("Welcome to DRAMA Stapel Tekenaar!", file=outfile)
    print("*********************************", file=outfile)
    print("by Mathijs Hubrechtsen", file=outfile)
    print("", file=outfile)
    print("1. Introduction:", file=outfile)
    print("What is the DRAMA Stapel Tekenaar? Well, it is what it's name implies, it draws", end=" ", file=outfile)
    print("stapels for the DRAMA simulator used in socs.", file=outfile)
    print("I made this program so I could hone my skils in python/practice socs a bit,", end=" ", file=outfile)
    print("and I thought that maybe some people would like a program like this.", file=outfile)
    print("How does it work you ask? Well first off the user enters a few correct Toekeningstabellen.", file=outfile)
    print("After the user has done this, they simply ask the program to model what the stapel should look like.", file=outfile)
    print("It offers all the basic features you would expect: modifying T-Tabellen, visualizing T-Tabellen, etc.", file=outfile)
    print("The program isn't that complex ~900 lines of code, but it does offer quite a few nifty features.", file=outfile)
    print("Seeing as you're reading this manual right now, you're probably in possession of the program,", end=" ", file=outfile)
    print("so why not try it out! ;-)", file=outfile)
    print("Anyways, thank you for using my program and I hope it will be of some use to you!", file=outfile)
    print("", file=outfile)
    print("2. MANUAL:", file=outfile)
    print("Currently the DRAMA Stapel Tekenaar does not have a GUI, instead it uses", end=" ", file=outfile)
    print("a Terminal-esque UI where the user enters commands in", end=" ", file=outfile)
    print("the terminal/input box of Pycharm.", file=outfile)
    print("When the user starts the program he/she will be asked to press enter.", file=outfile)
    print("The user can also enter MANUAL to download the MANUAL you are now reading.", file=outfile)
    print("After pressing enter, they will be asked to enter a Function name.", file=outfile)
    print("This is the name of the first function you want to create a toekeningstabel of.", file=outfile)
    print("     The Input should be a string (bvb.: HelloWorld)", file=outfile)
    print("After entering a name, the user will be prompted to enter PAR or VAR or RES.", file=outfile)
    print("These commands stand for PARameter, VARiable or RESultaat", end=" ", file=outfile)
    print("the user should enter what kind of toekeningstabel he/she wants to make.", file=outfile)
    print("     The Input should be PAR or VAR or RES (bvb. : PAR)", file=outfile)
    print("After entering both the title of the function and what kind of tabel the user wants,", end=" ", file=outfile)
    print("the user will need to enter the amount of elements used in the tabel", file=outfile)
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


# These Functions save or visualize either the Current function or all of the functions in the current session.
def standaard():
    TT_Lijst = [ [1, 'Test1', ['Test1', 'PAR', [ ["PARA3", '1(R8)'], ["PARA2", '2(R8)'], ["PARA1", '3(R8)'], ] ],
                 ['Test1', 'VAR', [ ["VARA1", '-4(R8)'], ["VARA2", '-3(R8)'], ["VARA3", '-2(R8)'] ] ],
                 ['Test1', 'RES', [ ["RES1", '4(R8)'] ] ] ],
                 [2, 'Test2', ['Test2', 'PAR', [ ["PARA3", '1(R8)'], ["PARA2", '2(R8)'], ["PARA1", '3(R8)'], ] ],
                 ['Test2', 'VAR', [ ["VARA1", '-4(R8)'], ["VARA2", '-2(R8)'] ] ],
                 ['Test2', 'RES', [ ["RES1", '4(R8)'] ] ] ] ]
    return TT_Lijst


def drukCurrent(titel, tabel, pava):
    print()
    print("%s:" % titel)
    print(pava, "|", end=" ")
    print("ADRES")
    for i in range(len(tabel)):
        for j in range(2):
            if j == 0:
                print(tabel[i][j], "|", end=" ")
            if j == 1:
                print(tabel[i][j])
    print()
    return


def drukAll(TT_Lijst):
    for sub in TT_Lijst:
        nummer = sub[0]
        titel = sub[1]
        node_lijst = sub[2: len(sub)]
        print("*********************************")
        print("Tabellen van %i. %s:" % (nummer, titel))
        for node in node_lijst:
            drukCurrent(titel, node[2], node[1])
    return


def saveFile(filename, TT_Lijst):
    outfile = open('%s.txt' % filename, 'w+')
    print("Current T-Tabellen written to %s.txt!" % filename)

    for sub in TT_Lijst:
        nummer = sub[0]
        titel = sub[1]
        node_lijst = sub[2: len(sub)]
        print("*********************************", file=outfile)
        print("Tabellen van %i. %s:" % (nummer, titel), file=outfile)
        print("", file=outfile)
        for node in node_lijst:
            pava = node[1]
            tabel = node[2]
            value = len(tabel)
            print("     ", "%s%s%s" % ("*", pava, "*"), "|", end=" ", file=outfile)
            print("*ADRES*", file=outfile)
            for i in range(value):
                for j in range(2):
                    if j == 0:
                        print("     ", tabel[i][j], "|", end=" ", file=outfile)
                    if j == 1:
                        print(tabel[i][j], file=outfile)
            print("", file=outfile)
    outfile.close()
    return


def TT_Lijst_graphics(TT_Lijst):
    widthmax = 7
    length = 50
    for sub in TT_Lijst:
        user = sub[2: len(sub)]
        for node in user:
            tabel = node[2]
            length += len(tabel) * 25 + 25
            length += 50
            for i in range(len(tabel)):
                for j in range(2):
                    string = str(tabel[i][j])
                    if len(string) > widthmax:
                        widthmax = len(string)

    width = 2 * (25 + widthmax * 10 + 25)
    posy = 50
    win = GraphicsWindow(50 + width + 50, length + 100)
    canvas = win.canvas()

    for sub in TT_Lijst:
        user = sub[2: len(sub)]
        for node in user:
            canvas.setTextAnchor("nw")
            canvas.drawText(50, posy - 20, " %s-%s:" % (node[0], node[1]))
            tabel = node[2]

            height = len(tabel) * 25 + 25
            canvas.drawRect(50, posy, width, height)
            canvas.drawLine(50 + width / 2, posy, 50 + width / 2, posy + height)

            canvas.setTextAnchor("center")
            for j in range(2):
                if j == 0:
                    canvas.drawText(50 + width / 4 + j * (width / 2), posy + 12.5, "*" + node[1] + "*")
                else:
                    canvas.drawText(50 + width / 4 + j * (width / 2), posy + 12.5, "*ADRES*")
            posy += 25
            canvas.drawLine(50, posy, 50 + width, posy)

            for i in range(len(tabel)):
                for j in range(2):
                    canvas.drawText(50 + width / 4 + j * (width / 2), posy + 12.5, tabel[i][j])
                posy += 25
                canvas.drawLine(50, posy, 50 + width, posy)
            posy += 50
    win.wait()
    return
# ----------


# These Functions handle the stapel.
def ontleed(adres):
    adres = str(adres)
    try:
        int(adres)
    except ValueError:
        if adres == "...":
            return False
        if adres[0] == "R":
            return False
        token = adres.split("(")
        indexregister = token[1]
        if indexregister[1] != "8":
            return False
        return token[0]

    return False


def update_part(part, tabel):
    for i in range(len(tabel)):
        string = ontleed(tabel[i][1])
        if string is not False:
            part.append([string, tabel[i][0]])
            part[0] += 1
    return


def make_stapel(TT_Lijst):
    stapel = []
    for sub in TT_Lijst:
        nummer = sub[0]
        titel = sub[1]
        user = sub[2: len(sub)]
        par_part = [0]
        var_part = [0]
        res_part = [0]
        for node in user:
            temp = []
            pava = node[1]
            tabel = node[2]
            if pava == "PAR":
                update_part(par_part, tabel)
            elif pava == "VAR":
                update_part(var_part, tabel)
            elif pava == "RES":
                update_part(res_part, tabel)

        temp.append(nummer)
        temp.append(titel)
        temp.append(par_part)
        temp.append(var_part)
        temp.append(res_part)
        stapel.append(temp)
    return stapel


def burn_stapel(stapel, filename):
    outfile = open('%s.txt' % filename, 'w+')
    changed = False
    count = int

    for functie in stapel:
        nummer = functie[0]
        titel = functie[1]
        # User bevat PAR, VAR en RES
        user = functie[2: len(functie)]
        print("*********************************", file=outfile)
        print("Tabellen van %i. %s:" % (nummer, titel), file=outfile)
        print("", file=outfile)

        # VARIABELE EERST (START TOP STAPEL)
        var = user[1]
        if var[0] != 0:
            # Neem de count weg
            var = var[1: len(var)]
            # Current bovenste punt, we zoeken het kleinste omdat top stapel = kleinste adres
            current = var[0]
            for punt in var:
                if int(punt[0]) < int(current[0]):
                    current = punt
            var.remove(current)
            print("|%s" % current[1], file=outfile)

            # count is ons kleinste adres
            count = int(current[0])
            while var != []:
                count += 1
                current = [count, ""]
                for punt in var:
                    if int(punt[0]) == int(current[0]):
                        current = punt
                        changed = True
                if changed:
                    var.remove(current)
                    changed = False
                print("|%s" % current[1], file=outfile)

            # zorg ervoor dat we op -2(R8) terechtkome5n
            while count < -2:
                current = [count, ""]
                count += 1
                print("|%s" % current[1], file=outfile)

        # Altijd
        current = [-1, "TKA"]
        print("|%s" % current[1], file=outfile)
        current = [-0, "VORIGE R8"]
        print("|%s" % current[1], file=outfile)

        # Parameters onder variabele
        par = user[0]
        if par[0] != 0:
            par = par[1: len(par)]
            current = par[0]

            for punt in par:
                if int(punt[0]) < int(current[0]):
                    current = punt
            par.remove(current)
            print("|%s" % current[1], file=outfile)

            count = int(current[0])
            while par != []:
                count += 1
                current = [count, ""]
                for punt in par:
                    if int(punt[0]) == int(current[0]):
                        current = punt
                        changed = True
                if changed:
                    par.remove(current)
                    changed = False
                print("|%s" % current[1], file=outfile)

        # Resultaat als laatste
        res = user[2]
        if res[0] != 0:
            res = res[1: len(res)]

            current = res[0]
            for punt in res:
                if int(punt[0]) < int(current[0]):
                    current = punt
            res.remove(current)

            if user[0][0] != 0:
                count += 1
                while count < int(current[0]):
                    count += 1
                    print("", file=outfile)
            print("|%s" % current[1], file=outfile)

            count = int(current[0])
            while res != []:
                count += 1
                current = [count, ""]
                for punt in res:
                    if int(punt[0]) == int(current[0]):
                        current = punt
                        res.remove(current)
                print("|%s" % current[1], file=outfile)

        print("_", file=outfile)
    outfile.close()
    return


def fix_stapel_layout(filename):
    length = 0
    outfile = open('%s.txt' % filename, 'r')
    for line in outfile:
        if line[0] == "|":
            if len(line) - 1 > length:
                length = len(line) - 1

    outfile.close()
    burn_stapel_temp(filename, length)
    return


def burn_stapel_temp(filename, length):
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


def copy_temp(filename):
    outfile = open('%s.txt' % filename, 'w+')
    temp = open('%s.txt' % "temp", 'r')

    for line in temp:
        print("%s" % line[0: len(line) - 1], file=outfile)

    outfile.close()
    temp.close()
    clean_temp()
    return


def clean_temp():
    temp = open('%s.txt' % "temp", 'w+')
    temp.close()
    return
# ----------


# These Functions change the current function.
def addTabel(tabel, pava):
    print("RIJ is niet de plaats van rij!")
    print("Als je de eerste rij wilt hebben moet je niet 0 invullen maar 1!")
    user = int(input("ADD how many new %s? " % pava))
    print()
    for i in range(user):
        tabel.append(["...", "..."])
    print("*Nieuwe Tabel*")


def deleteTabel(tabel):
    print("RIJ is niet de plaats van rij!")
    print("Als je de eerste rij wilt hebben moet je niet 0 invullen maar 1!")
    rij = int(input("RIJ: "))
    print()
    tabel.pop(rij - 1)
    print("*Nieuwe Tabel*")


def enterTabel(titel, tabel, pava):
    print("Element betekent de data dat je op die plaats wil invoeren.")
    print("Vul EXIT in om vroegtijdig weg te gaan uit ENTER modus.")
    for i in range(len(tabel)):
        for j in range(2):
            drukCurrent(titel, tabel, pava)
            print()
            if j == 0:
                user = input("Enter Element: ")
            elif j == 1:
                user = validInput("ENTER", tabel, i, j)

            if user != "EXIT":
                tabel[i][j] = user
            else:
                break
        if user == "EXIT":
            break
    print("*Nieuwe Tabel*")


def makeNew(amt):
    tabel = []
    for i in range(amt):
        rij = ["..."] * 2
        tabel.append(rij)
    return tabel


def modifyTabel(tabel):
    print("RIJ en KOLOM zijn niet de plaats van de rij en kolom!")
    print("Als je de eerste rij wilt hebben moet je niet 0 invullen maar 1!")
    rij = int(input("RIJ: "))
    kolom = int(input("KOLOM: "))
    if kolom - 1 == 1:
        user = validInput("MODIFY", tabel, rij, kolom)
        tabel[rij - 1][kolom - 1] = user
    else:
        user = input("NEW VALUE: ")
        tabel[rij - 1][kolom - 1] = user
    return
# ----------


# These Functions check if the input is valid or sort the ToekeningsTabellen of the current session>
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


def validInput(tocheck, tabel, rij, kolom):
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
                    int(test)
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
                print("The input should be a valid DRAMA adress!")
                user = validInput("MODIFY", tabel, rij, kolom)
            elif valid is not True and tocheck == "ENTER":
                print("The input should be a valid DRAMA adress!")
                user = validInput("ENTER", tabel, rij, kolom)
    return user


def create_node(titel, pava, tabel):
    node = []
    node.append(titel)
    node.append(pava)
    node.append(tabel)
    return node


def create_sub(nummer, titel, tabel, pava):
    sub = []
    sub.append(nummer)
    sub.append(titel)
    sub.append(create_node(titel, pava, tabel))
    return sub


def check_sub(sub):
    user = sub[2: len(sub)]
    new_node = user[-1]
    new_node_pava = new_node[1]
    for node_count in range(len(user) - 1):
        node = user[node_count]
        node_pava = node[1]
        if node_pava == new_node_pava:
            sub.pop(node_count + 2)
            return
    return


def check_after_delete(TT_Lijst, sub):
    if len(sub) == 2:
        # Delete sub
        TT_Lijst.remove(sub)

        nummer_expect = 1
        for sub in TT_Lijst:
            if sub[0] != nummer_expect:
                sub[0] = nummer_expect
            nummer_expect += 1
    return


def sort_sub(sub):
    user = sub[2: len(sub)]
    user_count = 0
    test = ["PAR", "VAR", "RES"]
    test_count = 0
    node_count = 0
    found = False
    wait = True

    while wait:
        temp_node = user[user_count]
        pava = temp_node[1]
        pava_test = test[test_count]
        if pava == pava_test:
            user_count += 1
            test_count += 1
        else:
            for node_count in range(len(user)):
                temp_node = user[node_count]
                pava = temp_node[1]

                if pava == pava_test:
                    found = True
                    break

            if found:
                temp = sub.pop(node_count + 2)
                sub.insert(user_count + 2, temp)
                user.pop(node_count)
                user.insert(user_count, temp)
                print(sub)
                found = False
            else:
                test_count += 1

        if test_count == 3 or user_count == len(user):
            wait = False
    return


def sort_lijst_invoeg(TT_Lijst, titel, pava, tabel):
    sub_nummer = 0
    check = True

    for sub in TT_Lijst:
        sub_nummer = sub[0]
        sub_titel = sub[1]
        if sub_titel == titel:
            check = False
            sub.append(create_node(titel, pava, tabel))
            check_sub(sub)
            sort_sub(sub)
            break
    if check:
        new_sub = create_sub(sub_nummer + 1, titel, tabel, pava)
        TT_Lijst.append(new_sub)
    return
# ----------


# This Function handles the interface.
def Interface(titel, pava, tabel, TT_Lijst):
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
            print("8: FROMFILE => !WIP!")
            print("9: GET")
            print("10: GRAPHICS or G")
            print("11: HELP")
            print("12: LIJST")
            print("13: MODIFY")
            print("14: NEW")
            print("15: REMOVE")
            print("16: SAVE or S")
            print("17: STAPEL or ST")
            print("18: STANDARD or STD")
            print("TYPE DETAILS FOR DETAILS ON ALL COMMANDS")
            input("Press Enter to exit HELP!")
            print()

        elif user == "DETAILS":
            print("* DETAILS: *")
            print("FUNCTION = the function of which you are currently making a toekeningstabel")
            print("SESSION = all of the functions made during a single 'session'")
            print()
            print("These Instructions modify the current function:")
            print("1: ADD = ADD a specied amount of extra rows to the current function.")
            print("3: DELETE = DELETE a specified row.")
            print("6: ENTER = ENTER the function, this will always enter the function at the very first element.")
            print("13: MODIFY =  MODIFY a specified element in the function.")
            input("Press Enter to continue")
            print()
            print("These Instructions generate a new or old function:")
            print("9: GET = GET an old function.")
            print("14: NEW = Create a NEW function.")
            print("15: REMOVE = REMOVE an old function")
            input("Press Enter to continue")
            print()
            print("These Instructions visualize or save the current function:")
            print("5: DRUK = DRUK the current function.")
            print("16: SAVE =  SAVE the current function")
            input("Press Enter to continue")
            print()
            print("These Instructions generate a standard or old session:")
            print("8: FROMFILE = CURRENTLY NOT IMPLEMENTED")
            print("18: STANDARD or STD = load the STANDARD preset session ")
            input("Press Enter to continue")
            print()
            print("These Instructions visualize or save the current session")
            print("2: BURN = BURN all the functions you have saved in the current session to a specified", end=" ")
            print(".txt file ,if there is no file with that name, the program will create one.")
            print("2: The program saves this .txt file in the same folder as where the program is located.")
            print("10: GRAPHICS = will GRAPHICally generate the current session with the graphics.py module.")
            print("12: LIJST = Will LIJST all the functions you have saved in the current session in the terminal.")
            input("Press Enter to continue")
            print()
            print("These Instructions will perform global actions.")
            print("4: DETAILS = I think you know what this does ;-)")
            print("5: EXIT = EXIT the program.")
            print("11: HELP = will display a list of all the currently implemented commands to HELP you")
            print("15: STAPEL =  will generate the STAPEL in a specified .txt file. (see BURN)")
            input("Press Enter to exit DETAILS!")
            print()

        elif user == "ADD":
            print("*Dit is de oude tabel*")
            drukCurrent(titel, tabel, pava)
            addTabel(tabel, pava)
            drukCurrent(titel, tabel, pava)

        elif user == "DELETE":
            print("*Dit is de oude tabel*")
            drukCurrent(titel, tabel, pava)
            deleteTabel(tabel)
            drukCurrent(titel, tabel, pava)

        elif user == "DRUK":
            print("Dit is de Current geselecteerde tabel:")
            drukCurrent(titel, tabel, pava)

        elif user == "ENTER":
            print("Enter de elementen van de tabel, startend met linksboven:")
            enterTabel(titel, tabel, pava)
            drukCurrent(titel, tabel, pava)

        elif user == "GET":
            print("Roep een oude gesavede functie op:")
            titel = input("Enter Functie Naam: ")
            pava = checkInput("PAVA", "NULL")

            found = False
            for sub in TT_Lijst:
                if sub[1] == titel:
                    temp = sub[2: len(sub)]
                    for node in temp:
                        if node[1] == pava:
                            found = True
                            tabel = node[2]
                            print("Current Tabel is nu:")
                            drukCurrent(titel, tabel, pava)
                            break
                    break

            if found is False:
                print("That T-Tabel doesn't exist!")
                print("Creating new T-Tabel with name %s-%s." % (pava, titel))
                amt = checkInput("AMOUNT", pava)
                tabel = makeNew(amt)

        elif user == "MODIFY":
            print("*Old T-Tabel*")
            drukCurrent(titel, tabel, pava)
            modifyTabel(tabel)
            print("*New T-Tabel*")
            drukCurrent(titel, tabel, pava)

        elif user == "NEW":
            print("Make a new Function: ")
            print()
            titel = input("Enter Function name: ")
            pava = checkInput("PAVA", "NULL")
            amt = checkInput("AMOUNT", pava)
            tabel = makeNew(amt)

        elif user == "SAVE" or user == "S":
            sort_lijst_invoeg(TT_Lijst, titel, pava, tabel)

        elif user == "LIJST":
            print("*These are all the current T-Tabellen*")
            print()
            drukAll(TT_Lijst)

        elif user == "GRAPHICS" or user == "G":
            TT_Lijst_graphics(TT_Lijst)

        elif user == "BURN":
            filename = input("Enter filename: ")
            saveFile(filename, TT_Lijst)

        elif user == "REMOVE":
            print("Delete an old function: ")
            titel = input("Enter Function name: ")
            pava = checkInput("PAVA", "NULL")

            found = False
            for sub in TT_Lijst:
                if sub[1] == titel:
                    temp = sub[2: len(sub)]
                    for node_count in range(len(temp)):
                        node = temp[node_count]
                        if node[1] == pava:
                            found = True
                            sub.pop(node_count + 2)
                            check_after_delete(TT_Lijst, sub)
                            print("T-Tabel with name %s-%s removed." % (pava, titel))
                            break
                    break
            if found is False:
                print("That T-Tabel doesn't exist!")

        elif user == "STAPEL" or user == "ST":
            filename = input("Enter filename: ")
            print("Current Stapel written to %s.txt!" % filename)
            stapel = make_stapel(TT_Lijst)
            burn_stapel(stapel, filename)
            fix_stapel_layout(filename)

        elif user == "STANDARD" or user == "STD":
            TT_Lijst = standaard()

    return
# ----------


#  The "main" function.
def main():
    TT_Lijst = []
    print("*********************************")
    print("Welcome to DRAMA Stapel Tekenaar!")
    print("*********************************")
    print("TYPE MANUAL FOR MANUAL!")
    print()
    user = input("Press enter to start or type MANUAL to download the manual! ")
    user = user.upper()
    while user == "MANUAL":
        print("The MANUAL has been written to the file <DRAMA T-Tabellen MANUAL.txt>")
        manual()
        print()
        user = input("Press enter to start or type MANUAL to download the manual! ")
        user = user.upper()

    if user == "STD":
        print("LOADING WITH STANDAARD SETTINGS")
        titel = "TESTERINO"
        pava = "PAR"
        amt = 1
        tabel = makeNew(amt)
        TT_Lijst = standaard()
        Interface(titel, pava, tabel, TT_Lijst)

    else:
        print()
        titel = input("Enter Function name: ")
        pava = checkInput("PAVA", "NULL")
        amt = checkInput("AMOUNT", pava)
        tabel = makeNew(amt)
        Interface(titel, pava, tabel, TT_Lijst)
# ----------


main()
