import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate("/home/joao/Tangram/adminKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'alunos').document(u'2')

doc_ref.set({
		u'nome':u'João',
		u'idade':u'58'
	})