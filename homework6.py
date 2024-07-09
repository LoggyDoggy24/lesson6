my_dict = {"Я": 1992, "Он": 1991, "Она": 1990, "Они": 1996, "Оно": 1989}
print(my_dict)
print(my_dict["Я"])
print(my_dict.get("Ты"))
my_dict.update({"Ты": 1989, "Мы": 2016})
exception = my_dict.pop("Я")
print(exception)
print(my_dict)
my_set = {666, 666, "Beast", "Beast", 666.666}
print(my_set)
my_set.add((6, 6, 6) * 2)
my_set.add(6.66)
my_set.discard("Beast")
modified_set = print(my_set)