# Backend

Do zbudowania aplikacji potrzebne jest środowisko zainstalowane anaconda lub [miniconda](https://docs.conda.io/en/latest/miniconda.html).

Następnie, potrzebujemy wszystkich zależności aplikacji.

- Dla Windows:
    ```
    conda env crate -f environment.yml
    ```
- Dla MacOS:
    ```
    conda env crate -f environment_macos.yml
    ```
Po poprawnym stworzeniu środowiska należy je aktywować:
```
conda activate <nazwa środowiska>
```

Teraz już można uruchomić serwer. Będąc w folderze z plikiem manage.py:
```
python manage.py runserver
```

Server jest dostępny pod tym [adresem](http://localhost:8000/planner). Jednak aby uzyskać odpowiedź trzeba podać jakieś body w Request. Można to robić np. za pomocą aplikacji [Insomnia](https://insomnia.rest/).

Testy odpala się za pomocą:
```
python manage.py test planner
```