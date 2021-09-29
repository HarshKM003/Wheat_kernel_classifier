import pickle
from Model_building.model_formation import get_train_test_data
from Hyperparameter_tuning.h_tuning import p_tuning
from application_logging import logger

a = get_train_test_data()
p = p_tuning()

p.model_access()
p.set_parameters()
p.model_tuning()

pickle.dump(p.rf_best,open('model.pkl','wb'))
log_writer = logger.app_logger()
file_object = open("C:/Users/HP/Desktop/wheat_3/Training_logs/Smodel.txt", 'a+')
log_writer.log(file_object, 'Model Saved Successfully.')
file_object.close()
print("Success")