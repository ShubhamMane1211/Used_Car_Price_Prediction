import joblib

from src.preprocess import preprocess_input


class CarPricePredictor:

    def __init__(self):

        self.model = joblib.load("models/best_model.pkl")

        self.make_encoder = joblib.load(
            "models/make_encoder.pkl"
        )

        self.feature_columns = joblib.load(
            "models/features.pkl"
        )

    def predict(self, user_input):

        processed = preprocess_input(

            user_input,

            self.make_encoder,

            self.feature_columns

        )

        prediction = self.model.predict(processed)

        return float(prediction[0])