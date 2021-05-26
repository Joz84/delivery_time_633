import os
import pandas as pd
import re

class Olist:

    def __init__(self):
      self.root_path = os.path.dirname(__file__)
      self.csv_path = os.path.join(self.root_path, "..", "data", "csv")

    def __file_to_key(self, string):
        string = re.sub("_dataset.csv", "", string)
        string = re.sub(".csv", "", string)
        return re.sub("olist_", "", string)

    def __file_names(self):
        return [csv_file for csv_file in os.listdir(self.csv_path) if csv_file.endswith(".csv")]

    def __to_dataframe(self, csv_file):
        return pd.read_csv(os.path.join(self.csv_path, csv_file))

    def get_data(self):
        data = {}
        file_names = self.__file_names()
        for csv_file in file_names:
            data[self.__file_to_key(csv_file)] = self.__to_dataframe(csv_file)

        return data
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrame loaded from csv files
        """
        # Hint: Build csv_path as "absolute path" in order to call this method from anywhere.
        # Hint2: Use __file__ as absolute path anchor to avoid displaying your username or computer-specific folder architecture.
        # Hint3: Use os.path library to construct path independent of Unix vs. Windows specificities

    def get_matching_table(self):
        """
        01-01 > This function returns a matching table between
        columns [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """
        data = self.get_data()

        orders = data["orders"][["order_id", "customer_id"]]
        reviews = data["order_reviews"][["order_id", "review_id"]]
        items = data["order_items"][["order_id", "product_id", "seller_id"]]

        matching_table = orders.merge(reviews, on="order_id", how="outer").merge(items, on="order_id", how="outer")

        return matching_table

    def ping(self):
        """
        You call ping I print pong.
        """
        print('pong')
