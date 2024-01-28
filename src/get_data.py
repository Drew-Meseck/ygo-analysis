import src.scraping
import pandas as pd


def get_tournaments():
    data = src.scraping.get_tournaments()
    df = pd.DataFrame(data)
    save_tournaments(df)
    return 'Tournaments Successfully Saved'


def save_tournaments(tournaments_df): #Takes a df of tournament results and saves them to a csv
    path = 'src/data/tournaments.csv'
    tournaments_df.to_csv(path)

def get_tops():
    pass

def save_tops(tops_df):
    pass

def get_lists():
    pass

def save_lists(lists_df):
    pass
