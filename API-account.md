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
example:

{
  "account":"swshawnwu@gmail.com",
  "password": "66666666666"
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
example:

{
  "signup_account":"swshawnwu@gmail.com",
  "signup_password": "6666666666",
  "signup_name": "shawn"
}
```

#### Response
```
True or False:
```


## Procfile
#### Request
- Method: **POST**
- URL:  ```/rollcallbackend.herokuapp.com/account/getprocfiledata```
   
- Headers：
    ```Content-Type: application/json```
- Body:

```
example:

{
  "account":"swshawnwu@gmail.com",
  "password": "6666666666"
}
```

#### Response
```
Procfile data List

```


## Procfile Device of group Data
#### Request
- Method: **POST**
- URL:  ```/rollcallbackend.herokuapp.com/account/getprocfilegroupdevicedate```
   
- Headers：
    ```Content-Type: application/json```
- Body:

```
example:

{
  "account":"swshawnwu@gmail.com",
  "password": "6666666666"
}
```

#### Response
```
Group and device data
