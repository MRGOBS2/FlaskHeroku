from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

future_jobs = [
    "Anggota Avanger", "Spiderman", "Gus", "Juragan Mie Ayam", "Dokter kelamin",
    "Pengangguran", "Iron Man", "Pawang Hujan", "Pakar Kelamin", "Pembalap"
]

form_html = '''
<!doctype html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Prediksi Pekerjaan Masa Depan</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(120deg, #89f7fe, #66a6ff);
      color: #333;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }

    h1 {
      color: #222;
      margin-bottom: 20px;
    }

    form {
      background: white;
      padding: 20px 30px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      text-align: center;
    }

    input[type="text"] {
      padding: 10px;
      width: 250px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 16px;
    }

    input[type="submit"] {
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      font-size: 16px;
      cursor: pointer;
    }

    input[type="submit"]:hover {
      background-color: #45a049;
    }

    h2 {
      margin-top: 30px;
      color: #fff;
      background: rgba(0,0,0,0.3);
      padding: 15px;
      border-radius: 10px;
    }

    strong {
      color: #ffd700;
    }
  </style>
</head>
<body>
  <h1>Prediksi Pekerjaan Masa Depan</h1>
  <form method="POST">
    <input type="text" name="nama" placeholder="Masukkan nama Anda" required><br>
    <input type="submit" value="Lihat Pekerjaan Masa Depan">
  </form>
  {% if nama and pekerjaan %}
    <h2>Halo {{ nama }}!<br>Pekerjaan masa depanmu adalah: <strong>{{ pekerjaan }}</strong></h2>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def prediksi_pekerjaan():
    nama = None
    pekerjaan = None
    if request.method == 'POST':
        nama = request.form['nama']
        pekerjaan = random.choice(future_jobs)
    return render_template_string(form_html, nama=nama, pekerjaan=pekerjaan)

if __name__ == '__main__':
    app.run(debug=True)
