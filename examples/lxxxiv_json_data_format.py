"""

json.dumps(data) - zapisuje dane do postaci Stringowej json
json.dump(data, nameOfFileHandler, ensure_ascii=False) -
                               zapisuje dane do pliku w postacji json

dump z ang. zsypać/zwalić/zrzucać
"""

import json

film = {
    "title" : "Alen",
    "release_year" : 1979,
    "won_oscar" : True,
    "actors": (" Sigourney Weaver", "Tom Skerritt"),
    "budget" : 11000000,
    "credits" : {
            "director" : "Ridley Scott",
            "writer" : "Dan O’Bannon"

            },
    "test" : "ąśęółńćżź"
}

encodedFilm = json.dumps(film, ensure_ascii=False, indent=4, sort_keys=True)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False)
"""

"""
print(encodedFilm)

encodedRetrivedMovie = encodedFilm
print(encodedRetrivedMovie)
decodedMovie = json.loads(encodedRetrivedMovie)
print(decodedMovie)

with open("sample.json", encoding="UTF-8") as file:
    wynik = json.load(file)

print(wynik)
print(json.dumps(wynik, ensure_ascii=False, indent=4))

import pprint

pprint.pprint(wynik)
