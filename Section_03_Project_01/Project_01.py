import TimeZone
import Account
# import Transaction_Numbers


if __name__ == "__main__":
    print(Account.Account.get_interest_rate())
    Account.Account.set_interest_rate(10)
    print(Account.Account.get_interest_rate())
    try:
        Account.Account.set_interest_rate(1+1j)
    except ValueError as ex:
        print(ex)