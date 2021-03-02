def get_city(city, country, population=""):
    if population:
        formatted = f"{city}, {country}\nPopulation: {population}"
    else:
        formatted = f"{city}, {country}"
    return formatted.title()

print(get_city("paris", "france", "2100000"))
