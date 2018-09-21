from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from collections import OrderedDict
import sys
from src import read_csv_create_table as db

# matches_csv = "/home/dell/PycharmProjects/data_project1/data/matches.csv"
# delivery_csv = "/home/dell/PycharmProjects/data_project1/data/deliveries.csv"


def establish_connection(database):
    conn = db.connect_db(database, 'root', 'admin@123', 'localhost')
    return conn

# Plot the number of matches played per year of all the years in IPL.


def num_of_match_each_year(db_name, match_table_name):
    conn_obj = establish_connection(db_name)
    cursor = conn_obj.cursor()
    cursor.execute('SELECT season, COUNT(season) FROM {} group by season;'.format(match_table_name))
    data_dict = dict(cursor)
    conn_obj.close()
    for season in sorted(data_dict.keys()):
        data_dict[season] = int(data_dict[season])
    # print(data_dict)
    return list(data_dict.keys()), list(data_dict.values())

# Plot a stacked bar chart of matches won of all teams over all the years of IPL.


def stacked_bar_chart(db_name, match_table_name):
    data_dict, lst_of_winning_team = {}, []
    conn_obj = establish_connection(db_name)
    cursor = conn_obj.cursor()
    cursor.execute('SELECT season, winner, COUNT(winner) FROM {} GROUP BY winner, season;'.format(match_table_name))
    for match in cursor:
        season, winner, win_frequency = 0, 1, 2
        if match[season] not in data_dict:
            data_dict[match[season]] = {}
        if match[winner] != "":
            if match[winner] not in data_dict[match[season]]:
                data_dict[match[season]][match[winner]] = 0
                if match[winner] not in lst_of_winning_team:
                    lst_of_winning_team.append(match[winner])
            data_dict[match[season]][match[winner]] += int(match[win_frequency])
    conn_obj.close()
    data_dict = OrderedDict(sorted(data_dict.items()))
    # print(data_dict)
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


def match_2016_extra_run(db_name, match_table_name, delivery_table_name):
    conn_obj = establish_connection(db_name)
    cursor = conn_obj.cursor()
    cursor.execute("SELECT bowling_team, SUM(extra_runs) FROM {0} INNER JOIN {1} ON {0}.id = {1}.match_id WHERE {0}.season = '2016' group by {1}.bowling_team;".format(match_table_name, delivery_table_name))
    extra_run_per_team = dict(cursor)
    conn_obj.close()
    for bowling_team in sorted(extra_run_per_team.keys()):
        extra_run_per_team[bowling_team] = int(extra_run_per_team[bowling_team])
    # print(extra_run_per_team)
    return extra_run_per_team

# For the year 2015 plot the top economical bowlers.


def match_2015_eco_bowler(db_name, match_table_name, delivery_table_name):
    economical_bowler, bowler, total_runs, num_of_balls = {}, 0, 1, 2
    conn_obj = establish_connection(db_name)
    cursor = conn_obj.cursor()
    cursor.execute("SELECT bowler, SUM(total_runs), COUNT(over) FROM {0} INNER JOIN {1} ON {0}.id = {1}.match_id WHERE {0}.season = '2015' GROUP BY {1}.bowler;".format(match_table_name, delivery_table_name))
    for data in cursor:
        economical_bowler[data[bowler]] = round(float(data[total_runs]) * 6 / float(data[num_of_balls]), 1)
    conn_obj.close()
    economical_bowler = OrderedDict(sorted(economical_bowler.items(), key=lambda x: x[1])[:10])
    # print(economical_bowler)
    return economical_bowler

# Match summary for players winning man of the match maximum number of times in a given year


def match_summary_over_years(db_name, match_table_name, season):
    data_dict, player, winning_frequency = {}, 0, 1
    conn_obj = establish_connection(db_name)
    cursor = conn_obj.cursor()
    cursor.execute("SELECT player_of_match, COUNT(player_of_match) AS frequency FROM {0} WHERE season = {1} GROUP BY player_of_match ORDER BY frequency DESC;".format(match_table_name, season))
    for player_data in cursor:
        data_dict[player_data[player]] = int(player_data[winning_frequency])
    conn_obj.close()
    data_dict = OrderedDict(sorted(data_dict.items())[:10])
    # print(data_dict)
    return data_dict


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
                lst_of_season, num_of_matches_played = num_of_match_each_year('live_db', 'matches')
                plt.bar(lst_of_season, num_of_matches_played, color=['c', 'hotpink', 'darkslateblue', 'forestgreen',
                                                                     'sienna', 'midnightblue', 'steelblue',
                                                                     'lightslategrey', 'cadetblue', 'lightseagreen'])
                plt.xlabel('Seasons')
                plt.ylabel('Number of matches played')
                plt.title('Number of matches played each year')
                plt.grid(axis='y')
                plt.show()
            elif selection_var == 2:
                data_dict, lst_of_winning_team = stacked_bar_chart('live_db', 'matches')
                lst_every_team_data = matches_won_by_team(data_dict, sorted(lst_of_winning_team))
                plot_stacked_bar_graph(data_dict.keys(), lst_every_team_data)
            elif selection_var == 3:
                extra_run_per_team = match_2016_extra_run('live_db', 'matches', 'deliveries')
                plt.bar(list(extra_run_per_team.keys()), list(extra_run_per_team.values()),
                        color=['c', 'hotpink', 'darkslateblue', 'forestgreen', 'midnightblue', 'steelblue',
                               'lightslategrey', 'lightseagreen'])
                plt.xlabel('Team Name')
                plt.ylabel('Total Extra runs given in 2016')
                plt.title('Extra runs conceded per team')
                plt.grid(axis='y')
                plt.show()
            elif selection_var == 4:
                bowler_eco_rate = match_2015_eco_bowler('live_db', 'matches', 'deliveries')
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
                player_of_match = match_summary_over_years('live_db', 'matches', str(season))
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
