# Aplikacja mobilna

Do uruchomienia aplikacji jest wymagany [flutter](https://flutter.dev/?gclid=Cj0KCQiA9P__BRC0ARIsAEZ6irg155LD24W7_zmf0NJm1xpsJRnM5FYLFVfxbYGpXRSgIfEsdaWOuCoaApMPEALw_wcB&gclsrc=aw.ds) i skonfigurowanie komendy flutter. 

Aplikacje flutter uruchamia się za pomocą komendy będąc w tym samym folderze co pubspec.yaml:
```
flutter run 
```
Po dokładniejszą konfiguracje odsyłam do docs.

Aplikacja korzysta z Map Google i do poprawnego działania wymaga klucha Api. Klucz należy umieścić w pliku android/local.properties dodając linijkę:
```
MAPS_API_KEY=<klucz google>
```
W przypadku ios klucz należy umieścić w pliku ios/Runner/AppDelegate.swift:
```swift
GMSServices.provideAPIKey("<klucz google>")
```
Po klucz api można się zgłosić do autora tego repozytorium lub stworzyć własny.


Również do poprawnego korzystania z aplikacji należy ustawić poprawny adres ip serwera w pliku lib/service/planner. Aktualny adres jest poprawny dla używania serwera działającego lokalnie na maszynie i symulatorze androida.

## Działanie aplikacji

Aplikacja składa się z jednego ekranu na którym dodajmy przystanki na trasie poprzez tapniecie na mapie w odpowiednim miejscu. Przycisk Find route wysyła request do serwera i oczekuje na najlepszą trasę pomiędzy punktami, zaczynając od własnej lokalizacji jako punktu startowego. Gdy serwer zwróci trasę zostaje ona narysowana na mapie.

