from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from collections import OrderedDict
import sys
import csv

matches_csv = "/home/dell/PycharmProjects/data_project1/data/matches.csv"
delivery_csv = "/home/dell/PycharmProjects/data_project1/data/deliveries.csv"

# Plot the number of matches played per year of all the years in IPL.


def num_of_match_each_year(match_url):
    match_handle = open(match_url, 'r')
    data_dict = {}
    for match in csv.DictReader(match_handle):
        if match['season'] not in data_dict:
            data_dict[match['season']] = 0
        data_dict[match['season']] += 1
    match_handle.close()
    data_dict = OrderedDict(sorted(data_dict.items()))
    # print(data_dict)
    return list(data_dict.keys()), list(data_dict.values())

# Plot a stacked bar chart of matches won of all teams over all the years of IPL.


def stacked_bar_chart(match_url):
    match_handle = open(match_url, 'r')
    data_dict, lst_of_winning_team = {}, []
    for match in csv.DictReader(match_handle):
        if match['season'] not in data_dict:
            data_dict[match['season']] = {}
        if match['winner'] != "":
            if match['winner'] not in data_dict[match['season']]:
                data_dict[match['season']][match['winner']] = 0
                if match['winner'] not in lst_of_winning_team:
                    lst_of_winning_team.append(match['winner'])
            data_dict[match['season']][match['winner']] += 1
    match_handle.close()
    data_dict = OrderedDict(sorted(data_dict.items()))
    # print(data_dict)
    # print(lst_of_winning_team)
    return [data_dict, lst_of_winning_team]


def matches_won_by_team(data_dict, lst_of_winning_team):    # Returns the matches won per team in year 2008 to 2017
    matches_per_team = {}

    for team in lst_of_winning_team:
        matches_per_team[team] = []

    for season in data_dict:
        for team in data_dict[season]:
            matches_per_team[team].append(data_dict[season][team])

        for team in lst_of_winning_team:        # Inserting zero for the team which is not won in a season
            if team not in data_dict[season]:
                matches_per_team[team].append(0)
    return matches_per_team


def get_index_list(cur_team, lst_every_team_data):        # Returns the location list of the bar plot for each team
    prev_list_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if lst_every_team_data.index(cur_team) == 0:
        return prev_list_sum
    else:
        for data in range(lst_every_team_data.index(cur_team)):
            prev_list_sum = [x + y for x, y in zip(prev_list_sum, lst_every_team_data[data])]
        # print(prev_list_sum)
        return prev_list_sum


def plot_stacked_bar_graph(lst_of_seasons, matches_per_team):
    patch_list, i = [], 0
    color_lst = ['c', 'hotpink', 'darkslateblue', 'forestgreen', 'midnightblue', 'steelblue', 'dodgerblue',
                 'lightslategrey', 'lightseagreen', 'darkgoldenrod', 'rebeccapurple', 'darkorange', 'sienna']

    for team in matches_per_team:
        plt.bar(lst_of_seasons, matches_per_team[team], color=color_lst[i],
                bottom=get_index_list(matches_per_team[team], list(matches_per_team.values())))
        patch_list.append(mpatches.Patch(color=color_lst[i], label=team))
        i += 1

    plt.grid(axis='y')
    plt.title('Stacked Bar Chart')
    plt.xlabel('Seasons')
    plt.ylabel('No. of matches won')
    plt.legend(handles=patch_list, loc='upper right')
    plt.show()

# For the year 2016 plot the extra runs conceded per team.


def match_2016_extra_run(match_url, delivery_url):
    match_handle = open(match_url, 'r')
    delivery_handle = open(delivery_url, 'r')
    lst_of_match_id, extra_run_per_team = [], {}

    for match in csv.DictReader(match_handle):
        if match['season'] == '2016':
            lst_of_match_id.append(match['id'])
    for delivery in csv.DictReader(delivery_handle):
        if delivery['match_id'] in lst_of_match_id:
            if delivery['bowling_team'] not in extra_run_per_team:
                extra_run_per_team[delivery['bowling_team']] = 0
            extra_run_per_team[delivery['bowling_team']] += int(delivery['extra_runs'])
    match_handle.close()
    delivery_handle.close()
    return extra_run_per_team

# For the year 2015 plot the top economical bowlers.


def match_2015_eco_bowler(match_url, delivery_url):
    match_handle = open(match_url, 'r')
    delivery_handle = open(delivery_url, 'r')
    lst_match_id, economical_bowler, final_economical_bowler, lst_of_bowlers = [], {}, {}, []
    for match in csv.DictReader(match_handle):      # Reading match_id for bowlers
        if match['season'] == '2015':
            lst_match_id.append(match['id'])
    match_handle.close()
    # Creating "bowler_dict = {'bowler': {'no_of_balls': val, 'tot_runs_given': val}}" in this format
    for delivery in csv.DictReader(delivery_handle):
        if delivery['match_id'] in lst_match_id:
            if delivery['bowler'] not in economical_bowler:
                economical_bowler[delivery['bowler']] = {}
                economical_bowler[delivery['bowler']]['no_of_balls'] = 0
                economical_bowler[delivery['bowler']]['total_runs_given'] = 0
            economical_bowler[delivery['bowler']]['no_of_balls'] += 1
            economical_bowler[delivery['bowler']]['total_runs_given'] += int(delivery['total_runs'])
    delivery_handle.close()
    for bowler in economical_bowler:
        economical_bowler[bowler] = round(economical_bowler[bowler]['total_runs_given'] * 6 /
                                          economical_bowler[bowler]['no_of_balls'], 1)      # Calculating economic rate
        # Creating a dictionary {economic_rate: list of bowlers}
        if economical_bowler[bowler] not in final_economical_bowler:
            final_economical_bowler[economical_bowler[bowler]] = []
            final_economical_bowler[economical_bowler[bowler]].append(bowler)
    final_economical_bowler = OrderedDict(sorted(final_economical_bowler.items()))
    for bowler_lst in final_economical_bowler.values():
        lst_of_bowlers += bowler_lst
    final_economical_bowler = OrderedDict()     # Initializing the variable with empty ordered dictionary
    for bowler in lst_of_bowlers[:10]:      # Storing the final data to the variable
        final_economical_bowler[bowler] = economical_bowler[bowler]
    return final_economical_bowler

# Match summary for players winning man of the match maximum number of times in a given year


def match_summary_over_years(match_url, season):
    match_handle = open(match_url)
    data_dict, rev_data_dict = {}, {}
    lst_of_top_players = []

    for match in csv.DictReader(match_handle):  # Counting frequency of player_of_match for each player in a season
        if match['season'] == season:
            if match['player_of_match'] not in data_dict:
                data_dict[match['player_of_match']] = 0
            data_dict[match['player_of_match']] += 1
    # print(data_dict)
    for player in data_dict:       # Creating a reverse dictionary with values of data_dict as key
        if data_dict[player] not in rev_data_dict:
            rev_data_dict[data_dict[player]] = []
        rev_data_dict[data_dict[player]].append(player)

    rev_data_dict = OrderedDict(sorted(rev_data_dict.items(), reverse=True))
    # print(rev_data_dict)
    for val_man_of_match in rev_data_dict:      # Storing top players in a list
        lst_of_top_players += rev_data_dict[val_man_of_match]
    rev_data_dict = OrderedDict()       # Initializing with empty dictionary for reusing the variable
    for player in lst_of_top_players[:10]:      # Storing the first 10 player data
        rev_data_dict[player] = data_dict[player]
    # print(rev_data_dict)
    return rev_data_dict


def choose_option():
    while True:
        print('Press 1 to Plot the number of matches played per year of all the years in IPL.')
        print('Press 2 to Plot a stacked bar chart of matches won of all teams over all the years of IPL.')
        print('Press 3 For the year 2016 plot the extra runs conceded per team.')
        print('Press 4 For the year 2015 plot the top economical bowlers.')
        print('Press 5 to obtain the player who was awarded as man of the match maximum number of times')
        print('Press 6 to Exit')
        selection_var = eval(input('Enter an integer for the choice given above\n'))
        if isinstance(selection_var, int) and selection_var in [1, 2, 3, 4, 5, 6]:
            if selection_var == 1:
                lst_of_season, num_of_matches_played = num_of_match_each_year(matches_csv)
                plt.bar(lst_of_season, num_of_matches_played, color=['c', 'hotpink', 'darkslateblue', 'forestgreen',
                                                                     'sienna', 'midnightblue', 'steelblue',
                                                                     'lightslategrey', 'cadetblue', 'lightseagreen'])
                plt.xlabel('Seasons')
                plt.ylabel('Number of matches played')
                plt.title('Number of matches played each year')
                plt.grid(axis='y')
                plt.show()
            elif selection_var == 2:
                data_dict, lst_of_winning_team = stacked_bar_chart(matches_csv)
                lst_every_team_data = matches_won_by_team(data_dict, sorted(lst_of_winning_team))
                plot_stacked_bar_graph(data_dict.keys(), lst_every_team_data)
            elif selection_var == 3:
                extra_run_per_team = match_2016_extra_run(matches_csv, delivery_csv)
                plt.bar(list(extra_run_per_team.keys()), list(extra_run_per_team.values()),
                        color=['c', 'hotpink', 'darkslateblue', 'forestgreen', 'midnightblue', 'steelblue',
                               'lightslategrey', 'lightseagreen'])
                plt.xlabel('Team Name')
                plt.ylabel('Total Extra runs given in 2016')
                plt.title('Extra runs conceded per team')
                plt.grid(axis='y')
                plt.show()
            elif selection_var == 4:
                bowler_eco_rate = match_2015_eco_bowler(matches_csv, delivery_csv)
                plt.bar(bowler_eco_rate.keys(), bowler_eco_rate.values(),
                        color=['c', 'hotpink', 'darkslateblue', 'forestgreen', 'sienna',
                               'midnightblue', 'steelblue', 'lightslategrey', 'cadetblue',
                               'lightseagreen'])
                plt.xlabel('Bowler Name')
                plt.ylabel('Average runs given per over')
                plt.title('Bowler Economic Rate for 2015')
                plt.grid(axis='y')
                plt.show()
            elif selection_var == 5:
                season = eval(input('Enter the year for which you want to track man of the match\n'))
                player_of_match = match_summary_over_years(matches_csv, str(season))
                plt.bar(player_of_match.keys(), player_of_match.values())
                plt.xlabel('Player Name')
                plt.ylabel('Max. number of man of the match')
                plt.title('Player awarded as man of the match maximum number of times in the year {}'.format(season))
                plt.grid(axis='y')
                plt.show()
            elif selection_var == 6:
                sys.exit()
        else:
            print('Invalid input please try again later!!!')


if __name__ == '__main__':
    choose_option()
