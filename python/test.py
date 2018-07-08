prefix = 'Py'
prefix = prefix + 'thon'

print(prefix)
print(prefix[3])

print("Hello!!")

username = "Yogesh"
timestamp = "16:20"
url = "http://petshop.com/pets/reptiles/pythons"

print(username + " accessed the site " + url + " at " + timestamp + ".")

given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"

name = given_name + " " + middle_names + " " + family_name

name_length = len(name)  # todo: calculate how long this name is

driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)