import inspect


def some_function(*args, **kwargs):
    print(args, kwargs)


def modified_func(func, *fixated_args, **fixated_kwargs):

    def new_func(*fixed_args, **fixed_kwargs):
        """
        A func implementation of {func_name}
        with pre-applied arguments being:
        {fixated_args}, {fixated_kwargs}
        source_code:
        {source}
        """
        all_args = (*fixed_args, *fixated_args)
        all_kwargs = {**fixed_kwargs, **fixated_kwargs}

        return func(*all_args, **all_kwargs)

    source = inspect.getsource(new_func) 
    replaces = (('{func_name}', str(func.__name__)),
                ('{fixated_args}', str(fixated_args)),
                ('{fixated_kwargs}', str(fixated_kwargs)),
                ('{source}', source))

    for replace in replaces:
        new_func.__doc__ = new_func.__doc__.replace(*replace)

    new_func.__name__ = func.__name__

    return new_func

some_dict = {'param': True, 'not_param': False}

modified_func(some_function, 5, 6)()
print(modified_func(min, 5, 6)(3))
modified_func(some_function, 5)(**some_dict)
