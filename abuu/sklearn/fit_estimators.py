from importlib import import_module
from typing import Union, List

mapper = {
    # Trees
    "dtc": ["sklearn.tree", "DecisionTreeClassifier"],
    "dtr": ["sklearn.tree", "DecisionTreeRegressor"],
    "etc": ["sklearn.tree", "ExtraTreeClassifier"],
    "etr": ["sklearn.tree", "ExtraTreeRegressor"],

    # SVM
    "svc": ["sklearn.svm", "LinearSVC"],
    "svr": ["sklearn.svm", "LinearSVR"],

    # Clustering
    "kmeans": ["sklearn.cluster", "KMeans"],

    # Ensemble
    "abc": ["sklearn.ensemble", "AdaBoostClassifier"],
    "abr": ["sklearn.ensemble", "AdaBoostRegressor"],
    "bc": ["sklearn.ensemble", "BaggingClassifier"],
    "br": ["sklearn.ensemble", "BaggingRegressor"],
    "etc": ["sklearn.ensemble", "ExtraTreesClassifier"],
    "etr": ["sklearn.ensemble", "ExtraTreesRegressor"],
    "gbc": ["sklearn.ensemble", "GradientBoostingClassifier"],
    "gbr": ["sklearn.ensemble", "GradientBoostingRegressor"],
    "rfc": ["sklearn.ensemble", "RandomForestClassifier"],
    "rfr": ["sklearn.ensemble", "RandomForestRegressor"],
}

unsupervised = set(["sklearn.cluster.KMeans"])

"""
Problem: When experimenting with models, and you just want to train something right away,
just to see how a model works right out of the box without any HP tuning, you need to do 3
statements: import, initialise and fit.

Also, when trying to fit multiple models, the import statement does get bigger
and more boilerplate is added, so this is a simple way of eliminating that
"""
def get_module(base:str, module:str):
        return getattr(import_module(base), module) 

def fit_one_estimator(abbr: str, X, y = None):
    cls, e = mapper[abbr]

    if f"{cls}.{e}" in unsupervised:
        assert y is None, "For unsupervised techniques, y must not exist"
    else:
        assert X is not None and y is not None, "X and y must exist"

    estimator = get_module(cls, e)

    if y is None:
        return estimator().fit(X)
    else:
        return estimator().fit(X, y)

def fit_estimators(abbr: Union[str, List[str]], X, y = None):
    if isinstance(abbr, str):
        assert abbr in mapper, "The abbr must be one of: {}".format(list(mapper.keys()))
        return fit_one_estimator(abbr, X, y)
    
    return list(map(lambda x: fit_one_estimator(x, X, y), abbr))


    
