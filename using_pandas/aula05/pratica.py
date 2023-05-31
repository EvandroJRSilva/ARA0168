import pandas as pd

iris = pd.read_csv('using_pandas/aula05/iris.data')

#print(iris)

sepal_columns = iris[['sepal length', 'sepal width']]
petal_columns = iris[['petal length', 'petal width']]

#print(sepal_columns.describe())
#print(petal_columns.describe())

petal_lenght_above3 = iris[iris['petal length'] > 3]
print(petal_lenght_above3)