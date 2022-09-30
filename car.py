# 8.14
def make_car(make, model, **features):
    dict = {"make": make, "model": model}
    for feature in features.items():
        dict[feature[0]] = feature[1]
    
    return dict
