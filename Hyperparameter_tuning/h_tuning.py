from sklearn.model_selection import RandomizedSearchCV
from Model_building.model_formation import get_train_test_data
from sklearn import metrics
from application_logging import logger

class p_tuning:
    """
        Class_Name : p_tuning
        Description: This Class is used to perform hyperparamter tuning on the Random Forest model.
        Written By : Quad Intelligence
        Version    : 1.0
        Revisions  : 0
        """
    def __init__(self):
        self.a = get_train_test_data()
        self.log_writer = logger.app_logger()
        self.file_object = open("C:/Users/HP/Desktop/wheat_3/Training_logs/Htuning.txt", 'a+')

    def model_access(self):
        """
               Method Name : model_access
               Description : This method is used to access the training and testing data as well as machine learning model built.
               output      : DataFrame
               On_failure  : Raise Exception
               Written By  : Quad Intelligence
               Version     : 1.0
               Revision    : 0
               """

        try:
            self.val = self.a.retrieve_data()
            self.model = self.a.rfc_model()
        except Exception as e:
            raise e

    def set_parameters(self):
        """
                Method Name : set_parameters
                Description : This method is used to choose the best parameters and assigning it with set of values which can help our model to give better results.
                output      : None
                On_failure  : Raise Exception
                Written By  : Quad Intelligence
                Version     : 1.0
                Revision    : 0
                """
        try:
            self.param_grid = {
                'n_estimators': [x for x in range(10,3000,100)],
                'criterion': ['gini', 'entropy'],
                'max_features':['auto','log2',None],
                'min_samples_leaf':[int(x) for x in range(1,100,1)],
                'min_samples_split':[x for x in range(2,100,1)],
                'max_depth':[x for x in range(1,53,1)]
            }
        except Exception as e:
            raise e

    def model_tuning(self):
        """
        Method Name : model_tuning
        Description : This method is used to perform hyperparameter tuning using the set of values .
        output      : Acc.Scores
        On_failure  : Raise Exception
        Written By  : Quad Intelligence
        Version     : 1.0
        Revision    : 0
        """
        self.log_writer.log(self.file_object, 'Hyperparameter tuning starts.')
        try:
            self.rf_rcv = RandomizedSearchCV(estimator=self.a.rfc, param_distributions=self.param_grid, n_iter=200,
                                             cv=3, n_jobs=-1, random_state=10, verbose=True)
            self.rf_rcv.fit(self.a.x_train, self.a.y_train)

            self.rf_best = self.rf_rcv.best_estimator_
            print(self.rf_best)
            y_pre = self.rf_best.predict(self.a.x_test)

            print(metrics.accuracy_score(self.a.y_test, y_pre))
            print(self.rf_best.score(self.a.x_train, self.a.y_train))
            self.log_writer.log(self.file_object, 'Hyperparameter tuning ends.')
            self.file_object.close()
        except Exception as e:
            raise e

p = p_tuning()
p.model_access()
p.set_parameters()
p.model_tuning()