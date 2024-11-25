import inspect
from inspect import getmodule


def introspection_info(obj):
    t_obj = type(obj)
    d_obj = dir(obj)
    c_obj = callable(obj)
    m_obj = getmodule(obj)
    cl_obj = inspect.isclass(obj)
    info = {'type': t_obj, 'attributes': d_obj, 'module': m_obj, 'is call': c_obj, 'is class': cl_obj}
    return info


number_info = introspection_info('Hello')
print(number_info)
