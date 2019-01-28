from flask import Flask 
import re
import random
import json

TXTFILE = 'wordlist'
app = Flask(__name__)

all_words = []
with open('./words/' + TXTFILE + '.txt', 'r') as f:
    all_words = [line.strip().upper() for line in f]

def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/newScramble')
def scramble():
    a = []
    while len(a) < 3:
        s = random.choice(all_words)
        a = [ans for ans in all_words if isAnagram(s, ans)]
    s = list(s)
    random.shuffle(s)
    s = "".join(s)
    return json.dumps({
        'scramble' : s,
        'answers' : a
    })

if __name__ == '__main__':    
    app.run(debug=True, port=5000)