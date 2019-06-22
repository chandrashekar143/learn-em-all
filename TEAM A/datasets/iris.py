## Core Functionality to Load in Datasets

import numpy as np  
import pathlib
from sklearn.model_selection import train_test_split


def load_data(split=False,ratio=None,path='./data/iris.csv'): ## generalized function to load data
    """
    Loads in data from ./data/dataset.csv

    Parameters:
    =====================================
    1) dataset : takes in name of dataset to be loaded as input for eg. (dataset=iris)

    2) split : split the data in train and test datsets 

    3) ratio : ratio with which train and testing dataset need to be split. By default 80/20 (trian/test) ratio
 

    Returns:
    ======================================
    Returns a Dict. which contains:

    1) X : A 2-D numpy array representing our Dataset, with each row corresponding to a new entry 
           and each column corresponding to diffrent features

    2) y : A numpy array with corresponding classes that each row represents

    3) X_train : In case of split it represents data that will be used in for training

    4) X_test  : In case of split it represents data that will be used for testing purposes

    5) y_train : Corresponding classes of each row in training data

    6) y_test  : Corresponding classes of each row in testing data

    7) class_names : Name of classes of the given dataset

    8) features : Feature set of given dataset

    """
    
    if not pathlib.Path(path): ## if data is not available
        print('This Dataset is currently not supported. Please download via external source')
        return 
    
    ## load in the data
    data = np.genfromtxt(path,delimiter=',')
    X,y = data[:,:-1],data[:,-1] ## set in our X and y variables
    iris_dict = {}  ## the dict which will be returned


    if not split:
        iris_dict['X'] = X
        iris_dict['y'] = y
        
    else:
        X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=ratio,random_state=0,shuffle=True,stratify=y)
        iris_dict['X_train'],iris_dict['X_test'],iris_dict['y_train'],iris_dict['y_test'] = X_train,X_test,y_train,y_test

    iris_dict['class_names'] = ['Iris-setosa','Iris-versicolor','Iris-virginica']
    iris_dict['features'] = ['Sepal Length', 'Sepal Width', 'Petal Length' , 'Petal Width']
    return iris_dict




if __name__ == '__main__':
    data = load_data(split=True,ratio=0.7,path = '../data/iris.csv')
    print(data.keys())
    X_train = data['X_train']
    print(type(X_train),X_train.shape)
    print(X_train)