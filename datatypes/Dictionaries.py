# Dictionaries are unordered mappings for storing objects. Just like maps in java
my_dict = { "key1" : "value1",
            "key2" : "value2"
            }
print(my_dict)
print(my_dict["key1"])

# Dictionary can hold data of various objects in one declaration only
var_dict = {"k1": "Divya",
            "k2": ['a', 'b', 'c', 'd'],
            "k3": {"k4": "Thakur"}
            }
print(var_dict)
print(var_dict["k3"]["k4"])
print(var_dict["k2"][0].upper())
var_dict["k1"] = "Mridul"
print(var_dict)

# Getting all the keys and values from dictionary
print(var_dict.keys())
print(var_dict.values())
print(var_dict.items())
