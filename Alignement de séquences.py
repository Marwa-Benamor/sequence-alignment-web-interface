from flask import Flask, render_template, request
from Bio.Align import PairwiseAligner
from Bio.Seq import Seq


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sequence1 = request.form['sequence1']
        sequence2 = request.form['sequence2']

        aligner = PairwiseAligner()
        alignments = aligner.align(sequence1, sequence2)

        # Recherche du meilleur alignement
        best_alignment = None
        best_score = float('-inf')

        for alignment in alignments:
            if alignment.score > best_score:
                best_alignment = alignment
                best_score = alignment.score

        return render_template('result.html', alignment=best_alignment, score=best_score)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)