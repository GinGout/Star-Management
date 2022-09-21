print(
    """============================================================================================================

                                   Welcome to Star Management Console

============================================================================================================
Menu:
[1] Add stars       [2] Register a new transaction    [3] View transactions    [4] Summary"""
)


def menu():
    user_input = int(input('Enter your choice: '))
    if user_input == 1:
        add_stars()

    elif user_input == 2:
        register_a_new_transaction()

    elif user_input == 3:
        view_transaction()

    elif user_input == 4:
        summary()

    else:
        print('Please enter the correct number')

    menu()


def add_stars():
    print('The add stars functionality will be added in this function')


def register_a_new_transaction():
    print('The transaction registration functionality will be added in this function')


def view_transaction():
    print('The View transactions functionality will be added in this function')


def summary():
    print('The Summary view will be added in this function')


menu()
