paris_info = {
    "country": "France",
    "population": 12278210,
    "fact": "France is called the city of love."
}

nyc_info = {
    "country": "The USA",
    "population": 18804000,
    "fact": "Times Square is named after the New York Times news paper."
}

tokyo_info = {
    "country": "Japan",
    "population": 37393000,
    "fact": "Tokyo is the largest metropolitan area in the world."
}

cities = {
    "paris": paris_info,
    "nyc": nyc_info,
    "tokyo": tokyo_info
}


for city in cities:
    if city == "nyc":
        print(f"\n{city.upper()}:")
    else:
        print(f"\n{city.title()}:")
    if city == "paris":
        for key, info in paris_info.items():
            print(f"{key.title()}: {info}")
    if city == "nyc":
        for key, info in nyc_info.items():
            print(f"{key.title()}: {info}")
    if city == "tokyo":
        for key, info in tokyo_info.items():
            print(f"{key.title()}: {info}")