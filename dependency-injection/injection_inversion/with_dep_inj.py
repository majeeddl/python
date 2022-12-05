
import string
import random


class Order:

    def __init__(self) -> None:
        self.id = ''.join(random.choices(string.ascii_lowercase, k=6))
        self.status = 'open'

    def set_status(self, status):
        self.status = status


class Authorizer_SMS:

    def __init__(self) -> None:
        self.authorized = False
        self.code = None

    def generate_sms_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))

    def authorize(self):
        code = input("Enter SMS code: ")
        self.authorized = code == self.code

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor:

    def __init__(self,authorizor:Authorizer_SMS) -> None:
        self.authorizor = authorizor

    def pay(self, order):
        
        self.authorizor.authorize()

        if not self.authorizor.is_authorized():
            raise Exception("Not Authorized")

        print(f"Processing payment for order with id {order.id}")

        order.set_status("paid")
