import pandas as pd
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

# Cargamos los datos
car_data = pd.read_csv('../data/cars.csv', sep=';')

# Definimos las variables predictoras y la variable objetivo
X = car_data.drop(labels=['Mas_1_coche'], axis=1)
y = car_data['Mas_1_coche']

# Estandarizamos los datos

# 1º Filtramos las cols que tengan valores mayores a 1
cols = [col for col in X.columns if X[col].max() > 1]

# 2º Se recorren las columnas especificadas y se escala cada una
for col in cols:
    X[col] = scale(X[col])

# Dividimos los datos en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)


# Entrenamos el modelo de Gradient Boosting
gb_model = GradientBoostingClassifier(random_state=912)
gb_model.fit(X_train, y_train)
gb_pred = gb_model.predict(X_test)

# Entrenamos el modelo de Extreme Gradient Boosting
xgb_model = xgb.XGBClassifier(random_state=912)