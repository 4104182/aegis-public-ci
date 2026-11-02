"""Open, fabricated Aegis-style safety contract. NOT wallet code or crypto QA."""
import unittest

def allowed_operation(network_isolated, owner_authorized, fresh_qa_fixture):
    return all((network_isolated, owner_authorized, fresh_qa_fixture))

def valid_public_commit(value):
    return len(value) == 40 and all(c in "0123456789abcdef" for c in value)

class SyntheticWalletSafetyContract(unittest.TestCase):
    def test_denies_when_owner_missing(self):
        self.assertFalse(allowed_operation(True, False, True))
    def test_denies_when_network_not_isolated(self):
        self.assertFalse(allowed_operation(False, True, True))
    def test_denies_without_fixture(self):
        self.assertFalse(allowed_operation(True, True, False))
    def test_fake_positive_logic_only(self):
        self.assertTrue(allowed_operation(True, True, True))
    def test_commit_identity(self):
        self.assertTrue(valid_public_commit("a"*40))
        self.assertFalse(valid_public_commit("main"))

if __name__ == "__main__":
    unittest.main()
