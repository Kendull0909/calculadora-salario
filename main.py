from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = {}
    mensaje = ''

    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            horas = sum([
                float(request.form.get('martes', 0) or 0),
                float(request.form.get('miercoles', 0) or 0),
                float(request.form.get('jueves', 0) or 0),
                float(request.form.get('viernes', 0) or 0),
                float(request.form.get('sabado', 0) or 0),
                float(request.form.get('domingo', 0) or 0),
            ])

            horas_extra = float(request.form.get('horas_extra', 0) or 0)
            precio_hora = float(request.form.get('precio_hora', 0) or 0)
            rebajos = float(request.form.get('rebajos', 0) or 0)

            horas_totales = horas + horas_extra
            subtotal = horas_totales * precio_hora
            salario_final = subtotal - rebajos

            resultado = {
                'subtotal': subtotal,
                'salario_final': salario_final,
                'horas_trabajadas': horas,
                'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

        except ValueError:
            mensaje = "⚠️ Por favor, asegúrate de ingresar solo números válidos."

    return render_template('index.html', resultado=resultado, mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
