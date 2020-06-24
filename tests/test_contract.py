#tests/test_contract.py
import unittest

from contracting.client import ContractingClient
client = ContractingClient()

with open('../my_token.py') as f:
    code = f.read()
    client.submit(code, name='my_token')

class MyTestCase(unittest.TestCase):
    def test_supply(self):
        # Get contract reference
        my_token = client.get_contract('my_token')
        # Assert token balance for 'me'
        self.assertEqual(my_token.quick_read('S', 'me'), 50)

    def test_transfer(self):
        # set transaction sender
        client.signer = 'me'
        # Get contract reference
        my_token = client.get_contract('my_token')
        # Call transfer method
        my_token.transfer(
            amount=10,
            receiver='you'
        )
        # Assert token balance for 'me'
        self.assertEqual(my_token.quick_read('S', 'me'), 40)
        # Assert token balance for 'you'
        self.assertEqual(my_token.quick_read('S', 'you'), 10)

    def test_transfer_neg_insufficient_funds(self):
        # set transaction sender
        client.signer = 'you'
        # Get contract reference
        my_token = client.get_contract('my_token')

        me_balance_before = my_token.quick_read('S', 'me')
        you_balance_before = my_token.quick_read('S', 'you')

        # Set transfer ammount to X + 1
        transfer_amount = you_balance_before + 1

        # Test that the transfer method raises an Assertion
        self.assertRaises(
            AssertionError,
            lambda: my_token.transfer(
                amount=transfer_amount,
                receiver='me'
            )
        )

        # Assert token balance for 'me' has not changed
        self.assertEqual(my_token.quick_read('S', 'me'), me_balance_before)
        # Assert token balance for 'you' has not changed
        self.assertEqual(my_token.quick_read('S', 'you'), you_balance_before)

if __name__ == '__main__':
    unittest.main()