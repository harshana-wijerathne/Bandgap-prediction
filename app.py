from flask import Flask,render_template,request
import pickle
import math
import numpy as np
app=Flask(__name__)

def prediction(lst):
    filename = 'model\Bandgap_predicter_model.pickle'
    with open(filename,'rb') as file:
        model = pickle.load(file)
    pred_value=model.predict([lst])
    return pred_value

def t(a,b,x,n):
    t=(a+x)/((2**0.5)*(b+x))
    return t
def tau(a,b,x,n):
    tau = (x/b)-n*(n-(a/b)/(math.log(a/b,math.e)))
    return tau
    



@app.route('/', methods=["POST","GET"])
def index():
    pred=0
    if request.method == 'POST':
        eleA=request.form["radiusA"]
        eleB=request.form["radiusB"]
        eleX=request.form["radiusC"]
        print(eleA)
        print(eleB)
        print(eleX)

        A=['Ag', 'Ba', 'Cs', 'In', 'K', 'Li', 'Rb', 'Tl', 'MA', 'FA']
        rA=[1.15, 1.64569, 1.88, 0.93412, 1.64, 1.18, 1.72, 1.7, 2.71, 2.85]
        nA=[1, 2, 1, 3, 1, 1, 1, 1, 1, 1]
        Ea=[7.57, 9.98, 3.89, 28.14, 4.34, 5.4, 2.52, 6.11, 9.3, 9.0]

        B = ['Al', 'As', 'Au', 'Ba', 'Be', 'Ca', 'Cd', 'Co', 'Cr', 'Cu', 'Fe', 'Ga', 'Ge', 'Hf', 'Hg', 'In', 'Ir', 'Li', 'Mg', 'Mn', 'Na', 'Ni', 'Os', 'P', 'Pb', 'Pd', 'Pt', 'Rh', 'Ru', 'Sb', 'Sc', 'Se', 'Si', 'Sn', 'Sr', 'Ti', 'Tl', 'V', 'Y', 'Zn', 'Zr', 'Ag']
        rB=[0.54, 0.46, 1.37, 1.61, 0.49, 1.0, 0.95, 0.74, 0.8, 0.73, 0.78, 0.62, 0.71, 1.02, 0.59, 0.72, 0.83, 0.69, 1.54, 1.19, 0.86, 0.77, 0.55, 0.68, 0.75, 0.64, 0.4, 1.15, 1.18, 0.84, 1.7, 0.79, 0.9, 0.46078, 0.48843, 0.798, 0.71086, 1.01911, 0.59208, 0.71593, 0.69063, 0.70866, 1.53591, 0.77291, 0.55121, 0.68203, 0.61543, 0.84183, 0.72001]
        nB=[3, 5, 1, 2, 2, 2, 2, 3, 3, 2, 3, 3, 4, 4, 2, 3, 3, 1, 2, 3, 1, 2, 4, 5, 2, 2, 2, 3, 3, 3, 3, 2, 4, 4, 2, 4, 2, 5, 2, 2, 2, 1]
        Eb=[27.45, 62.73, 8.9, 9.65, 17.81, 11.87, 16.91, 32.45, 29.61, 20.29, 30.63, 30.7, 45.81, 31.26, 18.76, 28.6, 30.08, 5.39, 15.03, 33.43, 5.14, 18.17, 44.9, 65.12, 21.47, 19.52, 18.56, 31.06, 28.47, 25.56, 24.36, 21.2, 45.14, 40.73, 11.03, 40.98, 24.56, 65.23, 12.24, 17.96, 14.61, 7.57]
        
        X=['F', 'Cl', 'Br', 'I']
        rX=[1.33, 1.81, 1.96, 2.2]
        nX=[-1, -1, -1, -1]
        Ex=[-3.28, -3.61, -3.36, -3.06]


        features=[]
        '''radius value append'''
        features.append(rA[A.index(eleA)])
        features.append(rB[B.index(eleB)])
        features.append(rX[X.index(eleX)])

        '''valance value append'''
        features.append(nA[A.index(eleA)])
        features.append(nB[B.index(eleB)])
        features.append(Eb[X.index(eleX)])

        '''valance value append'''
        features.append(Ea[A.index(eleA)])
        features.append(Eb[B.index(eleB)])
        features.append(Ex[X.index(eleX)])

        print(features)

        pred=prediction(features)
        print(pred)

        tau1= tau(features[0],features[1],features[2],features[8])
        t1= t(features[0],features[1],features[2],features[8])


        formula= eleA+eleB+eleX
        print(formula)


    '''return render_template("index.html", pred_value = pred, t_value=t1, tau_value=tau1,fomula=formula)'''
    return render_template("index.html", pred_value = np.round(pred[0],3), fomula=formula, tau_value=np.round(tau1,3),t_value=np.round(t1,3))


if __name__ == "__main__":
    app.run(debug=True)