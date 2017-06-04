# filename = secure_filename(file.filename)
#             print(os.path.join(app.config['UPLOAD_FOLDER']))
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#             print(filename + " is saved and done !!")
#             apply_threshold(filename)
#             dig_string  = identify()
#             print(dig_string)
#             return render_template('home.html')
#
#
#
# 		if file and allowed_file(file.filename):
#             print("Hi this is the file")
#             return render_template('home.html')