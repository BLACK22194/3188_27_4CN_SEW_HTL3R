"""
Modul-Dokumentation
"""
from time import time

# Metadaten zu dieser Datei:
__author__ = "Mahdi Danesh"
__example__ = "SEW4/UE01/03"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "24.09.2026"
__license__ = "GNU GPLv3"


def mcarthy_91_function_M(n: int) -> int:
    """
      Klassische McCarthy-91-Funktion.
      >>> mcarthy_91_function_M(99)
      91
      >>> mcarthy_91_function_M(102)
      92
      """
    if n <= 100:
        return mcarthy_91_function_M(mcarthy_91_function_M(n + 11))
    else:
        return n - 10


def main():
    """
       Generiert eine Liste und ein Dictionary mit den ersten 200 Elementen
       der McCarthy-91-Funktion und misst dabei die benoetigte Zeit.

       Was ist bemerkenswert beim Ergebnis dieser Funktion?
       -> Fuer alle Eingabewerte n <= 101 ist das Ergebnis immer konstant 91.

       Wie lange dauert die Berechnung?
       -> Die Dauer wird als Float in Sekunden zurueckgegeben (unter 1 Millisekunde).

       :return: Ein Tupel bestehend aus:
                - m_list: Liste der Ergebnisse fuer n von 0 bis 199
                - m_dict: Dictionary mit n als Key und M(n) als Value
                - dauer: Die gemessene Berechnungszeit in Sekunden

       >>> m_list, m_dict, _ = main()
       >>> len(m_list)
       200
       >>> len(m_dict)
       200
       >>> m_dict[0]
       91
       >>> m_dict[102]
       92
    """
    t0 = time()
    m_list: list[int] = []
    for i in range(200):
        m_list.append(mcarthy_91_function_M(i))

    m_dict: dict[int, int] = {}
    for i in range(200):
        m_dict[i] = mcarthy_91_function_M(i)

    t1 = time()
    dauer = t1 - t0
    pass


if __name__ == "__main__":
    main()
