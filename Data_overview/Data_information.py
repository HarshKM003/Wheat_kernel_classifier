import pandas as pd
import numpy as np
from Data_collection.data_collect import get_data


class dinfo:
    """
    This class is used to figure out the size and shape and other informtion of the data.
    Written by: Quad Intelligence
    Version: 1.0
    Revisions: 0

    """

    def get_shape(self):
        """
        Method Name: get_shape()
        Description: It is used to get the shape of the data
        Output: 2-D array
        On failure: Raise Exception
        Written by: Quad Intelligence
        Version 1.0
        Revisions: 0

        """
        try:
            self.shape = get_data().acquire_data_from_src().shape
            print(self.shape)
        except Exception as e:
            print(e)
            raise e

    def get_info(self):

        """
        Method Name: get_info()
        Description: It finds other information of data
        Output: Pandas Dataframe
        On failure: raises Exception
        Written by: Quad Intelligence
        Version: 1.0
        Revisions: 0
        """
        try:
            self.info = get_data().acquire_data_from_src().info()
            print(self.info)
        except Exception as e:
            print(e)
            raise e

    def get_size(self):
        """
                Method Name : get_size()
                Description : This method is used to find overall size of the dataset loaded.
                output      : Integer Value
                on Failure  : raise exception
                Written by  : Quad Intelligence
                Version     : 1.0
                Revision    : 0

                """

        try:
            self.size = get_data().acquire_data_from_src().size()
            print(self.size)
        except Exception as e:
            print(e)


