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
        review_aroma = self.database.fetch_one("SELECT AVG(review_aroma) FROM reviews")
        review_appearance = self.database.fetch_one("SELECT AVG(review_appearance) FROM reviews")
        review_palate = self.database.fetch_one("SELECT AVG(review_palate) FROM reviews")
        review_taste = self.database.fetch_one("SELECT AVG(review_taste) FROM reviews")
        beer_abv = self.database.fetch_one("SELECT AVG(beer_abv) FROM reviews")
        # Obvious type cast error below :( Tuple = bad juju
        result = [
            ['Overall', review_overall],
            ['Aroma', review_aroma],
            ['Appearance', review_appearance],
            ['Palate', review_palate],
            ['Taste', review_taste],
            ['ABV', beer_abv],
        ]
        return result

