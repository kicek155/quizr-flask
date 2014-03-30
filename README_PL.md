Quizr
=====

Aplikacja pozwalaj¹ca na rozwi¹zywanie quizów. 

To jest tylko szkielet aplikaji, jak¹ studenci musz¹ rozwin¹æ w ramach æwiczeñ
podczas podyplomowych studiów "Programowanie aplikacji internetowych" na Wy¿szej
Szkole Nauk Humanistycznych i Dziennikarstwa w Poznaniu.


Instalacja
----------

WejdŸ na github do [repozytorium projektu](https://github.com/sargo/quizr)
i stwórz forka.

Nastêpnie przygotuj virtualenv i sklonuj Twojego forka repozytorium:

```
source /opt/python/2.7/bin/virtualenvwrapper.sh
mkvirtualenv --python=/opt/python/2.7/bin/python quizr
cdvirtualenv
git clone git@github.com:username/quizr.git
cd quizr
pip install -r requirements.txt
```

U¿ycie
------

Przygotowanie do pracy:

```
workon quizr
cdvirtualenv
cd quizr
```

Uruchomienie aplikacji:

```
python quizr
```

Uruchomienie testów jednostkowych:

```
python quizr_tests
```

Treœæ zadania
-------------

Nale¿y stworzyæ aplikacjê, dziêki której u¿ytkownik bêdzie móg³ wzi¹æ udzia³ 
w quizie. U¿ytkownik, po wejœciu na stronê g³ówn¹ powinien zobaczyæ krótki opis
zasad quizu, pole do wpisania swojego pseudonimu oraz przycisk “Start”. Po
rozpoczêciu, aplikacja losuje jedno z pytañ i pokazuje je u¿ytkownikowi wraz z
mo¿liwymi odpowiedziami. Po udzieleniu odpowiedzi przez u¿ytkownika, losowane
jest kolejne pytanie (nie s¹ brane pod uwagê pytania które wczeœniej pad³y). Po 
dzieleniu odpowiedzi na 5 pytanie, u¿ytkownikowi pokazywany jest ekran
podziêkowania, wraz z iloœci¹ zdobytych punktów wraz z maksymaln¹ wartoœci¹
oraz jako procent maksymalnej wartoœci - przyk³ad 12 / 15 (80%).

Punktacja:
 * 3 punkty za poprawn¹ odpowiedŸ w czasie krótszym ni¿ 10 sekund od wyœwietlenia pytania
 * 2 punkty za poprawn¹ odpowiedŸ w pomiêdzy 10 a 30 sekund¹ od wyœwietlenia pytania
 * 1 punkt za poprawn¹ odpowiedŸ w czasie powy¿ej 30 sekund

Pytania mog¹ mieæ 2 do 5 mo¿liwych odpowiedzi, ale tylko jedna jest prawid³owa.
Pytania do quizu aplikacja pobieraæ bêdzie z pliku w formacie CSV.
Przyk³adowy plik znajduje siê w folderze `data`.

Struktura CSV:
 * Pierwsza kolumna - pytanie
 * Ostatnia kolumna - prawid³owa odpowiedŸ (wartoœæ A, B, C, D lub E)
 * Pozosta³e kolumny - mo¿liwe odpowiedzi
 
Aplikacja powinna posiadaæ testy jednostkowe.



