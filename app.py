from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {'id': 1,
   'title': 'Engineer',
   'location': 'West Indies',
   'salary': '£80,000',
  },
  {'id': 2,
    'title': 'Borracheiro',
    'location': 'Italy',
    'salary': '£25,000',
  },
  {'id': 3,
    'title': 'Driver',
    'location': 'Los Angeles',
  },
  {'id': 4,
    'title': 'Engineer Backend',
    'location': 'San Francisco',
    'salary': '£80,000',
}
]

app = Flask(__name__,template_folder='Templates')
@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name= "OOstrich Esmeralda")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
