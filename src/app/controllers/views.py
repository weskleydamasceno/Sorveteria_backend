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
        #print(request.args['id'])
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


@app.route('/remessa/<int:remessa_id>', methods=['PUT'])
def update_remessa(remessa_id):
    rem = {
        'data': request.json['data'],
        'quantidade': request.json['quantidade'],
        'status': request.json['status'],
        'vendidos': request.json['vendidos'],
        'pagos': request.json['pagos'],
        'usuario_id': request.json['usuario_id'],
        'local_id': request.json['local_id']
            
    }
    remessa = Remessa.query.filter_by(id=remessa_id).first_or_404()
    if remessa == None:
        abort(404)
    remessa.data = rem['data']
    remessa.qtde = rem['quantidade']
    remessa.status = rem['status']
    remessa.vendidos = rem['vendidos']
    remessa.pagos = rem['pagos']
    remessa.usuario_id = rem['usuario_id']
    remessa.local_id = rem['local_id']

    db.session.commit()

    return jsonify({'remessa': rem}), 204

@app.route('/remessa/<int:remessa_id>', methods=['DELETE'])
def delete_remessa(remessa_id):
    remessa = Remessa.query.filter_by(id=remessa_id).first_or_404()
    if remessa == None:
        abort(404)
    db.session.delete(remessa)
    db.session.commit()
    return jsonify({'result': True})



#Crud de local
@app.route('/local', methods=['GET'])
def get_local():
    if request.method == 'GET':
        locais = []
        loc = Local.query.all()
        for l in loc:
            local = {
                'id': l.id,
                'descricao': l.descricao
            }
            locais.append(local)
       
        return jsonify({'locais': locais})


@app.route('/local', methods=['POST'])
def create_local():
    local = {
        'descricao': request.json['descricao']
    }
    descricao = local['descricao']
    #print('UserName {}'.format(username))
    l = Local(descricao)

    db.session.add(l)
    db.session.commit()

    return jsonify({'local': local}), 201


@app.route('/local/<int:local_id>', methods=['PUT'])
def update_local(local_id):
    local = {
        'descricao': request.json['descricao']
    }
    loc = Local.query.filter_by(id=local_id).first_or_404()
    if loc == None:
        abort(404)
    loc.descricao = local['descricao']

    db.session.commit()

    return jsonify({'local': local}), 204


@app.route('/local/<int:local_id>', methods=['DELETE'])
def delete_local(local_id):
    local = Local.query.filter_by(id=local_id).first_or_404()
    if local == None:
        abort(404)
    db.session.delete(local)
    db.session.commit()
    return jsonify({'result': True})

@app.route("/remessa/filtro", methods=['GET'])
def get_remessa_filtrada():
    dataInicial = request.args['dataInicial']
    dataFinal = request.args['dataFinal']
    remessa = []
    remessaPeriodo = Remessa.query.filter(Remessa.data.between(dataInicial, dataFinal))
    for r in remessaPeriodo:
        rem = {
            'id': r.id,
            'data': r.data,
            'quantidade': r.qtde,
            'status': r.status,
            'vendidos': r.vendidos,
            'pagos': r.pagos,
            'usuario_id': r.usuario_id,
            'local_id': r.local_id
        }
        remessa.append(rem)

    return jsonify({'remessas': remessa})