from datetime import datetime, timedelta

print "This program is perfect for restaurants, that do not operate on fixed menu,\nbut rather with different complete menues per meal.\nYou can plan your 7 day, 3 course (or less) menu.\n"

weeklyMenu_lists = {}

#writes dates of menu validity
menu_file = open("menu.txt", "w+")
menu_file.write ("Daily menu\n\n")
weekStart = raw_input("Menu is valid from (dd.mm.llll): ")
weekEnd = raw_input("Menu is valid to (dd.mm.llll): ")
menu_file.write ("From " + weekStart + " to " + weekEnd +"\n\n")

#dates will provide number of iterations
weekStart = datetime.strptime(weekStart, "%d.%m.%Y")
weekEnd = datetime.strptime(weekEnd, "%d.%m.%Y")
number_of_days = (weekEnd - weekStart).days + 1

#reades input to list
for day_number in range(number_of_days):
    another_meal = "y"
    current_date = (weekStart + timedelta(days=day_number)).date()
    day = datetime.strftime(current_date, "%A")
    date = datetime.strftime(current_date, "%d.%m.%Y")
    print "\nVnos za: " + day + ", " + date + "\n"

    weeklyMenu_lists[date] = {}
    weeklyMenu_lists[date]['dishes'] = {}

    while another_meal.lower() == "y":
        meal_name = raw_input("Name of the meal: ")
        price = raw_input("Price of the meal: ")
        soup = raw_input("Soup: ")
        main_dish = raw_input("Main Dish: ")
        third_course = raw_input("Salad, fruit or something sweet:")
        another_meal = raw_input("Do you want to add another meal to this day?    Y / N  :")

        weeklyMenu_lists[date]['day'] = day
        weeklyMenu_lists[date]['dishes'][meal_name] = {}
        weeklyMenu_lists[date]['dishes'][meal_name]['price'] = price
        weeklyMenu_lists[date]['dishes'][meal_name]['soup'] = soup
        weeklyMenu_lists[date]['dishes'][meal_name]['main_dish'] = main_dish
        weeklyMenu_lists[date]['dishes'][meal_name]['third_course'] = third_course

#writes list to file
for (date, weeklyMenu_list) in sorted(weeklyMenu_lists.items()):
    menu_file.write(weeklyMenu_list['day'] + ", " + date + "\n\n")

    for (meal_name, dishes) in weeklyMenu_list['dishes'].items():
        menu_file.write(meal_name + "\n" + "Cena: " + dishes['price'] + " EUR\n"
                        + dishes['soup'] + "\n"
                        + dishes['main_dish'] + "\n"
                        + dishes['third_course'] + "\n\n")

menu_file.close()
