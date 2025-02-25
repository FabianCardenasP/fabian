from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtener los datos del formulario
        R = request.form.get("R")
        T = request.form.get("T")
        HI = request.form.get("HI")
        HS = request.form.get("HS")
        AE = request.form.get("AE")
        AS = request.form.get("AS")
        N = request.form.get("N")
        CA = request.form.get("CA")
        MN = request.form.get("MN")
        Cr = request.form.get("Cr")

        # Aquí puedes procesar los datos (por ejemplo, guardarlos en una base de datos o hacer cálculos)
        print(f"Radio: {R}, Temperatura: {T}, Altura de entrada: {HI}, Altura de salida: {HS}, Ancho de entrada: {AE}, Ancho de salida: {AS}, RPM: {N}, Carbono: {CA}, Magnesio: {MN}, Cromo: {Cr}")

        # Puedes devolver un mensaje de éxito o redirigir a otra página
        return "Datos recibidos correctamente."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)