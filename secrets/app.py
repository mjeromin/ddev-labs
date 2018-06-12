from flask import Flask, render_template
import requests, json, os

authtoken = open(os.environ['AUTHTOKEN'], 'r').readline().strip()
headers = {
    "Authorization": "token " + authtoken
}
app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():

  r = requests.get(
        'https://api.github.com/user/repos',
        headers=headers
      )
  return render_template('repos.html', repos=json.loads(r.text))

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
