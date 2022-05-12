import sys
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment

class PayPalClient:
    def __init__(self):
        self.client_id = "Ae2jUbEPs4QThi6aM0SMTcZyMnqCNqHZFE2L6qu3_35bd2v_-j5t5GQp8s9Hml5sYeeyDCZXqYi4Mf4u"
        self.client_secret = "EPFh8NI_31FVi6Rb5WiESwOr0Q-A1lV6LHkxHL8awD3mP3T0Z6vui5riXjewbgfZFe2znrgyyKDa0l9D"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
