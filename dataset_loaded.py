import pandas as pd

def load_dataset():

    df = pd.read_excel(
        "datasets/test.xlsx"
    )

    return df