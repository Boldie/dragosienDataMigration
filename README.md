Skript zum migrieren der Daten aus Greasemonkey nach Violentmonkey für Dragosien Resourceninitkator Skript
==========================================================================================================

1. Skript aus Greasemonkey herauskopieren und  in Violentmonkey installieren
2. Unter Einstellungen in Violentmonkey das Skript inkl. der Skriptdaten exportieren. Man erhält dann eine Datei, die man u.u. noch umbenennen muss. Die Endung muss .zip lauten.
3. Datei entpacken, es sollten 2 Dateien im .zip vorhanden sein: violentmonkey, Dragosien Resourcenindikatoren.user.js; Als Ziel am Besten das Verzeichniss, wo auch diese readme zu finden ist.
4. Nach der alten Datenbank suchen: Dragosien_Resourcenindikatoren.db welches unter dem Firefoxprofil (unter Linux z.B. unter ~/.mozilla/firefox/8asff747f.default-14444554003/) unter dem Verzeichnis gm_scripts abgelegt ist. Am einfachsten ist es, wenn dies in das Verzeichniss mit den entpackten Dateien reinkopiert wird.
5. dragMigrate.py aufrufen
6. Die Datei violentmonkey, Dragosien Resourcenindikatoren.user.js wieder in ein .zip Archiv packen.
7. Import des neuen .zip files in Violentmonkey. Wenn es erfolgreich war, Dragosien neu laden und nachsehen, ob die alten Daten wieder da sind.


