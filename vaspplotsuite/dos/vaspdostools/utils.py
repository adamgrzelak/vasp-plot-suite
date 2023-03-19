import numpy as np

from .dostypes import Dos
from .dostypes import RawDos


def extract(directory):
    """
    Reads DOS from VASP output \n
    See DOS class for more information \n
    :param directory:
    :return: DOS
    """
    return RawDos(directory)


def open_file(path, name=None):
    """
    Reads DOS from previously saved .csv \n
    :param str path: location
    :param str name: name for the system
    :return: Dos
    """
    dos_array = np.genfromtxt(path, delimiter=",", dtype=np.float64)
    if name is None:
        name = path.split(".")[-1]
    return Dos(dos_array, name)
