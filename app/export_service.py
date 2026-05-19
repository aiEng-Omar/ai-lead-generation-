import pandas as pd
import os


def export_to_csv(results, file_name="leads.csv"):
    os.makedirs("exports", exist_ok=True)

    df = pd.DataFrame(results)

    path = f"exports/{file_name}"

    df.to_csv(path, index=False)

    return path



def export_to_excel(results, file_name="leads.xlsx"):
    os.makedirs("exports", exist_ok=True)

    df = pd.DataFrame(results)

    path = f"exports/{file_name}"

    df.to_excel(path, index=False)

    return path