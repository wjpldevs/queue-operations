from dataclasses import dataclass

@dataclass
class Customer:

    _customer_name: str
    _customer_email: str
    _customer_account: float

    # constructor
    def __init__(self, customer_name="", customer_email="", customer_account=0.0) -> None:
        self._customer_name = customer_name
        self._customer_email = customer_email
        self._customer_account = customer_account
    
    # properties
    # getter
    @property
    def customer_name(self):
        return self._customer_name

    # setter
    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    # getter
    @property
    def customer_email(self) -> str:
        return self._customer_email

    # setter
    @customer_email.setter
    def customer_email(self, value):
        self._customer_email = value

    # getter
    @property
    def customer_account(self) -> float:
        return self._customer_account
    
    # setter
    @customer_account.setter
    def customer_account(self, value):
        self._customer_account = value
    