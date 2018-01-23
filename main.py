from Application import create_app

app = create_app()

# 確保被導入時不執行
if __name__ == '__main__':
    app.run(host='rollcallbackend.herokuapp.com',port=33507)