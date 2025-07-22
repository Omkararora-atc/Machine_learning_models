<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Loan Approval Prediction - Supervised Learning Project</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&display=swap');
        body {
            font-family: 'Montserrat', Arial, sans-serif;
            background: linear-gradient(135deg, #8ec5fc 0%, #e0c3fc 100%);
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 900px;
            margin: 40px auto;
            background: #fff;
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
            padding: 40px 50px 30px 50px;
        }
        h1 {
            text-align: center;
            font-size: 2.6em;
            color: #663399;
            letter-spacing: 2px;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #333;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .badge {
            display: inline-block;
            padding: 8px 18px;
            background: linear-gradient(90deg, #f7971e 0%, #ffd200 100%);
            color: #222;
            border-radius: 30px;
            font-weight: 700;
            margin: 0 7px 10px 0;
            font-size: 1em;
        }
        section {
            margin-bottom: 30px;
        }
        h2 {
            color: #4f2e93;
            border-bottom: 2px solid #e0c3fc;
            padding-bottom: 7px;
            margin-bottom: 15px;
        }
        ul, ol {
            margin: 0 0 0 25px;
            color: #444;
            line-height: 1.7;
        }
        .highlight {
            background: #e0c3fc;
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 1.1em;
            color: #4f2e93;
        }
        a {
            color: #f7971e;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            color: #663399;
            text-decoration: underline;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.98em;
        }
        @media (max-width: 600px) {
            .container { padding: 15px; }
            h1 { font-size: 2em; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Loan Approval Prediction</h1>
        <div class="subtitle">
            <span class="badge">Supervised Learning</span>
            <span class="badge">Machine Learning</span>
            <span class="badge">Classification</span>
        </div>
        <section>
            <h2>🚀 Project Overview</h2>
            <p>
                This project aims to build an intelligent system using supervised machine learning techniques to predict whether a loan application will be <span class="highlight">approved</span> or <span class="highlight">rejected</span> based on applicant data.
            </p>
        </section>
        <section>
            <h2>📦 Project Structure</h2>
            <ul>
                <li><b>Data Preprocessing:</b> Handle missing values, encode categorical data, and scale features.</li>
                <li><b>Model Building:</b> Apply various classification algorithms such as Logistic Regression, Decision Trees, Random Forest, etc.</li>
                <li><b>Evaluation:</b> Compare models using accuracy, precision, recall, F1-score, and confusion matrix.</li>
                <li><b>Prediction:</b> Predict loan status for new applicants.</li>
            </ul>
        </section>
        <section>
            <h2>🗂️ Folder Contents</h2>
            <ul>
                <li><b>loan_data.csv</b> &mdash; Dataset containing historical loan applications.</li>
                <li><b>loan_approval.ipynb</b> &mdash; Jupyter notebook with all code and analysis.</li>
                <li><b>model/</b> &mdash; Saved machine learning models.</li>
                <li><b>README.html</b> &mdash; This stylish project guide.</li>
            </ul>
        </section>
        <section>
            <h2>🧠 How It Works</h2>
            <ol>
                <li>Data is loaded and cleaned for analysis.</li>
                <li>Features are engineered and selected for optimal prediction.</li>
                <li>Multiple classification models are trained and compared.</li>
                <li>The best model is saved and used for predictions.</li>
            </ol>
        </section>
        <section>
            <h2>✨ Key Features</h2>
            <ul>
                <li>User-friendly notebook for step-by-step guidance.</li>
                <li>Handles missing values and categorical data automatically.</li>
                <li>Visualizations for better insight into data and model performance.</li>
                <li>Ready to integrate with web or desktop applications.</li>
            </ul>
        </section>
        <section>
            <h2>📈 Example Use Case</h2>
            <p>
                <span class="highlight">Banking & Finance:</span> Automate loan approvals to speed up decision-making and minimize risk.
            </p>
        </section>
        <section>
            <h2>🔗 Resources</h2>
            <ul>
                <li><a href="https://scikit-learn.org/" target="_blank">scikit-learn Documentation</a></li>
                <li><a href="https://pandas.pydata.org/" target="_blank">Pandas Documentation</a></li>
                <li><a href="https://matplotlib.org/" target="_blank">Matplotlib for Data Visualization</a></li>
            </ul>
        </section>
        <section>
            <h2>💡 Getting Started</h2>
            <ol>
                <li>Clone the repository:</li>
                <pre class="highlight">git clone https://github.com/Omkararora-atc/Machine_learning_models.git</pre>
                <li>Open <b>03_Loan_Approval/loan_approval.ipynb</b> in Jupyter Notebook or Google Colab.</li>
                <li>Follow the step-by-step instructions in the notebook.</li>
            </ol>
        </section>
        <div class="footer">
            &copy; 2025 &middot; Omkar Arora &middot; <a href="https://github.com/Omkararora-atc/Machine_learning_models" target="_blank">View on GitHub</a>
        </div>
    </div>
</body>
</html>