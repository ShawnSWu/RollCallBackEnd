from Application import create_app
import os

app = create_app()
port = int(os.environ.get('PORT', 33507))

# 確保被導入時不執行
if __name__ == '__main__':
    app.run()