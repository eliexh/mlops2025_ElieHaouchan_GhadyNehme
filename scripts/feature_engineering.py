from mlproject.features.featurize import feature_engineering
if __name__ == "__main__":
    feature_engineering("data/cleaned_train.csv", "data/features_train.csv")
