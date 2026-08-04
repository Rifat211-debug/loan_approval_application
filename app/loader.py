import os
import joblib

def load_models(config):
    cls_path = config['models']['classifier']
    reg_path = config['models']['regressor']
    if not os.path.exists(cls_path):
        raise FileNotFoundError(f"Classifier Not Found on : {cls_path}")
    if not os.path.exists(reg_path):
        raise FileNotFoundError(f"Regression Not Found on : {reg_path}")
    cls = joblib.load(cls_path)
    reg = joblib.load(reg_path)

    return cls, reg