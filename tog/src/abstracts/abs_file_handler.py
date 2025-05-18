from tog.src.constants.path import Path
from abc import ABC
from typing import Final
import pandas as pd

#----------------------
# Class AbsFileHandler.
#----------------------


class AbsFileHandler(ABC):

    _file = None

    # Constants.
    DEFAULT_PK: Final = 'id'

    def __init__(self, file_name):
        self._file = pd.read_csv(Path.SOURCES_FOLDER + file_name, sep=';')

    ###############################
    ########## PROTECTED ##########
    ###############################

    def _find_value(self, id_value, column):
        """
        Find the value of a column given an id of a row. 
        It always returns one value.

        Parameters
        ----------
        id_value : string
            The value of the row id.
        column : string
            The column name.

        Returns
        -------
        string
            The value found. None if not found.
        """
        row = self._find_row(self.DEFAULT_PK, id_value)
        return self._find_value_in_row(row, column)

    def _find_value_in_row(self, row, column):
        """
        Find the value of a column given a pandas row. 
        It always returns one value.

        Parameters
        ----------
        row : Series
            A pandas row.
        column : string
            The column name.

        Returns
        -------
        value : string
            The value found. None if not found.
        """
        value = None
        if row is not None and column in row:
            value = row[column].values[0]

        return value
    
    def _find_row(self, pk, pk_value):
        """
        Find a row by its unique primary key. 

        Parameters
        ----------
        pk : string
            The primary key.
        pk_value : string
            The primary key value.

        Returns
        -------
        row : Series
            A pandas row.
        """
        row = None
        try:
            row = self._file.loc[self._file[pk] == pk_value] 
            if (self._is_row_empty(row)):
                row = None
        except Exception:
            raise Exception(f"Primary key {pk} value {pk_value} not found.")

        return row 

    def _is_row_empty(self, row):
        """
        Check if a pandas row is empty or not.

        Parameters
        ----------
        row : Series
            A pandas row.

        Returns
        -------
        bool
            If the row is empty or not.
        """
        return len(row.index) == 0
