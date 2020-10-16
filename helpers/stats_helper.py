from helpers.database_helper import Database


class StatsHelper():

    def __init__(self):
        self.database = Database()
        print("Stats Helping initialising!")

    def caculate_ave_overall_rating(self):
        result = self.database.fetch_one("SELECT AVG(review_overall) FROM reviews")
        return result[0]

    # HINT: You can define more queries here, along with some python logic to calculate!
    def top_five_by_taste(self):
        result = self.database.fetch_all("SELECT * FROM reviews ORDER BY review_taste DESC LIMIT 5")
        return result

    def bottom_five_by_overall(self):
        result = self.database.fetch_all("SELECT * FROM reviews ORDER BY review_overall ASC LIMIT 5")
        return result

    def calculate_averages(self):
        review_overall = self.database.fetch_one("SELECT AVG(review_overall) FROM reviews")
        result = None
        return result

