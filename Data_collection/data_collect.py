import pandas as pd

class get_data:

    """
    This class helps in acquiring the data stored in the system.
    Written by : Quad Intelligence
    Version : 1.0
    Revisions : 0

    """
    def __init__(self):
        self.data_src = "C:/Users/HP/Desktop/wheat_3/Data/seeds_dataset.csv"
        self.delimiter = "\t"
        self.cols = ['Area','Perimeter','Compactness','Length_of_kernel','Width_of_kernel','Asymmetry_Coeff','Len_Kernel_Groove','Kernel_type']

    def acquire_data_from_src(self):

        """
        Method_name: acquire_data_from_src
        Description: It is used to get data from its source
        Output: Pandas Dataframe
        On_failure: Raises Exception
        Written by: Quad Intelligence
        Version: 1.0
        Revisions: 0

        """
        try:
            self.df = pd.read_csv(self.data_src,delimiter=self.delimiter,names=self.cols)
            return(self.df)
        except Exception as e:
            print(e)

g = get_data()
g.acquire_data_from_src()


