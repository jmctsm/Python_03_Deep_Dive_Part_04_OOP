import itertools


class Account:
    transaction_counter = itertools.count(100)

    def make_transaction(self):
        new_trans_id = next(Account.transaction_counter)
        return new_trans_id
