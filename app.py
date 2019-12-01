from flask import Flask,request,render_template
app = Flask(__name__)

from commons import rest_of_code
from dotdot import dot

@app.route('/',methods = ['GET','POST'])
@app.route('/index')
def hello():
	if request.method == 'GET':
		return render_template('index.html',value = '1000')
		
	if request.method == 'POST':
		if 'file' not in request.files:
			print('file not uploaded')
			return 
		file = request.files['file']
		image = file.read()
		predictions = rest_of_code(image_bytes=image)
		path = dot(image_bytes=image,prediction=predictions)
		return render_template('result.html',xray = predictions,image_path=path)


if __name__ == '__main__':

    app.run(debug = True)


