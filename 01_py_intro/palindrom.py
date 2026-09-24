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
"""
# Metadaten zu dieser Datei:
__author__ = "Mahdi Danesh"
__example__ = "SEW4/01/F1"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
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

