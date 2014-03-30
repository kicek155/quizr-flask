Quizr
=====

Aplikacja pozwalająca na rozwiązywanie quizów. 

To jest tylko szkielet aplikaji, jaką studenci muszą rozwinąć w ramach ćwiczeń
podczas podyplomowych studiów "Programowanie aplikacji internetowych" na Wyższej
Szkole Nauk Humanistycznych i Dziennikarstwa w Poznaniu.


Instalacja
----------

Wejdź na github do [repozytorium projektu](https://github.com/sargo/quizr-flask)
i stwórz forka.

Następnie przygotuj virtualenv i sklonuj Twojego forka repozytorium:

```
source /opt/python/2.7/bin/virtualenvwrapper.sh
mkvirtualenv --python=/opt/python/2.7/bin/python quizr-flask
cdvirtualenv
git clone git@github.com:username/quizr-flask.git
cd quizr-flask
pip install -r requirements.txt
```

Użycie
------

Przygotowanie do pracy:

```
workon quizr-flask
cdvirtualenv
cd quizr-flask
```

Uruchomienie aplikacji:

```
python quizr
```

Uruchomienie testów jednostkowych:

```
python quizr_tests
```

Treść zadania
-------------

Należy stworzyć aplikację, dzięki której użytkownik będzie mógł wziąć udział 
w quizie. Użytkownik, po wejściu na stronę główną powinien zobaczyć krótki opis
zasad quizu, pole do wpisania swojego pseudonimu oraz przycisk “Start”. Po
rozpoczęciu, aplikacja losuje jedno z pytań i pokazuje je użytkownikowi wraz z
możliwymi odpowiedziami. Po udzieleniu odpowiedzi przez użytkownika, losowane
jest kolejne pytanie (nie są brane pod uwagę pytania które wcześniej padły). Po 
dzieleniu odpowiedzi na 5 pytanie, użytkownikowi pokazywany jest ekran
podziękowania, wraz z ilością zdobytych punktów wraz z maksymalną wartością
oraz jako procent maksymalnej wartości - przykład 12 / 15 (80%).

Punktacja:
 * 3 punkty za poprawną odpowiedź w czasie krótszym niż 10 sekund od wyświetlenia pytania
 * 2 punkty za poprawną odpowiedź w pomiędzy 10 a 30 sekundą od wyświetlenia pytania
 * 1 punkt za poprawną odpowiedź w czasie powyżej 30 sekund

Pytania mogą mieć 2 do 5 możliwych odpowiedzi, ale tylko jedna jest prawidłowa.
Pytania do quizu aplikacja pobierać będzie z pliku w formacie CSV.
Przykładowy plik znajduje się w folderze `data`.

Struktura CSV:
 * Pierwsza kolumna - pytanie
 * Ostatnia kolumna - prawidłowa odpowiedź (wartość A, B, C, D lub E)
 * Pozostałe kolumny - możliwe odpowiedzi
 
Aplikacja powinna posiadać testy jednostkowe.
