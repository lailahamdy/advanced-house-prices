from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import importlib
preprocess = importlib.import_module("preprocessing-script")

def train():
	X,y = preprocess.pipeline()
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=33)

	y_train= y_train.values.reshape(-1,1)
	y_test= y_test.values.reshape(-1,1)
	y_train = np.log(y_train)
	y_test = np.log(y_test)
	
	
	LR = LinearRegression()
	model = LR.fit(X_train,y_train)
	preds = model.predict(X_test)

	print('MAE:', metrics.mean_absolute_error(y_test, preds))
	print('MSE:', metrics.mean_squared_error(y_test, preds))
	print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, preds)))	

	return model
