# bindiff
BinDiff vergleicht zwei Ordner mit Unterordnern.
Zunächst wird geprüft, ob der Inhalt beider Ordner nach Namen und Datei-Größen identisch ist,
dann prüft das Programm binäre darauf, ob Quelle und Ziel identisch sind.

Ich verwende es, um kopien von Filmordnern mit dem Original zu vergleichen.
Da es nur privat genutzt wird, habe ich die Parameter "primPath" und "secPath"
als globale Variablem im Programm hart vergeben und nicht über die Command-Line vefügbar gemacht.
Das Logging erfolgt auf der Konsole.
Das Programm ist durch die Nutzung von ANSI-Sequenzen etwas aufgehübscht. (Über Geschmack kann man streiten...)

ruegi
