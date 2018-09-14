from src import dataProject1 as dp
import unittest


class TestDataProject(unittest.TestCase):

    sample_match = "/home/dell/PycharmProjects/data_project_unit_test/data/sample_matches.csv"
    sample_delivery = "/home/dell/PycharmProjects/data_project_unit_test/data/sample_delivery.csv"

    def test_number_of_matches_played_per_year(self):
        expected_season = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
        expected_value = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        lst_of_season, lst_of_matches_played_per_year = dp.num_of_match_each_year(self.sample_match)
        self.assertEqual(lst_of_season, expected_season)
        self.assertEqual(lst_of_matches_played_per_year, expected_value)

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
        dict_of_matches_won_each_season = dict(dp.stacked_bar_chart(self.sample_match)[0])
        self.assertEqual(dict_of_matches_won_each_season, expected_value)

    def test_match_2016_extra_run(self):
        expected_value = {'Rising Pune Supergiants': 0, 'Mumbai Indians': 0, 'Kolkata Knight Riders': 0,
                          'Delhi Daredevils': 0}
        extra_run_per_team = dp.match_2016_extra_run(self.sample_match, self.sample_delivery)
        self.assertEqual(extra_run_per_team, expected_value)

    def test_match_2015_eco_bowler(self):
        expected_value = {'UT Yadav': 3.0, 'JA Morkel': 12.0}
        bowler_eco_rate = dict(dp.match_2015_eco_bowler(self.sample_match, self.sample_delivery))
        self.assertEqual(bowler_eco_rate, expected_value)

    def test_match_summary_over_years(self):
        season = '2017'
        expected_value = {'Yuvraj Singh': 1, 'SPD Smith': 1}
        player_of_match = dict(dp.match_summary_over_years(self.sample_match, season))
        self.assertEqual(player_of_match, expected_value)


if __name__ == '__main__':
    unittest.main()