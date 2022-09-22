import mysql.connector

print(
    """============================================================================================================

                                   Welcome to Star Management Console

============================================================================================================
Menu:
[1] Add stars       [2] Register a new transaction    [3] View transactions    [4] Summary"""
)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="mysql"
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


def add_stars_to_account(account_id, add_count):
    cursor = mydb.cursor()
    update_table = f"update stars.account set stars = stars + {add_count} where account_id = '{account_id}'"
    no_of_records_updated = cursor.execute(update_table)
    mydb.commit()
    if no_of_records_updated == 1:
        return True
    else:
        return False


def add_stars():
    print('Tha add stars functionality will be added in this function')


def register_a_new_transaction():
    print('The transaction registration functionality will be added in this function')


def view_transaction():
    print('The View transactions functionality will be added in this function')


def summary():
    print('The Summary view will be added in this function')


menu()
