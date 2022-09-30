# 8.12 rewrite for 8.17
def get_sandwich(*items):
    """
    Print the sendwich ordered by the user.
    Each item in the sendwich is printed on a new line.
    """
    print("\nYou ordered the following sandwich: ")
    for item in items:
        print(f" - {item}")

get_sandwich("tomato")
get_sandwich("lettuce", "tomato", "ham")
get_sandwich("lettuce", "egg", "chicken", "cheese")
