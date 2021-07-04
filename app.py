from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('principal.html')


@app.route('/consulta')
def medicalConsultation():
    return render_template('menu.html')

@app.route('/antecedentes')
def medicalhistory():
    return render_template('history_patient.html')

@app.route('/sintomas')
def sympthons():
    return render_template('sympthons.html')

@app.route('/efectosdesencadenantes')
def triggersHeadache():
    return render_template('triggers.html')

@app.route('/alimentos')
def food():
    return render_template('food.html')

@app.route('/caracteristicasdeldolor')
def featuresPain():
    return render_template('actual_pain.html')

@app.route('/revisioninicial')
def secondaryHeadache():
    return render_template('secondary_diagnosis.html')

@app.route('/nuevopaciente')
def newPatient():
    return render_template('new_patient.html')

@app.route('/buscarpaciente')
def searchPatient():
    return render_template('look_for.html')

@app.route('/recuperarcontrasena')
def recoveryPassword():
    return render_template('recovery_pass.html')

@app.route('/diagnostico')
def diagnosis():
    return render_template('diagnosis.html')


if __name__ == '__main__':
    app.run(debug=True)