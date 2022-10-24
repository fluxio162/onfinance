import requests


# https://api.onvista.de/api/v1/stocks/ISIN:US0378331005/snapshot

class OnFinance:
    def __init__(self, isin):
        print(requests.__version__)

        if not self.__isin_correct(isin):
            raise TypeError(isin + " ISIN is not valid")

        url = "https://api.onvista.de/api/v1/funds/ISIN:{}/snapshot".format(isin)
        response = requests.request("GET", url=url)

        self.__responseJson = response.json()

    def get_info(self):
        return self.__responseJson.get("fundsDetails")

    def get_current_price(self):
        return round(self.__responseJson.get("quote").get("last"), 2)

    def get_name(self):
        return self.__responseJson.get("instrument").get("name")

    def get_markets(self):
        return [market for market in self.__responseJson.get("quoteList").get("list")]

    def get_market(self, market):
        for m in self.__responseJson.get("quoteList").get("list"):
            if m.get("market").get("name") == market:
                return m
        raise KeyError(market + " not found!")

    def get_available_markets(self):
        markets = set()
        for m in self.__responseJson.get("quoteList").get("list"):
            markets.add(m.get("market").get("name"))
        return markets

    def get_performance(self):
        return self.__responseJson.get("cnPerformance")

    def get_holdings(self):
        holdings = self.__responseJson.get("fundsHoldingList")
        return holdings

    def get_branches(self):
        return self.__responseJson.get("branchFundsBreakdownList")

    def __isin_correct(self, isin):

        if len(isin).__eq__(12):
            country_code = isin[:2]
            identifier = isin[2:]

            if country_code.isalpha() and identifier.isnumeric():
                return True

        return False
