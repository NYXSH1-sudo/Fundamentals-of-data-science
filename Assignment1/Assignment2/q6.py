def find_country_index(countries, target_country):
    """
    Returns the index of the target_country in the countries list.
    If not found, returns "Not Found in List".
    """
    if target_country in countries:
        return countries.index(target_country)
    else:
        return "Not Found in List"


#Examplelist
countries_list = ["Nepal", "India", "China", "USA", "Japan"]

print(find_country_index(countries_list, "USA"))   
print(find_country_index(countries_list, "Brazil"))  