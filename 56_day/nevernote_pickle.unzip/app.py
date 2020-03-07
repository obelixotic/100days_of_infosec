#!/usr/bin/env python3

from flask import Flask, render_template, send_from_directory, request, redirect
from werkzeug import secure_filename

import pickle
import os # i hope no one uses os.system

NOTE_FOLDER='notes/'


class Note(object):
    def __init__(self, title, content, image_filename):
        self.title=title
        self.content=content
        self.image_filename=secure_filename(image_filename)
        self.internal_title=secure_filename(title)


def save_note(note, image):
    note_file=open(NOTE_FOLDER + secure_filename(note.title + '.pickle'), 'wb')
    note_file.write(pickle.dumps(note))
    note_file.close()

    image.save(NOTE_FOLDER + note.image_filename)


def unpickle_file(file_name):
    note_file=open(NOTE_FOLDER + file_name, 'rb')
    return pickle.loads(note_file.read())


def load_all_notes():
    notes=[]
    for filename in os.listdir(NOTE_FOLDER):
        if filename.endswith('.pickle'):
            notes.append(unpickle_file(filename))
    return notes


app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', notes=load_all_notes())


@app.route('/notes/<file_name>')
def notes(file_name):
    if request.args.get('view', default=False):
        ##################################################################
        # let me go ahead and unpickle whatever file is being requested...
        ##################################################################
        note=unpickle_file(file_name)
        return render_template('view.html', note=note)
    else:
        ##################################################################
        # let me go ahead and send whatever file is being requested...
        ##################################################################
        return send_from_directory(NOTE_FOLDER, file_name)


@app.route('/new', methods=['GET', 'POST'])
def note_new():
    if request.method == "POST":
        image=request.files.get('image')
        if not image.filename.endswith('.png'):
            return 'nah bro png images only!', 403
        new_note=Note(
            request.form.get('title'),
            request.form.get('content'),
            image_filename=image.filename
        )
        save_note(new_note, image)
        return redirect('/notes/' + new_note.internal_title + '.pickle' + '?view=true')
    return render_template('new.html')


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000
    )
