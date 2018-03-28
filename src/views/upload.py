# -*- coding: utf-8 -*-

import os
from flask import current_app as app
from werkzeug.utils import secure_filename
from flask import flash, render_template, request, redirect, send_from_directory

UPLOAD_FOLDER = os.getcwd() + '/uploads/'
ALLOWED_EXTENSIONS = ['py']    # list of allowed file extensions to upload.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER    # set upload-folder in app configuration (same as app.py line 27 fff).


def allowed_file(filename):
    """Function to check if user given file is allowed to be uploaded.

    :param filename: given filename to check
    :returns: True, False
    :rtype: bool

    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS    # return True if given filename has extension mentioned in extension-list.

@app.route('/upload', methods=['GET', 'POST'])    # method:get = asks for upload.html; method:post = form wants to upload file (see upload.html line 61 fff).
def upload_file():
    """Renders upload.html and processes upload of user files.

    :returns: none
    :rtype: none

    """
    if request.method == 'POST':    # if request is post
        if 'pyscript' not in request.files:    # if pyscript (see upload.html line 62) not in form-files
            flash('no file part in post request')    # user has not chosen anything, remind user.
            return redirect(request.url)    # reload page.
        file = request.files['pyscript']    # else user has chosen something, and file is uploaded file.
        if file.filename == '':    # if file has no name
            flash('no selected file available')    # remind user.
            return redirect(request.url)    # reload page.
        if file and allowed_file(file.filename):    # if file is allowed to be uploaded
            filename = secure_filename(file.filename)    # make sure filename is not dangerous (fe. /../../../../.bashrc --> after function: /.bashrc)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))    # and save file to upload-folder.
            flash('upload done')    # inform user.
            return redirect(request.url)    # reload page.
        flash('wrong extension')    # else no .py file, remind user.
        return redirect(request.url)    # reload page.
    return render_template('upload.html')    # request is get, therefore render page.

@app.route('/uploads/<filename>')
def display_file(filename):
    """Returns uploaded file.

    :param filename: name of uploaded file
    :returns: none
    :rtype: none

    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
