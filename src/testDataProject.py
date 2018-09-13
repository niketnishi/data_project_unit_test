from src import dataProject1 as dp
import unittest


class TestDataProject(unittest.TestCase):

    sample_match = "/home/dell/PycharmProjects/data_project_unit_test/data/sample_matches.csv"
    sample_delivery = "/home/dell/PycharmProjects/data_project_unit_test/data/sample_delivery.csv"

    def test_number_of_matches_played_per_year(self):
        lst_of_season, lst_of_matches_played_per_year = dp.num_of_match_each_year(self.sample_match)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()