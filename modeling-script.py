from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train():
	X,y = preprocessing-script.pipeline()
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=33)

	y_train= y_train.values.reshape(-1,1)
	y_test= y_test.values.reshape(-1,1)
	y_train = np.log(y_train)
	y_test = np.log(y_test)
	
	
	LR = LinearRegression()
	model = LR.fit(X_train,y_train)
	
	return model
