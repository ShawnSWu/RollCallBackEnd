from Application import create_app
import os

app = create_app()
port = int(os.environ.get('PORT', 5000))

# 確保被導入時不執行
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)