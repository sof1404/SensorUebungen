"""
SensorPy – Messdaten analysieren
=================================
Dieses Modul enthält alle Funktionen zur Analyse von Umweltmessdaten.

Aufgabe: Implementiert jede Funktion so, dass sie der Beschreibung
im Docstring entspricht. Die Signatur (Name, Parameter, Rückgabetyp)
darf NICHT verändert werden.

Datenformat (eine Zeile aus messdaten.csv als dict):
    {
        "sensor_id":       "S01",
        "timestamp":       "2024-03-01 08:00",
        "temperatur":      19.2,
        "luftfeuchtigkeit": 52.1,
        "co2":             480.0
    }
"""

import csv


# ──────────────────────────────────────────────────────────────
# PERSON A
# ──────────────────────────────────────────────────────────────

def load_data(filename: str) -> list[dict]:
    """Liest eine CSV-Datei mit Messdaten ein und gibt sie als Liste zurück.

    Jede Zeile der CSV wird in ein dict umgewandelt.
    Numerische Felder (temperatur, luftfeuchtigkeit, co2) werden
    automatisch in float konvertiert.

    Args:
        filename: Pfad zur CSV-Datei (z. B. "data/messdaten.csv")

    Returns:
        Liste von dicts, eines pro Zeile. Leere Liste bei Fehler.

    Beispiel:
        >>> daten = load_data("data/messdaten.csv")
        >>> print(daten[0]["sensor_id"])
        S01
        >>> print(daten[0]["temperatur"])
        19.2
    """
    # TODO: Implementierung hier einfügen
    try:
        data = []

        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["temperatur"] = float(row["temperatur"])
                row["luftfeuchtigkeit"] = float(row["luftfeuchtigkeit"])
                row["co2"] = float(row["co2"])

                data.append(row)

        return data

    except (FileNotFoundError, KeyError, ValueError):
        return []


def calculate_average(values: list[float]) -> float:
    """Berechnet den Durchschnitt einer Liste von Zahlen.

    Args:
        values: Liste mit float-Werten (darf nicht leer sein)

    Returns:
        Arithmetisches Mittel aller Werte, gerundet auf 2 Dezimalstellen.

    Beispiel:
        >>> calculate_average([10.0, 20.0, 30.0])
        20.0
        >>> calculate_average([19.2, 21.4, 24.7])
        21.77
    """
    # TODO: Implementierung hier einfügen
    return round(sum(values) / len(values), 2)


def find_extremes(values: list[float]) -> tuple[float, float]:
    """Findet den kleinsten und grössten Wert einer Liste.

    Args:
        values: Liste mit float-Werten (darf nicht leer sein)

    Returns:
        Tupel (minimum, maximum)

    Beispiel:
        >>> find_extremes([19.2, 21.4, 24.7, 17.5])
        (17.5, 24.7)
    """
    # TODO: Implementierung hier einfügen
    return (min(values), max(values))


def count_above_threshold(values: list[float], threshold: float) -> int:
    """Zählt, wie viele Werte in der Liste den Schwellenwert überschreiten.

    Args:
        values:    Liste mit float-Werten
        threshold: Schwellenwert (Werte > threshold werden gezählt)

    Returns:
        Anzahl der Werte, die strikt grösser als threshold sind.

    Beispiel:
        >>> count_above_threshold([19.2, 27.1, 24.7, 33.2, 21.4], 25.0)
        2
    """
    # TODO: Implementierung hier einfügen
    count = 0

    for value in values:
        if value > threshold:
            count += 1

    return count


# ──────────────────────────────────────────────────────────────
# PERSON B
# ──────────────────────────────────────────────────────────────

def classify_value(value: float, limits: dict) -> str:
    """Klassifiziert einen Messwert anhand von Grenzwerten..

    Die limits-dict hat folgende Struktur:
        {
            "niedrig":  <obere Grenze für "niedrig">,
            "normal":   <obere Grenze für "normal">,
            "hoch":     <obere Grenze für "hoch">
            # alles darüber gilt als "kritisch"
        }

    Args:
        value:  Der zu klassifizierende Messwert
        limits: Dict mit den Grenzwerten (siehe oben)

    Returns:
        Einen der folgenden Strings: "niedrig", "normal", "hoch", "kritisch"

    Beispiel (Temperatur-Grenzen: niedrig<18, normal<26, hoch<32):
        >>> grenzen = {"niedrig": 18.0, "normal": 26.0, "hoch": 32.0}
        >>> classify_value(15.0, grenzen)
        'niedrig'
        >>> classify_value(22.0, grenzen)
        'normal'
        >>> classify_value(28.5, grenzen)
        'hoch'
        >>> classify_value(35.0, grenzen)
        'kritisch'
    """
    # TODO: Implementierung hier einfügen
    def classify_value(value: float, limits: dict) -> str:
        if value < limits["niedrig"]:
            return "niedrig"
        elif value < limits["normal"]:
            return "normal"
        elif value < limits["hoch"]:
            return "hoch"
        else:
            return "kritisch"

    pass


def filter_by_sensor(data: list[dict], sensor_id: str) -> list[dict]:
    """Filtert die Messdaten nach einer bestimmten Sensor-ID.

    Args:
        data:      Liste von Messdaten-dicts (Ausgabe von load_data)
        sensor_id: Sensor-ID, nach der gefiltert werden soll (z. B. "S01")

    Returns:
        Neue Liste, die nur Einträge mit der angegebenen sensor_id enthält.
        Leere Liste, wenn kein passender Eintrag gefunden wird.

    Beispiel:
        >>> daten = load_data("data/messdaten.csv")
        >>> s01 = filter_by_sensor(daten, "S01")
        >>> all(d["sensor_id"] == "S01" for d in s01)
        True
    """
    # TODO: Implementierung hier einfügen
    def filter_by_sensor(data: list[dict], sensor_id: str) -> list[dict]:
        return [entry for entry in data if entry["sensor_id"] == sensor_id]

    pass


def generate_report(data: list[dict]) -> str:
    """Erstellt einen Textbericht aus den Messdaten.

    Der Bericht enthält:
    - Gesamtanzahl der Messungen
    - Durchschnitt, Min und Max für Temperatur, Luftfeuchtigkeit und CO2
    - Anzahl der kritischen Temperaturmessungen (> 30 °C)
    - Liste aller vorhandenen Sensor-IDs

    Args:
        data: Liste von Messdaten-dicts (Ausgabe von load_data)

    Returns:
        Formatierter mehrzeiliger String.

    Beispiel-Output (gekürzt):
        ========== SensorPy Bericht ==========
        Messungen total:       36
        Sensoren:              S01, S02

        -- Temperatur (°C) --
        Durchschnitt:          22.48
        Min / Max:             15.9 / 33.2
        Kritische Werte (>30): 2

        -- Luftfeuchtigkeit (%) --
        ...
        ======================================
    """
    # TODO: Implementierung hier einfügen
    temps = [d["temperature"] for d in data]

    def generate_report(data: list[dict]) -> str:
        temps = [d["temperature"] for d in data]
    hums = [d["humidity"] for d in data]
    co2s = [d["co2"] for d in data]
    krit_temp = sum(1 for t in temps if t > 30)
    sensoren = sorted({d["sensor_id"] for d in data})

    report = []
    report.append("========== SensorPy Bericht ==========")
    report.append(f"Messungen total:       {len(data)}")
    report.append(f"Sensoren:              {', '.join(sensoren)}")
    report.append("")
    report.append("-- Temperatur (°C) --")
    report.append(f"Durchschnitt:          {sum(temps)/len(temps):.2f}")
    report.append(f"Min / Max:             {min(temps):.1f} / {max(temps):.1f}")
    report.append(f"Kritische Werte (>30): {krit_temp}")
    report.append("")
    report.append("-- Luftfeuchtigkeit (%) --")
    report.append(f"Durchschnitt:          {sum(hums)/len(hums):.2f}")
    report.append(f"Min / Max:             {min(hums):.1f} / {max(hums):.1f}")
    report.append("")
    report.append("-- CO2 (ppm) --")
    report.append(f"Durchschnitt:          {sum(co2s)/len(co2s):.2f}")
    report.append(f"Min / Max:             {min(co2s):.0f} / {max(co2s):.0f}")
    report.append("======================================")

    return "\n".join(report)

    pass

