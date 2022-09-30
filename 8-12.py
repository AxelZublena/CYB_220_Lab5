# 8.12
def get_sandwich(*items):
    print("\nYou ordered the following sandwich: ")
    for item in items:
        print(f" - {item}")

get_sandwich("tomato")
get_sandwich("lettuce", "tomato", "ham")
get_sandwich("lettuce", "egg", "chicken", "cheese")
