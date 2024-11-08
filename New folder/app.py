
from flask import Flask, render_template, request, redirect, url_for
    
app = Flask(__name__)
    
    # Home page
@app.route('/')
def home():
        return render_template('home.html')
    
    # Menu page
@app.route('/menu')
def menu():
        return render_template('menu.html')
    
    # Order page
@app.route('/order', methods=['GET', 'POST'])
def order():
        if request.method == 'POST':
            # Process order details here
            return redirect(url_for('home'))
        return render_template('order.html')
    
if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
    