import os
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split


df = pd.read_csv("data/sephora_website_dataset.csv").drop("URL", axis=1)

le = LabelEncoder()
categorical_cols = df.select_dtypes(exclude=[np.number]).columns.to_list()
df[categorical_cols] = df[categorical_cols].apply(lambda col: le.fit_transform(col))

X = df.drop(['love', 'rating'], axis = 1)
y = df['love']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print("Shape of X_Train :", X_train.shape)
print("Shape of y_Train :", y_train.shape)
print("Shape of X_test :", X_test.shape)
print("Shape of y_test :", y_test.shape)
print()

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

load_models = input(":: Load previously trained models? [Y/n] ")
print()

models = list()
if load_models == 'Y' or load_models == 'y' or load_models == '':
    print('Loading models...')

    if len(os.listdir('models/')) == 0:
        print("No models found, you should train them first")
    else:
        # Load all models in the models dir
        for file in os.listdir('models'):
            with open('models/' + file, 'rb') as f:
                model = pickle.load(f)
                models.append(model)

        print('Models Loaded')

else:
    print('Training models...')
    models = [
        DecisionTreeRegressor(),
        RandomForestRegressor(),
        LinearRegression(),
        GradientBoostingRegressor()
    ]

    for model in models:
        print(f'=>> Currently Training {type(model).__name__}')
        model.fit(X_train, y_train)
        print(f'<<= {type(model).__name__} Trained\n')
        # Cache the model
        pickle.dump(model, open("models/" + type(model).__name__, 'wb+'))
    
for model in models:
    print(f'R2 Score with {type(model).__name__}: {model.score(X_test, y_test):.2f}')
