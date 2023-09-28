"""
pip - pip installs packages - instalator pakunków

PyPi - Python Package index - indeks (spis) pakunków do Pythona

pip - pip install packages - instalator pakunków

PyPi - Python Package index - indeks(spis) pakunków dla Pythona

requests - (z ang.) żądania

http - protokół (reguły komunikacji między użytkownikiem, a serwerem)


Aby zainstalować pakunek:

W menu Startu otwieramy Microsoft Power Shell i wpisujemy: pip install requests

Od teraz możemy importować requests

    import requests
           response = requests.get("http://videokurs.pl")


Metoda get pozwala nam pobrać stronę internetową.

Gdy wpiszemy w Shell response wyświetlą się właściwości z których możemy skorzystać:

.status_code - sprawdza status strony

               response.status_code

           Są różne statusy, m.in.:
           200 - wszystko OK, strona istnieje (została pobrana)
           404 - błąd, strona nie istnieje

.text - pobiera stronę w wersji tekstowej

              response.text


"""

import requests

response = requests.get("https://hupla.pl/")

print(response.text)

