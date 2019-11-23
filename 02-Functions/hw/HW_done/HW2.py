def atom(var=None):

    def get_value():
        return var

    def set_value(set_value=None):

        nonlocal var
        var = set_value

        return var

    def process_value(*functions):

        nonlocal var
        for f in functions:
            var = f(var)

        return var

    def delete_value():
        nonlocal var
        del var

    return get_value, set_value, process_value, delete_value

# value = 5
# vget = atom(value)[0]
# vset = atom(value)[1]
# veval = atom(value)[2]
# vdel = atom(value)[3]

print('Set_value\nnew value :', atom(5)[1](10))
print('process_value\nto_float->to_int :', atom(5)[2](float, int))
print('delete_value :', atom(5)[3]())
