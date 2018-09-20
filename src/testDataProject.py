from src import read_csv_create_table as db
from src import dataProject1 as dp
import unittest


class TestDataProject(unittest.TestCase):

    sample_match = "/home/dell/PycharmProjects/data_project_unit_test/data/sample_matches.csv"
    sample_delivery = "/home/dell/PycharmProjects/data_project_unit_test/data/sample_delivery.csv"

    sample_match1 = "/home/dell/PycharmProjects/data_project_unit_test/data/sample_matches1.csv"
    sample_delivery1 = "/home/dell/PycharmProjects/data_project_unit_test/data/sample_delivery1.csv"

    def setUp(self):
        # db.create_database('sample_test_db')
        # db.create_database('sample_test1_db')
        db.create_table(self.sample_match, 'sample_test_db', 'matches_test', 'n')
        db.create_table(self.sample_delivery, 'sample_test_db', 'delivery_test', 'y')
        db.create_table(self.sample_match1, 'sample_test1_db', 'matches_test1', 'n')
        db.create_table(self.sample_delivery1, 'sample_test1_db', 'delivery_test1', 'y')
        # print('running first')

    def tearDown(self):
        db.drop_database('sample_test_db')
        db.drop_database('sample_test1_db')
        # print('running last')

    def test_number_of_matches_played_per_year(self):
        expected_season = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
        expected_value = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        lst_of_season, lst_of_matches_played_per_year = dp.num_of_match_each_year('sample_test_db', 'matches_test')
        self.assertEqual(lst_of_season, expected_season)
        self.assertEqual(lst_of_matches_played_per_year, expected_value)

        expected_season1 = ['2015', '2016', '2017']
        expected_value1 = [2, 4, 4]
        lst_of_season, lst_of_matches_played_per_year = dp.num_of_match_each_year('sample_test1_db', 'matches_test1')
        self.assertEqual(lst_of_season, expected_season1)
        self.assertEqual(lst_of_matches_played_per_year, expected_value1)

    def test_stacked_bar_chart(self):
        expected_value = {'2008': {'Kolkata Knight Riders': 1, 'Chennai Super Kings': 1},
                          '2009': {'Mumbai Indians': 1, 'Royal Challengers Bangalore': 1},
                          '2010': {'Kolkata Knight Riders': 1, 'Mumbai Indians': 1},
                          '2011': {'Chennai Super Kings': 1, 'Rajasthan Royals': 1},
                          '2012': {'Mumbai Indians': 1, 'Delhi Daredevils': 1},
                          '2013': {'Kolkata Knight Riders': 1, 'Royal Challengers Bangalore': 1},
                          '2014': {'Kolkata Knight Riders': 1, 'Royal Challengers Bangalore': 1},
                          '2015': {'Kolkata Knight Riders': 1, 'Chennai Super Kings': 1},
                          '2016': {'Rising Pune Supergiants': 1, 'Kolkata Knight Riders': 1},
                          '2017': {'Sunrisers Hyderabad': 1, 'Rising Pune Supergiants': 1}}
        dict_of_matches_won_each_season = dict(dp.stacked_bar_chart('sample_test_db', 'matches_test')[0])
        self.assertEqual(dict_of_matches_won_each_season, expected_value)

        expected_value1 = {'2015': {'Kolkata Knight Riders': 1, 'Rajasthan Royals': 1},
                           '2016': {'Rising Pune Supergiant': 2, 'Kings XI Punjab': 1, 'Sunrisers Hyderabad': 1},
                           '2017': {'Sunrisers Hyderabad': 2, 'Kolkata Knight Riders': 1, 'Rising Pune Supergiant': 1}}
        dict_of_matches_won_each_season = dict(dp.stacked_bar_chart('sample_test1_db', 'matches_test1')[0])
        self.assertEqual(dict_of_matches_won_each_season, expected_value1)

    def test_match_2016_extra_run(self):
        expected_value = {'Delhi Daredevils': 0, 'Kolkata Knight Riders': 0, 'Mumbai Indians': 0,
                          'Rising Pune Supergiants': 0}
        extra_run_per_team = dp.match_2016_extra_run('sample_test_db', 'matches_test', 'delivery_test')
        self.assertEqual(extra_run_per_team, expected_value)

        expected_value1 = {}
        extra_run_per_team = dp.match_2016_extra_run('sample_test1_db', 'matches_test1', 'delivery_test1')
        self.assertEqual(extra_run_per_team, expected_value1)

    def test_match_2015_eco_bowler(self):
        expected_value = {'DJ Muthuswami': 12.0, 'IC Pandey': 12.0, 'JA Morkel': 12.0, 'MM Sharma': 3.0, 'UT Yadav': 3.0,
                          'NM Coulter-Nile': 12.0}
        bowler_eco_rate = dict(dp.match_2015_eco_bowler('sample_test_db', 'matches_test', 'delivery_test'))
        self.assertEqual(bowler_eco_rate, expected_value)

        expected_value1 = {'UT Yadav': 0.0, 'Ankit Sharma': 10.0}
        bowler_eco_rate = dict(dp.match_2015_eco_bowler('sample_test1_db', 'matches_test1', 'delivery_test1'))
        self.assertEqual(bowler_eco_rate, expected_value1)

    def test_match_summary_over_years(self):
        season = '2017'
        expected_value = {'Yuvraj Singh': 1, 'SPD Smith': 1}
        player_of_match = dict(dp.match_summary_over_years('sample_test_db', 'matches_test', season))
        self.assertEqual(player_of_match, expected_value)

        season1 = '2015'
        expected_value1 = {'AD Russell': 1, 'AM Rahane': 1}
        player_of_match = dict(dp.match_summary_over_years('sample_test1_db', 'matches_test1', season1))
        self.assertEqual(player_of_match, expected_value1)


if __name__ == '__main__':
    unittest.main()
