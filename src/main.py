from wenxin.api import chat
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/image', methods=['post'])
def image():
    print(request.json)
    text = request.json.get("text")
    try:
        answer, img = chat(text)
        print(answer)
    except:
        return jsonify({
            'code': 500
        })
    return jsonify({
        'code': 200,
        'img': img,
        'data': answer
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
