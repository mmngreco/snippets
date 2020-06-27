"""
Vectorized implementation of datenum to datetime.

datenum2datetime(datenum : list or float) -> datetime

1. Intento una versión sencilla (naive) que opera sobre un número (datenum).
2. Intento una versión mejorada (naive_caching) la misma lógica pero con una cache.
3. Implemento una versión en vectorizada map_naive_caching
4. Implemento una alternativa vecotorizada en numpy numpy_v1
5. hago un test y fallan el 100% por errores de precisión.
6. cambio el algoritmo para tratar de minimizar errores de percisión.
7. los tests siguen fallando
8. intento mejorar el algoritmo usando ns pero encuentro un bug en numpy (https://github.com/numpy/numpy/issues/16689)
9. Cualquier implementación en ns con numpy/ pandas me lleva a al bug anterior en numpy.
10. decido cambiar de unidades de ns a ms y encuentro oro
11. implemento una version naive que use también ms como benchmark
12. solo fallan un 0.39% de los tests con un error de 1ms, parece asumible.
13. elijo numpy_v2 por tener menor er
"""
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from functools import lru_cache


def naive(datenum):
    """Caching version"""
    datenum_int = int(datenum)
    datenum_rest = datenum % 1

    out_datetime = (
        datetime.fromordinal(datenum_int)
        + timedelta(days=datenum_rest)
        - timedelta(days=366)
    )
    return out_datetime


def naive_ms(datenum):
    """Caching version"""
    day2ms = 86400000
    datenum_int = int(datenum)
    datenum_rest = int((datenum % 1) * day2ms)

    out_datetime = (
        datetime.fromordinal(datenum_int)
        + timedelta(milliseconds=datenum_rest)
        - timedelta(days=366)
    )
    return out_datetime


@lru_cache(maxsize=int(1e4))
def naive_caching(datenum):
    """Caching version"""
    return naive(datenum)


def map_naive_caching(datenum_list):
    """For loop version"""
    return [naive_caching(mdt) for mdt in datenum_list]


def map_naive_ms(datenum_list):
    """For loop version"""
    return [naive_ms(mdt) for mdt in datenum_list]

"""
Vectorized version of datenum2datetime using numpy
"""

def numpy_v1(datenum, pandas=False):
    """First multiply then substract"""
    # issue : https://github.com/numpy/numpy/issues/16689
    unit_to = 86400000  # ms
    MAT_ORIGIN_TIME = 719529
    datenum_arr = np.array(datenum, np.float64)
    # HERE IS THE ISSUE
    datenum_ns_arr = datenum_arr * unit_to - MAT_ORIGIN_TIME * unit_to
    return datenum_ns_arr.astype(int).astype("datetime64[ms]")


def numpy_v2(datenum, pandas=False):  # winer
    """Fist substract then multply"""
    # issue : https://github.com/numpy/numpy/issues/16689
    unit_to = 86400000  # ms
    MAT_ORIGIN_TIME = 719529
    datenum_arr = np.array(datenum, np.float64)
    datenum_ns_arr = (datenum_arr - MAT_ORIGIN_TIME) * unit_to
    return datenum_ns_arr.astype(np.int64).astype("datetime64[ms]")


def check_values(obtained, expected, only_fails=True, name=None):
    diff = (obtained - expected).astype(int)
    out = pd.DataFrame([obtained, expected, diff]).T
    print("=" * 40)
    print("Checking %s" % name)

    try:
        np.testing.assert_equal(obtained, expected)
    except Exception as e:
        print(e)

    if only_fails:
        failed = abs(diff) > 1e-12
        return out.loc[failed]

    return out



if __name__ == '__main__':
    """
    %run datenum2datetime.py

    # performance
    %timeit map_naive_caching(datenum_collection)  # actual
    %timeit map_naive_ms(datenum_collection)  # benchmark
    %timeit numpy_v1(datenum_collection)   # alternative
    %timeit numpy_v2(datenum_collection)   # alternative


    >>> %timeit map_naive_caching(datenum_collection)  # actual
    2.46 ms ± 60.8 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

    >>> %timeit map_naive_ms(datenum_collection)  # benchmark
    26.5 ms ± 2.66 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

    >>> %timeit numpy_v1(datenum_collection)   # alternative
    28.2 µs ± 401 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

    >>> %timeit numpy_v2(datenum_collection)   # alternative
    28 µs ± 241 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)


    | DATE                         | datenum | datetime64 |
    | : -------------------------  | :------:| :---------:|
    | datetime(1970, 1, 1, 0, 0)   | 719529  | 0          |
    """
    # -------------------------------------------------------------------------
    # TEST
    # obtained
    datenum_collection = np.linspace(721965, 731965, 10000)

    # naive_dt_list = map_naive_caching(datenum_collection)
    naive_dt_list = map_naive_ms(datenum_collection)

    np_dt_list1 = numpy_v1(datenum_collection)
    np_dt_list2 = numpy_v2(datenum_collection)

    # expected
    expected = np.array(naive_dt_list).astype("datetime64[ms]")
    # __import__('pdb').set_trace()


    check = check_values(expected, np_dt_list1, True, "bench vs numpy_v1")
    check = check_values(expected, np_dt_list2, False, "bench vs numpy_v2")
    check = check_values(np_dt_list1, np_dt_list2, True, "numpy_v1 vs numpy_v2")
