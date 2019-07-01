from flask import Flask, render_template
import numpy as np
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route('/')
def main_app():
    return render_template('index.html')

# @app.route('/risks')
# def get_risks():
#     all_risks = ['Risk 1', 'Risk 2', 'Risk 3']
#     return render_template('list.html', list=all_risks)

@app.context_processor
def test_vars():
    risks = ['Risk 1', 'Risk 2'] # risk names
    risk_weights = np.array([40, 60]) # universal risk weights
    risk_parameters = ['P1', 'P2', 'P3', 'P4', 'P5'] # parameter names
    parameter_points = [0.5, 1, 0.8, 0.3, 0.2]  # current situation
    x = np.array([[0, 10, 50, 80, 100], [20, 20, 20, 0, 0]]) # risk names
    score_matrix = np.multiply(x, risk_weights[:, None])
    score_matrix_1 = list(score_matrix[0])
    score_matrix_2 = list(score_matrix[1])
    total_scores = np.dot(risk_weights,x)
    total_score = sum(total_scores)
    total_ratios = total_scores / total_score
    final_results = total_ratios * parameter_points
    final_result = sum(final_results)
    plt.plot(risk_parameters, score_matrix_1 / total_score, color='b', marker='o', label=risks[0])
    plt.plot(risk_parameters, score_matrix_2 / total_score, color='r', marker='.', linewidth=2, label=risks[1])
    plt.plot(risk_parameters, final_results, color='k', linewidth=3, label='Final Result')
    plt.xlabel('Risk Parameters')
    plt.ylabel('Risk Weights & Score')
    plt.title('Risk Analysis of The Grid')
    plt.grid()
    plt.legend()
    strFile = 'static/plot.png'
    plt.savefig(strFile)
    return dict(
        risks=risks,
        risk_parameters=risk_parameters,
        risk_weights=risk_weights,
        parameter_points=parameter_points,
        r1=list(x[0]),
        r2=list(x[1]),
        score_matrix_1=score_matrix_1,
        score_matrix_2=score_matrix_2,
        total_scores=total_scores,
        total_score=total_score,
        total_ratios=total_ratios,
        final_results=final_results,
        final_result=final_result
    )