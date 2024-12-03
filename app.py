from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/web3-learning')
def web3_learning():
    return render_template('web3-learning.html')

@app.route('/trading-dashboard')
def trading_dashboard():
    return render_template('trading-dashboard.html')

@app.route('/portfolio-management')
def portfolio_management():
    return render_template('portfolio-management.html')

@app.route('/blockchain')
def blockchain():
    return render_template('blockchain.html')

@app.route('/contracts')
def contracts():
    return render_template('contracts.html')

# Route for NFTs page
@app.route('/nfts')
def nfts():
    return render_template('nfts.html')  # Adjust path if necessary


if __name__ == '__main__':
    app.run(debug=True)
