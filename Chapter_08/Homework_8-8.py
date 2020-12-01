def make_album(artist, album, songs= ""):

    album_dictionary = {"artist": f"{artist.title()}",
    "album": f"{album.title()}"}

    if songs:
        album_dictionary["songs"] = f"{songs}"

    else:
        formatted_album = f"{album.title()} is by {artist.title()}."
    return album_dictionary

while True:
    user_artist = input("Artist of album: ")
    user_album = input("Album: ")

    user_formatted_album = make_album(user_artist, user_album)
    print(user_formatted_album)

    end = input("Quit? (y, n): ")
    if end == "y":
        break
    else:
        print("")