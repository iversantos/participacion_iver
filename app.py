from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'  

usuarios = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        
        if username in usuarios:
            flash('El nombre de usuario ya existe. Elige otro.')
            return redirect(url_for('register'))
        
       
        usuarios[username] = password
        flash('Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect(url_for('home'))
    
    return render_template('register.html')

@app.route('/index', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in usuarios and usuarios[username] == password:
        session['username'] = username  
        return redirect(url_for('bienvenida'))  
    else:
        flash('Credenciales incorrectas. Intenta de nuevo.')  
        return redirect(url_for('home')) 

@app.route('/bienvenida')
def bienvenida():
    if 'username' in session: 
        return render_template('bienvenida.html', username=session['username']) 
    else:
        return redirect(url_for('home'))  

@app.route('/logout')
def logout():
    session.pop('username', None)  
    return redirect(url_for('home'))  

if __name__ == '__main__':
    app.run(debug=True)