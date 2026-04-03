from flask import Flask, render_template, request
from connection import get_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def ask():
    if request.method == 'GET':
        return render_template('input_response.html')

    elif request.method == 'POST':
        role = request.form['role']
        language = request.form['language']
        exp = request.form['exp']

        user_prompt = f"""
Create an interview preparation roadmap.

Role: {role}
Programming Language: {language}
Experience: {exp} years

Output should include:
- DSA roadmap
- LeetCode practice questions list
- Most asked DSA interview questions
- Aptitude topics
- CS fundamentals topics
- Role specific topics
- Weekly plan
"""

        ai_response = get_response(user_prompt)

        return render_template('output_response.html', ai=ai_response)

app.run(debug=True)