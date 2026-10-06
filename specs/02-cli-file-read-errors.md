# Spec: CLI-Dateifehler verständlich behandeln

## 1. Ziel

Wenn die CLI eine angegebene Markdown-Datei nicht lesen kann, soll sie eine verständliche Fehlermeldung statt eines Python-Tracebacks ausgeben. So kann der Nutzer das Problem erkennen und beheben.

## 2. Scope & Story-Größe

- **In Scope:** Erwartbare Fehler beim Prüfen, Öffnen oder Lesen einer per Dateipfad angegebenen Datei, einschließlich fehlender Datei, fehlender Leseberechtigung, ungültiger UTF-8-Daten und vergleichbarer erwartbarer Dateizugriffsfehler.
- **Out of Scope:** Änderungen an der Task-Erkennung, Schreibzugriffe auf Dateien, neue Abhängigkeiten und Änderungen am Verhalten der Stdin-Eingabe.

## 3. Bestehender Code & Wiederverwendung

- **Zu prüfende Module:** `src/task_extractor/cli.py`, insbesondere die Datei-Eingabe über `Path.read_text`.
- **Tests:** `tests/test_task_extractor.py` verwendet bereits `unittest` und subprocess-basierte CLI-Tests.
- **Dependencies:** Keine neuen; die Python-Standardbibliothek genügt.

## 4. Anforderungen

- **REQ-1:** Erwartbare Fehler beim Prüfen, Öffnen oder Lesen einer angegebenen Datei werden abgefangen und als verständliche Meldung auf `stderr` ausgegeben.
- **REQ-2:** Bei einem solchen Fehler beendet sich die CLI mit Exit-Code `1` und gibt keinen Traceback aus. Bei erfolgreichem Lesen bleibt das bisherige Verhalten unverändert.

## 5. Akzeptanzkriterien

- [ ] Eine nicht vorhandene Datei führt weiterhin zu einer verständlichen Fehlermeldung und Exit-Code `1`.
- [ ] Ein Fehler beim Lesen, zum Beispiel `PermissionError`, erzeugt eine verständliche Fehlermeldung, Exit-Code `1` und keinen Traceback.
- [ ] Eine Datei mit ungültigem UTF-8 wird kontrolliert abgewiesen: verständliche Meldung, Exit-Code `1`, kein Traceback.
- [ ] Erfolgreiches Lesen liefert weiterhin die erwarteten Aufgaben und das bisherige Ausgabe- und Exit-Code-Verhalten.
- [ ] Tests decken Fehlerfälle zuverlässig ab, ohne von besonderen Betriebssystem-Berechtigungen der Testumgebung abhängig zu sein.

## 6. Verifikation

- **Befehl:** `python3 -m unittest discover -s tests -v`
- **Erwartetes Ergebnis:** Alle Tests bestehen; keine zusätzlichen Abhängigkeiten.
