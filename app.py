from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Cargar modelo entrenado
modelo = joblib.load('modelo_insectos.pkl')

@app.route('/', methods=['GET', 'POST'])
def formulario():
    resultado = None

    if request.method == 'POST':
        abdomen = float(request.form['abdomen'])
        antena = float(request.form['antena'])
        prediccion = modelo.predict([[abdomen, antena]])
        resultado = prediccion[0]

    return render_template('formulario.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
