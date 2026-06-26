from src.predict import CarPricePredictor

predictor = CarPricePredictor()

car = {

    "symboling":1,

    "normalized-losses":120,

    "make":"toyota",

    "fuel-type":"gas",

    "aspiration":"std",

    "num-of-doors":"four",

    "body-style":"sedan",

    "drive-wheels":"fwd",

    "engine-location":"front",

    "wheel-base":97,

    "length":170,

    "width":65,

    "height":54,

    "curb-weight":2400,

    "engine-type":"ohc",

    "num-of-cylinders":"four",

    "engine-size":130,

    "fuel-system":"mpfi",

    "bore":3.46,

    "stroke":3.19,

    "compression-ratio":9,

    "horsepower":111,

    "peak-rpm":5000,

    "city-mpg":24,

    "highway-mpg":30
}

price = predictor.predict(car)

print(price)