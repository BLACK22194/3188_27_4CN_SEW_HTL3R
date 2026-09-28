"""
Modul-Dokumentation
"""
# Metadaten zu dieser Datei:
__author__ = "Mahdi Danesh"
__example__ = "SEW4/UE01/01"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "24.09.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"
__status__ = "Released"


def collatz_sequence(number: int) -> list[int]:
    """
    :param number: Startzahl
    :return: Collatz Zahlenfolge, resultierend aus n
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    if number == 1:
        return [1]
    if number % 2 == 0:
        new_number = number // 2
    else:
        new_number = number * 3 + 1
    return [number] + collatz_sequence(new_number)


def longest_collatz_sequence(n: int) -> tuple[int, int]:
    """
    :param number: Startzahl
    :return: Startwert und Länge der längsten Collatz Zahlenfolge deren Startwert <=n ist
    >>> longest_collatz_sequence(100)
    (97, 119)
    """
    long_col: list[int] = [0, 0]
    for i in range(1, n):
        if len(collatz_sequence(i)) > long_col[1]:
            long_col[0] = i
            long_col[1] = len(collatz_sequence(i))
    return long_col[0], long_col[1]


def collatz_sequence_p(number: int, p: int = 3) -> list[int]:
    """
    Bonus-Aufgabe
    :param number: Startzahl
    :return: Collatz Zahlenfolge, resultierend aus n
    >>> collatz_sequence_p(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence_p(3, p=5)
    [3, 16, 8, 4, 2, 1]
    """
    if number == 1:
        return [1]
    if number % 2 == 0:
        new_number = number // 2
    else:
        new_number = number * p + 1
    return [number] + collatz_sequence_p(new_number, p)
