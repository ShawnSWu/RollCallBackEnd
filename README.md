# RollCallBackEnd

# API
 http://rollcallbackend.herokuapp.com/

## sign up
#### Request
- Method: **POST**
- URL:  ```/rollcallbackend.herokuapp.com/account/signup```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
{
  "account":"email",
  "password": "password"
}
```

#### Response
```
Signup Success or Signup Fail
```




## log in
#### Request
- Method: **POST**
- URL:  ```/rollcallbackend.herokuapp.com/account/login```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
{
  "signup_account":"email",
  "signup_password": "password",
  "signup_name": "username"
}
```

#### Response
```
True or False
```
