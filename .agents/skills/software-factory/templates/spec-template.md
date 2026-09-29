# Spec: [Feature/Story-Name]

## 1. Ziel (Goal)
[1-2 Sätze: Welches konkrete Problem lösen wir in dieser Story und warum?]

## 2. Scope & Story-Größe (User Story Level)
* **In Scope:** [Max. 1-3 zusammenhängende Anforderungen]
* **Out of Scope:** [Alles, was in Folge-Stories oder spätere Epics gehört]

## 3. Bestehender Code & Wiederverwendung (Code Reuse First)
* **Zu prüfende / wiederverwendbare Module:** 
  * [z. B. src/utils/formatters.ts, src/components/Button, src/services/auth.service]
* **Refactoring bestehender Komponenten:**
  * [Ja / Nein - Was muss erweitert oder angepasst werden, ohne Bestandsfunktionen zu brechen?]

## 4. Anforderungen (Requirements)
Die fachlichen Funktionen (max. 1–3 pro Story):
* **REQ-1:** [Fachliche Anforderung]
* **REQ-2:** [Fachliche Anforderung]

## 5. Akzeptanzkriterien (Woran erkenne ich, dass es fertig ist?)
Direkt an die Requirements gekoppelt – aus Nutzersicht prüfbar:
* **Zu REQ-1:** 
  - [ ] [Sichtbares / prüfbares Verhalten aus Nutzersicht]
* **Zu REQ-2:** 
  - [ ] [Sichtbares / prüfbares Verhalten aus Nutzersicht]

## 6. Verifikation (QA Check)
* **Command:** [z. B. npm test / pytest]
* **Erwartung:** [Alle bestehenden Regressionstests UND neuen Tests grün, 0 Linter-Warnungen]
