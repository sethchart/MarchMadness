import pandas as pd
from pathlib import Path
from pandas import DataFrame


class DataIO(object):
    """DataIO.
    This class encapsulates all loading and saving of data files.
    """

    def __init__(self, input_path: str, output_path: str):
        """__init__.

        Parameters
        ----------
        input_path : str
            input_path is a path to the input folder from which all data will
            be loaded.
        output_path : str
            output_path is a path to the output folder to which all data will
            be saved.
        """
        self.input_path = Path(input_path).absolute()
        self.output_path = Path(output_path).absolute()

    def load_data(self, file_name: str) -> DataFrame:
        """load_data. This method loads data from the specified csv file as a
        Dataframe.

        Parameters
        ----------
        file_name : str
            file_name is the name of a csv file to be loaded from the input
            folder.

        Returns
        -------
        DataFrame

        """
        file_path = self.input_path.joinpath(file_name)
        df = pd.read_csv(file_path)
        return df

    def save_data(self, df: DataFrame, file_name: str):
        """save_data. This method saves the contents of the specified
        DataFrame as a csv with the specified file name in the output folder.

        Parameters
        ----------
        df : DataFrame
            df is a DataFrame containing data to be saved.
        file_name : str
            file_name the file name for the csv file where the data should be
            saved.
        """
        file_path = self.output_path.joinpath(file_name)
        df.to_csv(file_path, index=False)

    def list_input_files(self):
        """list_input_files. This method prints a list of available input
        files.
        """
        contents = self.input_path.iterdir()
        for x in contents:
            if x.is_file() and x.name.endswith('.csv'):
                print(x.name)
