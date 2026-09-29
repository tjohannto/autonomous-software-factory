# Spec: Markdown Task Extractor CLI

## 1. Ziel (Goal)
Entwicklung eines leichtgewichtigen Python-CLI-Tools, das Markdown-Dateien oder Text analysiert und alle offenen Aufgaben (`- [ ]`) herausfiltert und sauber ausgibt.

## 2. Scope & Story-Größe (User Story Level)
* **In Scope:**
  * Parsing von Text oder Dateien nach offenen Markdown-Aufgaben (`- [ ]` oder `* [ ]`).
  * Ausgabe der offenen Tasks als nummerierte Liste oder als JSON (via Flag `--json`).
  * Sauberes Handling, wenn keine Tasks gefunden wurden oder die Datei nicht existiert.
* **Out of Scope:**
  * Modifizieren von Dateien (z. B. Tasks abhaken).
  * Verschachtelte Kanban-Boards oder HTML-Rendering.

## 3. Bestehender Code & Wiederverwendung (Code Reuse First)
* **Zu prüfende / wiederverwendbare Module:** 
  * Standardbibliothek (`argparse`, `re`, `json`, `pathlib`, `sys`). Keine externen Schwergewicht-Dependencies nötig.
* **Refactoring bestehender Komponenten:**
  * Keine (Neues Modul unter `src/task_extractor/`).

## 4. Anforderungen (Requirements)
* **REQ-1:** Der Extractor erkennt alle offenen Tasks im Format `- [ ] <Text>` und `* [ ] <Text>` (auch mit führenden Leerzeichen). Erledigte Tasks (`- [x]`) werden ignoriert.
* **REQ-2:** CLI unterstützt zwei Modi: Text via Stdin ODER Dateipfad als Argument.
* **REQ-3:** Ausgabe standardmäßig als Textliste, mit `--json` als JSON-Array von Strings.

## 5. Akzeptanzkriterien (Woran erkenne ich, dass es fertig ist?)
* **Zu REQ-1:** 
  - [ ] Gibt ein Array der extrahierten Task-Texte zurück (ohne die Checkbox-Syntax).
  - [ ] Erledigte Tasks mit `[x]` oder `[X]` werden nicht erfasst.
* **Zu REQ-2:** 
  - [ ] Übergabe einer existierenden Markdown-Datei liefert deren Tasks.
  - [ ] Nicht-existierende Datei erzeugt Exit-Code 1 mit verständlicher Fehlermeldung.
* **Zu REQ-3:** 
  - [ ] Flag `--json` erzeugt valides JSON: `["Task 1", "Task 2"]`.

## 6. Verifikation (QA Check)
* **Command:** `python3 -m unittest discover -s tests -v`
* **Erwartung:** Alle Tests grün, 0 Fehler, keine Sicherheitswarnungen.
