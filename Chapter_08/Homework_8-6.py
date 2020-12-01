def city_country(city, country):
    formatted_pair = f"{city}, {country}"
    return formatted_pair.title()

paris = city_country(city= "parris", country= "france")
mexico_city = city_country(city= "mexico city", country= "mexcio")
berlin = city_country(city= "berlin", country= "germany")

cities = [paris, mexico_city, berlin]
for city in cities:
    print(city)