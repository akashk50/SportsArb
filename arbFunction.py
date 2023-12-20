class ArbitrageOpportunity:
    def __init__(self, teams, betting, return_percent):
        self.teams = teams
        self.betting = betting
        self.return_percent = return_percent-1

    def display_opportunity(self):
        print(f"Arbitrage Opportunity for: {self.teams[0]} vs {self.teams[1]}")
        for key, details in self.betting.items():
            print(f"  {key}:")
            print(f"    Site to Bet On: {details['site']}")
            print(f"    Odds: {details['odds']}")
            print(f"    % of Income to Bet: {round(details['bet_percent'] * 100,3)}%")
        print(f"  Expected Return: {round(100*self.return_percent,3)}%")
        print("")