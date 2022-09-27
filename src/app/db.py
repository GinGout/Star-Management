import mysql.connector

from src.app.Account import Account

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="mysql"
)


def add_stars_to_account(account_id, add_count):
    cursor = mydb.cursor()
    update_table = f"update stars.account set stars = stars + {add_count} where account_id = '{account_id}'"
    no_of_records_updated = cursor.execute(update_table)
    mydb.commit()
    if no_of_records_updated == 1:
        return True
    else:
        return False


def retrieve_accounts():
    cursor = mydb.cursor()
    cursor.execute("select * from stars.account")
    list_of_raw_account_records = cursor.fetchall()
    list_of_accounts = []
    for row in list_of_raw_account_records:
        list_of_accounts.append(Account(row[0], row[1], row[2], row[3]))

    return list_of_accounts


# accounts = retrieve_accounts()
#
# for account in accounts:
#     print(account)


def most_stars():
    accounts = retrieve_accounts()
    print(max(account.stars for account in accounts))


most_stars()
