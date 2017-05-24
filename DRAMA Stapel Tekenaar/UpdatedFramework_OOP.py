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
    def __init__(self, name):
        if not isinstance(name, str):
            raise AttributeError
        self._name = name

    _name = None
    _parameter = None
    _variable = None
    _result = None

    def get_name(self):
        return self._name

    def get_parameter(self):
        return self._parameter

    def get_result(self):
        return self._result

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


def main():
    x = Function("user")
    print(x)


main()
