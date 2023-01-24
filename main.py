import json

# creates a table showing the win/losses for each team in the JSON file against every other team
def generate_H2H_WL_table(filepath):
    # adjacency matrix (dictionary of dictionaries)
    adj_matrix = {} 
    raw_text = ""

    # import raw text data
    with open(filepath) as file:
        raw_text = file.read()

    # convert text to dictionary object
    file_data = json.loads(raw_text)

    # iterate through dictionary, building 
    for w_team, team_record in file_data.items():
        adj_matrix[w_team] = {}
        adj_matrix[w_team][w_team] = '--' # set team's self-record to '--'
        for l_team, record in team_record.items():
            wins = record["W"]
            adj_matrix[w_team][l_team] = str(wins)

    return adj_matrix

if __name__ == "__main__":
    table = generate_H2H_WL_table('./test_data.json')