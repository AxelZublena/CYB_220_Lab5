# 8.6
def city_country(city, country):
    string = f"{city}, {country}"
    return string.title() 

paris = city_country("paris", "france")
simpsonville = city_country("toronto", "canada")
tokyo = city_country("tokyo", "japan")

print(paris)
print(simpsonville)
print(tokyo)
