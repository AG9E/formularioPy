from flask import Flask, request, render_template_string, render_template, url_for, redirect
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME') 
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

temp_data = {}

@app.route('/')
def form1():
    return render_template('form1.html')

@app.route('/form2', methods=['POST'])
def form2():
    global temp_data
    temp_data['nombre'] = request.form['nombre']
    temp_data['edad'] = request.form['edad']
    temp_data['email'] = request.form['email']
    temp_data['sexo'] = request.form['sexo']
    temp_data['civil'] = request.form['civil']
    temp_data['hijos'] = request.form['hijos']
    return render_template('form2.html')

@app.route('/form3', methods=['POST'])
def form3():
    global temp_data
    temp_data['conoce'] = request.form['conoce']
    temp_data['administra'] = request.form['administra']
    temp_data['preocupa'] = request.form['preocupa']
    temp_data['riesgo'] = request.form['riesgo']
    temp_data['prefiere'] = request.form['prefiere']
    return render_template('form3.html')

@app.route('/form4', methods=['POST'])
def form4():
    global temp_data
    temp_data['gustaria'] = request.form['gustaria']
    temp_data['posibilidad'] = request.form['posibilidad']
    return render_template('form4.html')

@app.route('/submit', methods=['POST'])
def submit():
    global temp_data
    temp_data['tipo'] = request.form['tipo']
    temp_data['diferida'] = request.form['diferida']
    temp_data['categoria'] = request.form['categoria']
    temp_data['moneda'] = request.form['moneda']

    sender = os.getenv('MAIL_USERNAME') 
    correo = temp_data['email']

    msg = Message('El producto de su preferencia Allianz', sender=sender, recipients=[correo])
    msg.body = '¡Gracias por tu preferencia!'

    if temp_data['tipo'] == 'Programada' and temp_data['categoria'] == 'Regular' and temp_data['moneda'] == 'Dólares':
        with open('pro_reg_usd.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Programada' and temp_data['categoria'] == 'Garantía' and temp_data['moneda'] == 'Dólares':
        with open('pro_gar_usd.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Programada' and temp_data['categoria'] == 'Mancomunada' and temp_data['moneda'] == 'Dólares':
        with open('pro_man_usd.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Programada' and temp_data['categoria'] == 'Regular' and temp_data['moneda'] == 'Reevaluable':
        with open('pro_reg_ree.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Programada' and temp_data['categoria'] == 'Garantía' and temp_data['moneda'] == 'Reevaluable':
        with open('pro_gar_ree.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Programada' and temp_data['categoria'] == 'Mancomunada' and temp_data['moneda'] == 'Reevaluable':
        with open('pro_man_ree.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Programada' and temp_data['categoria'] == 'Regular' and temp_data['moneda'] == 'Nominal':
        with open('pro_reg_nom.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Programada' and temp_data['categoria'] == 'Garantía' and temp_data['moneda'] == 'Nominal':
        with open('pro_gar_nom.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Programada' and temp_data['categoria'] == 'Mancomunada' and temp_data['moneda'] == 'Nominal':
        with open('pro_man_nom.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Vitalicia' and temp_data['categoria'] == 'Regular' and temp_data['moneda'] == 'Dólares':
        with open('vit_reg_usd.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Vitalicia' and temp_data['categoria'] == 'Garantía' and temp_data['moneda'] == 'Dólares':
        with open('vit_gar_usd.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Vitalicia' and temp_data['categoria'] == 'Mancomunada' and temp_data['moneda'] == 'Dólares':
        with open('vit_man_usd.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Vitalicia' and temp_data['categoria'] == 'Regular' and temp_data['moneda'] == 'Reevaluable':
        with open('vit_reg_ree.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Vitalicia' and temp_data['categoria'] == 'Garantía' and temp_data['moneda'] == 'Reevaluable':
        with open('vit_gar_ree.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Vitalicia' and temp_data['categoria'] == 'Mancomunada' and temp_data['moneda'] == 'Reevaluable':
        with open('vit_man_ree.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Vitalicia' and temp_data['categoria'] == 'Regular' and temp_data['moneda'] == 'Nominal':
        with open('vit_reg_nom.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Vitalicia' and temp_data['categoria'] == 'Garantía' and temp_data['moneda'] == 'Nominal':
        with open('vit_gar_nom.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    elif temp_data['tipo'] == 'Vitalicia' and temp_data['categoria'] == 'Mancomunada' and temp_data['moneda'] == 'Nominal':
        with open('vit_man_nom.html', 'r', encoding='utf-8') as f:
            msg.html = f.read()
    else:
        msg.subject = 'Opción por defecto'
        msg.html = '<p>Correo por defecto</p>'

    
    #with open('vitalicia_mancomunada_reevaluable.html', 'r', encoding='utf-8') as f:
        #msg.html = f.read()

    mail.send(msg)

    #with open('datos.txt', 'a') as f:
        #f.write(f"Nombre: {temp_data['nombre']}\nEdad: {temp_data['edad']}\nCorreo electrónico: {temp_data['email']}\nSexo: {temp_data['sexo']}\nEstado civil: {temp_data['civil']}\nNúmero de hijos: {temp_data['hijos']}\nFamiliarizado con planes de retiro: {temp_data['conoce']}\nSabe administrar su dinero: {temp_data['administra']}\nLe preocupa perder su dinero durante el retiro: {temp_data['preocupa']}\nTolerancia al riesgo: {temp_data['riesgo']}\nPagos garantizados frente a potenciales rendimientos más altos pero inciertos: {temp_data['prefiere']}\n¿Te gustaría proteger tus ingresos en el retiro a cambios en las tasas de interés y/o rentabilidad?: {temp_data['gustaria']}\n¿Te preocupa la posibilidad de que tus ingresos en el retiro no alcancen para toda tu vida?: {temp_data['posibilidad']}\nPrefiere: {temp_data['tipo']}\nPrefiere: {temp_data['diferida']}\nPrefiere: {temp_data['categoria']}\nPrefiere: {temp_data['moneda']}\n\n")
    #return f"Gracias, {temp_data['nombre']}."
    return redirect('https://www.allianz.com.mx')

if __name__ == '__main__':
    """
    app.run(debug=True)
    """
    app.run(debug=True, host='0.0.0.0', port=8000)



   