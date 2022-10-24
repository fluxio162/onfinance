from onfinance.onfinance import OnFinance
import unittest

isin = "LU1781541179"
onfinance = OnFinance(isin)


class TestOnFinance(unittest.TestCase):
    def test_invalid_isin(self):
        test_isin = "L41179"
        with self.assertRaises(TypeError):
            test = OnFinance(test_isin)

    def test_price(self):
        assert isinstance(onfinance.get_current_price(), float)

    def test_name(self):
        assert isinstance(onfinance.get_name(), str)
        self.assertEqual(onfinance.get_name(), "Lyxor Core MSCI World(DR)UE A.")

    def test_markets(self):
        self.assertIsNotNone(onfinance.get_markets())

    def test_info(self):
        self.assertIsNotNone(onfinance.get_info())

    def test_market(self):
        self.assertIsNotNone(onfinance.get_market("Xetra"))

    def test_available_markets(self):
        self.assertIsNotNone(onfinance.get_available_markets())

    def test_performance(self):
        self.assertIsNotNone(onfinance.get_performance())

    def test_holdings(self):
        self.assertIsNotNone(onfinance.get_holdings())

    def test_branches(self):
        self.assertIsNotNone(onfinance.get_branches())


if __name__ == '__main__':
    unittest.main()
