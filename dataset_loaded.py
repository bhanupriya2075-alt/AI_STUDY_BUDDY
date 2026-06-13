import pandas as pd
from pypdf import PdfReader
import os


def load_csv_files():

    dataframes = []

    csv_files = [
        "datasets/train.csv",
        "datasets/test.csv",
        "datasets/validation.csv"
    ]

    for file in csv_files:

        if os.path.exists(file):

            df = pd.read_csv(file)

            dataframes.append(df)

    if dataframes:

        combined_df = pd.concat(
            dataframes,
            ignore_index=True
        )

        return combined_df

    return None


def load_pdf_files():

    pdf_text = ""

    pdf_files = [
        "datasets/physics.pdf",
        "datasets/biology.pdf",
        "datasets/political science.pdf"
    ]

    for file in pdf_files:

        if os.path.exists(file):

            reader = PdfReader(file)

            for page in reader.pages:

                text = page.extract_text()

                if text:

                    pdf_text += text + "\n"

    return pdf_text


def load_dataset():

    dataset = {}

    dataset["csv_data"] = load_csv_files()

    dataset["pdf_text"] = load_pdf_files()

    return dataset
