# Solution to Task 3 (Function):

def foodpanda(burger, location='Mohakhali'):
    menu = {"BBQ Chicken Cheese Burger ": 250, "Beef Burger": 170, "Naga Drums": 200}
    total = 40 if location == 'Mohakhali' else 60
    total += menu[burger] + (menu[burger]*0.08)
    print(total)


if __name__ == "__main__":
    user = input().strip("() ").replace("'", "")
    if "," in user:
        burger, location = [i.strip() for i in user.split(",")]
        foodpanda(burger, location)
    else:
        foodpanda(user)