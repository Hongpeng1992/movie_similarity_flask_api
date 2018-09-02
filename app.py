from flask import Flask
from flask_restful import reqparse, Api, Resource
import pickle
import pandas as pd

app = Flask(__name__)
api = Api(app)

# load similarity matrix
similarity_matrix = pd.read_csv("data//models/similarity_matrix.pkl")


# parse payload
parser = reqparse.RequestParser()
parser.add_argument('movie')


class MovieSimilarity(Resource):
    def get(self):
        seed_movie = parser.parse_args()
        output = {'movie': ['A','B','C'], 'similarity_score': [0,0,0]}
        return output


api.add_resource(MovieSimilarity, '/')


if __name__ == '__main__':
    app.run(debug=False)
