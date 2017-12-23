from Resources import manual


class TableType:
    def __init__(self, table_type):
        if not isinstance(type, str):
            raise AttributeError("table_type is invalid type")
        if not ((table_type == "PAR") or (table_type == "RES") or (table_type == "VAR")):
            raise AttributeError("type is not PAR or RES or VAR")
        self._table_type = table_type

    _table_type = None

    def _get_table_type(self):
        return self._table_type


class AssignmentTable:
    def __init__(self, owner, table, table_type):
        if not isinstance(owner, Function):
            raise AttributeError("owner is invalid type")
        if not isinstance(type, TableType):
            raise AttributeError("table_type is invalid type")
        self._owner = owner
        self._table = table
        self._table_type = table_type

    _owner = None
    _table = None
    _table_type = None

    def get_owner(self):
        return self._owner

    def get_table_type(self):
        return self._table_type

    def get_table(self):
        return self._table


class Function:
    def __init__(self, name, number):
        if not isinstance(name, str):
            raise AttributeError("name is invalid type")
        if not isinstance(number, int):
            raise AttributeError("number is invalid type")
        self._name = name
        self._number = number

    _name = None
    _number = int
    _parameter = None
    _result = None
    _variable = None

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_parameter(self):
        return self._parameter

    def get_result(self):
        return self._result

    def get_tables(self):
        return [self.get_parameter(), self.get_variable(), self.get_result()]

    def get_variable(self):
        return self._variable

    def set_parameter(self, parameter):
        if not isinstance(parameter, AssignmentTable):
            raise AttributeError("parameter is invalid type")
        self._parameter = parameter

    def set_result(self, result):
        if not isinstance(result, AssignmentTable):
            raise AttributeError("result is invalid type")
        self._result = result

    def set_variable(self, variable):
        if not isinstance(variable, AssignmentTable):
            raise AttributeError("variable is invalid type")
        self._variable = variable


# ----------
def make_new_table(amt):
    table = []
    for i in range(amt):
        rij = ["..."] * 2
        table.append(rij)
    return table


def standaard():
    functions = []
    temp_function = Function("Test1", 1)
    temp_assignment_table = AssignmentTable(temp_function, [["PARA3", '1(R8)'], ["PARA2", '2(R8)'], ["PARA1", '3(R8)']],
                                            TableType("PAR"))
    temp_function.set_parameter(temp_assignment_table)
    temp_assignment_table = AssignmentTable(temp_function, [["VARA1", '-4(R8)'],
                                                            ["VARA2", '-3(R8)'], ["VARA3", '-2(R8)']], TableType("VAR"))
    temp_function.set_variable(temp_assignment_table)
    temp_assignment_table = AssignmentTable(temp_function, [["RES1", '4(R8)']],
                                            TableType("RES"))
    temp_function.set_result(temp_assignment_table)
    functions.append(temp_function)

    temp_function = Function("Test2", 2)
    temp_assignment_table = AssignmentTable(temp_function, [["PARA3", '1(R8)'], ["PARA2", '2(R8)'], ["PARA1", '3(R8)']],
                                            TableType("PAR"))
    temp_function.set_parameter(temp_assignment_table)
    temp_assignment_table = AssignmentTable(temp_function, [["VARA1", '-4(R8)'], ["VARA2", '-2(R8)']],
                                            TableType("VAR"))
    temp_function.set_parameter(temp_assignment_table)
    temp_assignment_table = AssignmentTable(temp_function, [["RES1", '4(R8)']], TableType("RES"))
    temp_function.set_parameter(temp_assignment_table)
    functions.append(temp_function)

    return functions


def print_current(current_table):
    print()
    print("%s:" % current_table.get_owner().get_name())
    print(current_table.get_table_type(), "|", end=" ")
    print("ADRES")
    for i in range(len(current_table.get_table())):
        for j in range(2):
            if j == 0:
                print(current_table.get_table()[i][j], "|", end=" ")
            if j == 1:
                print(current_table.get_table()[i][j])
    print()
    return


def print_all(functions):
    for current_function in functions:
        print("*********************************")
        print("Tabellen van %i. %s:" % (current_function.get_number(), current_function.get_name()))
        for table in current_function.get_tables():
            print_current(table)
    return


def save_file(filename, functions):
    outfile = open('%s.txt' % filename, 'w+')
    print("Current assignment tables written to %s.txt!" % filename)

    for function in functions:
        print("*********************************", file=outfile)
        print("Tabellen van %i. %s:" % (function.get_number(), function.get_name()), file=outfile)
        print("", file=outfile)
        for table in function.get_tables():
            print("     ", "%s%s%s" % ("*", table.get_table_type(), "*"), "|", end=" ", file=outfile)
            print("*ADRES*", file=outfile)
            for i in range(len(table.get_table())):
                for j in range(2):
                    if j == 0:
                        print("     ", table.get_table[i][j], "|", end=" ", file=outfile)
                    if j == 1:
                        print(table.get_table[i][j], file=outfile)
            print("", file=outfile)
    outfile.close()
    return


def add_to_table(current_table):
    user = int(input("ADD how many new %s? " % current_table.get_table_type))
    print()
    for i in range(user):
        current_table.get_table().append(["...", "..."])
    print("*%i new %s added!*" % (user, current_table.get_table_type))


def delete_to_table(current_table):
    user = int(input("DELETE ROW: "))
    print()
    current_table.get_table().pop(user - 1)
    print("ROW: %i deleted" % user)


# def enter_table(current_table):
#     print("Element betekent de data dat je op die plaats wil invoeren.")
#     print("Vul EXIT in om vroegtijdig weg te gaan uit ENTER modus.")
#     for i in range(len(current_table.get_table())):
#         for j in range(2):
#             print_current(current_table)
#             print()
#             if j == 0:
#                 user = input("Enter Element: ")
#             elif j == 1:
#                 user = validInput("ENTER", tabel, i, j)
#
#             if user != "EXIT":
#                 tabel[i][j] = user
#             else:
#                 break
#         if user == "EXIT":
#             break
#     print("*Nieuwe Tabel*")


# ----------
def interface(current_table, functions):
    user = "START"
    while user != "EXIT":
        print()
        print("Enter HELP for list of commands")
        user = input("What do you want to do? ")
        user = user.upper()
        print("COMMAND: ", user)
        print()

        if user == "DRUK":
            print("Dit is de Current geselecteerde tabel:")
            print_current(current_table)


#  The "main" function.
def main():
    functions = []
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
        print("LOADING WITH STANDARD SETTINGS")
        new_function = Function("TEST", 3)
        table = make_new_table(1)
        current_table = AssignmentTable(new_function, table, TableType("PAR"))
        new_function.set_parameter(current_table)
        functions = standaard()
        interface(current_table, functions)
# ----------


main()
