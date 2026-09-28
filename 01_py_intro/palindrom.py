"""
Modul-Dokumentation

>>> is_palindrom("9009")
True
>>> is_palindrom("1223")
False
>>> is_palindrom_sentence("Wasser")
False
>>> is_palindrom_sentence("Was it a car or a cat I saw?")
True
>>> palindrom_product(100000)
99999
>>> get_dec_hex_palindrom(100000)
99599
"""
# Metadaten zu dieser Datei:
__author__ = "Mahdi Danesh"
__example__ = "SEW4/UE01/01"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "24.09.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"
__status__ = "Released"


def is_palindrom(s: str) -> bool:
    return s == s[::-1]


def is_palindrom_sentence(s: str) -> bool:
    s = s.upper()
    text: str = ""
    for i in s:
        if i != " " and i != "?" and i != "!" and i != ".":
            text += i
    if is_palindrom(text):
        return True
    else:
        return False


def palindrom_product(x: int) -> int:
    big: int = 0
    for j in range(100, 1000):
        for k in range(100, 1000):
            if x >= j * k > big:
                if is_palindrom(str(j * k)):
                    big = j * k
    return big


def get_dec_hex_palindrom(x: int) -> int:
    big: int = 0
    for i in range(x):
        if is_palindrom(str(i)) and is_palindrom(to_base(i, 16)) and i > big:
            big = i
    return big

def to_base(number: int, base: int) -> str:
    """
    :param number: Zahl im 10er-Syste,
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    >>> to_base(1234,16)
    '4D2'
    """
    hexz: str = ""
    while number % base != 0:
        for i in range(16):
            if i == 10 and number % base == i:
                hexz += "A"
            elif i == 11 and number % base == i:
                hexz += "B"
            elif i == 12 and number % base == i:
                hexz += "C"
            elif i == 13 and number % base == i:
                hexz += "D"
            elif i == 14 and number % base == i:
                hexz += "E"
            elif i == 15 and number % base == i:
                hexz += "F"
            elif number % base == i:
                hexz += str(i)
        number = number // base
    hexz = hexz[::-1]
    return hexz
