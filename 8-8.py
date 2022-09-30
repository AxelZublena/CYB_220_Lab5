# 8.8
def make_album(artist, title, song_number=None):
    dict = {"artist": artist, "title": title}
    if song_number:
        dict["song_number"] = song_number

    return dict

album1 = make_album("Iliona", "Tete Brulee")
album2 = make_album("Lomepal", "Mauvais Ordre")
album3 = make_album("Kanye West", "Donda")

album4 = make_album("Angele", "Nonante-Cinq", 12)

print(album1)
print(album2)
print(album3)
print(album4)

while True:
    artist = input("\nPlease provide the artist's name: ")
    title = input("Please provide the artist's album name ('q' to quit): ")

    if title == "q":
        break

    album = make_album(artist=artist, title=title)
    print(album)

