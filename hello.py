from flask import Flask, jsonify, request, render_template
import requests


app = Flask(__name__)

users = [
        {
            'username': 'admin',
            'password': 'admin',
            'alerts' : []
        }
        ]

current_user = [{
            'username': 'admin',
            'password': 'admin',
            'alerts' : []
        }]

connecte = [False]

@app.route("/")
def hello():
    if(connecte[0]):
        return render_template('connecte.html', user=current_user )
    else:
        return render_template('home.html')

@app.route("/test")
def get_data():
    import ws_connect 
    return 

# Route pour l'inscription d'un nouvel utilisateur
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Vérification si l'utilisateur existe déjà
    if any(user['username'] == username for user in users):
        return jsonify({'message': 'Utilisateur déjà existant'}), 400
    
    # Création d'un nouvel utilisateur
    new_user = {
        'username': username,
        'password': password,
        'alerts' : []
    }
    users.append(new_user)
    current_user[0] = new_user
    connecte[0] = True
    return render_template('connecte.html', user=current_user )

# Route pour la connexion d'un utilisateur
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Vérification si l'utilisateur existe
    user = next((user for user in users if user['username'] == username), None)
    if user is None or user['password'] != password:
        return jsonify({'message': 'Identifiants invalides'}), 401
    current_user[0] = user
    return jsonify({'message': 'Connexion réussie'}), 200

# Route pour afficher tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users}), 200

@app.route('/create_alert', methods=['POST'])
def create_alert():
    limite_haute = request.form.get('limite haute')
    limite_basse = request.form.get('limite basse')
    current_user[0]['alerts'].append((limite_basse,limite_haute))

    return render_template('connecte.html', user=current_user )

@app.route('/delete_alert', methods=['POST'])
def delete_alert():
    print(request.form.items())
    return render_template('connecte.html', user=current_user )

app.run()