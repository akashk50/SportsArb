import requests
import json

api_key = '42ecb96491ef131b24963fc08458e829'
sport_key = 'upcoming'

# Make the API request
odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
    'api_key': api_key,
    'sport': sport_key,
    'region': 'uk', # uk | us | eu | au
    'mkt': 'h2h' # h2h | spreads | totals
})

# Parse the JSON response
odds_json = json.loads(odds_response.text)
if not odds_json['success']:
    print('There was a problem with the odds request:', odds_json['msg'])
else:
    # Print information about the events
    print('Successfully got {} events'.format(len(odds_json['data'])), 'Here\'s the first event:')
    print(odds_json['data'][0])

    # Check your API usage
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])

    # Save the JSON data to a file
    with open('odds_data.json', 'w') as file:
        json.dump(odds_json, file, indent=4)
        print('The odds data has been saved to "odds_data.json".')

# Note: You can change 'odds_data.json' to any desired file name or path