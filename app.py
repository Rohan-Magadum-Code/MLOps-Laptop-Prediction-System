import pandas as pd
import joblib

class PredictionPipeline:

    def __init__(self):
        self.preprocessor = joblib.load("artifacts/data_transformation/preprocessor.pkl")
        self.model = joblib.load("artifacts/model_trainer/model.joblib")

    def get_dropdown_options(self):
        encoder = self.preprocessor.named_transformers_["cat"]

        return {
            "Company": encoder.categories_[0].tolist(),
            "TypeName": encoder.categories_[1].tolist(),
            "Cpu Name": encoder.categories_[2].tolist(),
            "Cpu brand": encoder.categories_[3].tolist(),
            "Gpu Brand": encoder.categories_[4].tolist(),
            "OS": encoder.categories_[5].tolist(),
        }

    def predict(self, data: pd.DataFrame):
        transformed_data = self.preprocessor.transform(data)
        prediction = self.model.predict(transformed_data)

        return prediction