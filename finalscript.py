import importlib
preprocess = importlib.import_module("preprocessing-script")
modeling = importlib.import_module("modeling-script")
predicting = importlib.import_module("predict")
modeling.train()
predicting.predict()