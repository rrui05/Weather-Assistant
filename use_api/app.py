from flask import Flask, render_template, request, jsonify
from agent.Mylangchain import agent_executor

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def query_weather():
    user_input = request.json.get('input', '')
    if not user_input:
        return jsonify({'error': '请输入城市名称'}), 400

    try:
        result = agent_executor.invoke({"input": user_input})
        return jsonify({'response': result["output"]})
    except Exception as e:
        return jsonify({'error': f'查询失败: {str(e)}'}), 500

app.run(debug=True)