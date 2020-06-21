from flask import Flask, render_template, jsonify, request
import joblib
# from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/results', methods=['GET','POST'])
# def results():
    # if request.method == 'POST':
    #     inputtitle = request.form['']
    #     data = inputtitle.lower()
    #     cosScore = cosine_similarity(countmatrix.toarray())
    #     indices = pd.Series(dfNFRec['title'].str.lower())
    #     if data in indices.tolist():
    #         def recommend(title, cosScore=cosScore):
    #             idx = indices[indices == title].index[0]
    #             simscores = list(enumerate(cosScore[idx]))
    #             simscores = sorted(simscores, key=lambda x: x[1], reverse=True)
    #             simscores = simscores[1:11]
    #             movieshowindices = [i[0] for i in simscores]
    #             return df.iloc[]
        
    #         rec = recommend(data)

    #         return render_template('.', inputtitle=inputtitle, rec=rec)

    #     else:
    #         return render_template('')

@app.route('/data_visualization')
def data_visualization():
    return render_template('datavisualization.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')


if __name__ == '__main__':
    # countmatrix = joblib.load('') 
    # df = pd.read_csv('')
    # dfNFRec = pd.read_csv('')
    app.run(debug=True)
