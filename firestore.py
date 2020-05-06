from google.cloud import firestore

def doc_to_dict(doc):
    if not doc.exists:
        return None
    doc_dict = doc.to_dict()
    doc_dict['id'] = doc.id
    return doc_dict

def read_all():
    db = firestore.Client()
    query = db.collection(u'Player')
    players = query.stream();
    players = list(map(doc_to_dict, players))
    return players

def read(id):
    db = firestore.Client()
    player = db.collection(u'Player').document(id)
    return doc_to_dict(player.get())


def update(data, player_id=None):
    db = firestore.Client()
    player = db.collection(u'Player').document(player_id)
    player.set(data)
    return doc_to_dict(player.get())

def delete(id):
    db = firestore.Client()
    player = db.collection(u'Player').document(id)
    player.delete()
