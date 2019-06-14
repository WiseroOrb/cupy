"""
Utilities needed for fallback_mode.
"""
import cupy as cp # NOQA
import numpy as np # NOQA

from cupy.fallback_mode.data_tranfer import _get_cupy_result
from cupy.fallback_mode.data_tranfer import _get_numpy_args


def _call_cupy(func, args, kwargs):
    """
    Calls cupy function with *args and **kwargs.

    Args:
        func: A cupy function that needs to be called.
        args (tuple): Arguments.
        kwargs (dict): Keyword arguments.

    Returns:
        Result after calling func.
    """

    return func(*args, **kwargs)


def _call_numpy(func, args, kwargs):
    """
    Calls numpy function with *args and **kwargs.

    Args:
        func: A numpy function that needs to be called.
        args (tuple): Arguments.
        kwargs (dict): Keyword arguments.

    Returns:
        Result after calling func.
    """

    numpy_args, numpy_kwargs = _get_numpy_args(args, kwargs)
    numpy_res = func(*numpy_args, **numpy_kwargs)
    cupy_res = _get_cupy_result(numpy_res)

    return cupy_res
