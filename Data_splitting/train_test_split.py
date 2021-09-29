import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from Data_collection.data_collect import get_data
from application_logging import logger

class seperate_ind_feat():
    """
       class Name  : seperate_ind_feat
       Description : This class is used to split the dataset in training and testing set.
       Written by  : Quad Intelligence
       Version     : 1.0
       Revision    : 0
       """
    def __init__(self):
        self.log_writer = logger.app_logger()
        self.file_object = open("C:/Users/HP/Desktop/wheat_3/Training_logs/traintestsplit.txt", 'a+')
    def x_y_feat(self):
        """
                Method_Name : x_y_feat
                Description : Splitting the dataset into dependent and independent features.
                Output      : DataFrame
                On Failure  : Raises Exception
                Written by  : Quad Intelligence
                Version     : 1.0
                Revision    : 0

                """

        self.log_writer.log(self.file_object, 'Train-Test split starts.')
        try:
            self.x = get_data().acquire_data_from_src().drop("Kernel_type",axis=1)
            self.y = get_data().acquire_data_from_src()["Kernel_type"]
            self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=1)
            return  self.x_train, self.y_train, self.x_test, self.y_test
            self.log_writer.log(self.file_object, 'Train-Test split ends.')
            self.file_object.close()
        except Exception as e:
            print(e)


s = seperate_ind_feat()
s.x_y_feat()
