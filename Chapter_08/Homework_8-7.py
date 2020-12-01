def make_album(artist, album, songs= ""):

    album_dictionary = {"artist": f"{artist.title()}",
    "album": f"{album.title()}"}

    if songs:
        album_dictionary["songs"] = f"{songs}"

    else:
        formatted_album = f"{album.title()} is by {artist.title()}."
    return album_dictionary



collide = make_album("skillet", "collide", 10)
phenomenon = make_album("thousand foot krutch", "phenomenon")
fireproof = make_album("pillar", "fireproof")

albums = [collide, phenomenon, fireproof]
for album in albums:
    print(album)