class Account:
    account_id = None
    first_name = None
    last_name = None
    stars = None

    def __init__(self, account_id, first_name, last_name, stars):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.stars = stars

    def __str__(self):
        return f'account_id = {self.account_id}, first_name = {self.first_name}, last_name = {self.last_name}, stars = {self.stars} '
