from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db
from models.usuario import Usuario

main = Blueprint('main', __name__)

@main.route('/')
def index():
    username = session.get('username')  # Obtener el username de la sesión
    return render_template('index.html', username=username)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Verificar credenciales
        user = Usuario.query.filter_by(username=username).first()
        if user and user.password == password:  
            flash('Login exitoso', 'success')
            session['username'] = username  # Guardar el username en la sesión
            return redirect(url_for('main.index')) 
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')
            return redirect(url_for('main.login'))
    
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Verificar si el usuario ya existe
        user_exists = Usuario.query.filter_by(username=username).first()
        if user_exists:
            flash('El nombre de usuario ya está en uso.', 'danger')
            return redirect(url_for('main.register'))
        
        # Crear nuevo usuario
        new_user = Usuario(username=username, password=password,tipo_id=1)
        db.session.add(new_user)
        db.session.commit()

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')

@main.route('/aves')
def aves():
    return render_template('animals/aves.html')

@main.route('/reptiles')
def reptiles():
    return render_template('animals/reptiles.html')

@main.route('/reptiles/tortuga_caja')
def tortuga_caja():
    return render_template('animals/tortuga_caja.html')

@main.route('/mamiferos')
def mamiferos():
    return render_template('animals/mamiferos.html')

@main.route('/otros')
def otros():
    return render_template('animals/otros.html')


@main.route('/logout')
def logout():
    session.pop('username', None)
    flash('Has cerrado sesión.', 'success')
    return redirect(url_for('main.index'))



