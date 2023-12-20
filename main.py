import json
import arbFunction

# Load JSON data
with open('odds_data.json', 'r') as file:
    data = json.load(file)

arb_opportunities = {}

for game in data['data']:
    teams = tuple(game['teams'])
    best_odds = {'Team1': 0, 'Team2': 0, 'Draw': 0}
    best_sites = {'Team1': '', 'Team2': '', 'Draw': ''}
    if game['sites']:
        for site in game['sites']:
            odds = site['odds']['h2h']
            if odds[0] > best_odds['Team1']:
                best_odds['Team1'] = odds[0]
                best_sites['Team1'] = site['site_key']
            if odds[1] > best_odds['Team2']:
                best_odds['Team2'] = odds[1]
                best_sites['Team2'] = site['site_key']
            if len(odds) == 3 and odds[2] > best_odds['Draw']:
                best_odds['Draw'] = odds[2]
                best_sites['Draw'] = site['site_key']
    
        # Calculate arbitrage
        if len(best_sites['Draw']) > 0:
            percent = 1 / (1/best_odds['Team1'] + 1/best_odds['Team2'] + 1/best_odds['Draw'])
        else:
            percent = 1 / (1/best_odds['Team1'] + 1/best_odds['Team2'])
    
        if percent > 1:
            opp = {
                teams[0]: {'site': best_sites['Team1'], 'odds': best_odds['Team1'], 'bet_percent': percent * (1 / best_odds['Team1'])},
                teams[1]: {'site': best_sites['Team2'], 'odds': best_odds['Team2'], 'bet_percent': percent * (1 / best_odds['Team2'])},
            }
            if len(best_sites['Draw']) > 0:
                opp['Draw'] = {'site': best_sites['Draw'], 'odds': best_odds['Draw'], 'bet_percent': percent * (1 / best_odds['Draw'])}
        
            arb_opportunities[teams] = arbFunction.ArbitrageOpportunity(teams, opp, percent)
for i in arb_opportunities:
    arb_opportunities[i].display_opportunity() 