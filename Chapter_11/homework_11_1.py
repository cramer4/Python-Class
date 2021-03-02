def get_city(city, country):
    formatted = f"{city}, {country}"
    return formatted.title()

print(get_city("paris", "france"))