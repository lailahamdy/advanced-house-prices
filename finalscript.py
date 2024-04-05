import importlib
preprocess = importlib.import_module("preprocessing-script")
modeling = importlib.import_module("modeling-script")
data=preprocess.read_data()
x,y=preprocess.get_xy(data)
model=modeling.train()