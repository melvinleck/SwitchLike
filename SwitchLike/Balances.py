class balance:
    def __init__(self, bank_name, account_number, type,date,amount):
        self.__bank_name = bank_name
        self.__account_number = account_number
        self.__type = type
        self.__date=date
        self.__amount=amount

    def get_bank_name(self):
        return self.__bank_name
    def get_account_number(self):
        return self.__account_number
    def get_type(self):
        return self.__type
    def get_date(self):
        return self.__date
    def get_amount(self):
        return self.__amount

    def set_bank_name(self, bank_name):
        self.__bank_name = bank_name
    def set_account_number(self,account_number):
        self.__account_number = account_number
    def set_type(self, type):
        self.__type = type
    def set_date(self,date):
        self.__date=date
    def set_amount(self,amount):
        self.__amount=amount
