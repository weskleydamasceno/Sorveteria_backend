from flask import Flask, request, jsonify, abort
from app import app, db
from app.models.tables import Usuario, Remessa, Local


#Crud de Usuario
@app.route('/usuario', methods=['GET'])
def get_user():
    if request.method == 'GET':
        users = []
        userRes = Usuario.query.all()
        for us in userRes:
            user = {
                'id': us.id,
                'username': us.username,
                'senha': us.senha,
            }
            users.append(user)
       
        return jsonify({'usuarios': users})


@app.route('/usuario', methods=['POST'])
def create_user():
    user = {
        'username': request.json['username'],
        'senha': request.json['senha']
    }
    username = user['username']
    senha = user['senha']
    #print('UserName {}'.format(username))
    u = Usuario(username, senha)

    db.session.add(u)
    db.session.commit()

    return jsonify({'usuario': user}), 201


@app.route('/usuario/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = {
        'username': request.json['username'],
        'senha': request.json['senha']
    }
    userRes = Usuario.query.filter_by(id=user_id).first_or_404()
    if userRes == None:
        abort(404)
    userRes.username = user['username']
    userRes.senha = user['senha']

    db.session.commit()

    return jsonify({'usuario': user}), 204


@app.route('/usuario/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    userRes = Usuario.query.filter_by(id=user_id).first_or_404()
    if userRes == None:
        abort(404)
    db.session.delete(userRes)
    db.session.commit()
    return jsonify({'result': True})




#Crud de remessa
@app.route('/remessa', methods=['GET'])
def get_remessa():
    if request.method == 'GET':
        remessa = []
        remessaRes = Remessa.query.all()
        for re in remessaRes:
            rem = {
                'id': re.id,
                'data': re.data,
                'quantidade': re.qtde,
                'status': re.status,
                'vendidos': re.vendidos,
                'pagos': re.pagos,
                'usuario_id': re.usuario_id,
                'local_id': re.local_id
            }
            remessa.append(rem)
       
        return jsonify({'remessas': remessa})


@app.route('/remessa', methods=['POST'])
def create_remessa():
   
    rem = {
        'data': request.json['data'],
        'quantidade': request.json['quantidade'],
        'status': request.json['status'],
        'vendidos': request.json['vendidos'],
        'pagos': request.json['pagos'],
        'usuario_id': request.json['usuario_id'],
        'local_id': request.json['local_id']
            
    }
    data = rem['data']
    qtde = rem['quantidade']
    status = rem['status']
    vendidos = rem['vendidos']
    pagos = rem['pagos']
    usuario_id = rem['usuario_id']
    local_id = rem['local_id']

    #print('UserName {}'.format(username))
    r = Remessa(data, qtde, status, vendidos, pagos, usuario_id, local_id)

    db.session.add(r)
    db.session.commit()

    return jsonify({'remessa': rem}), 201
