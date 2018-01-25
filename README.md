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
example:
```
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

example:
```
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


## Insert new data to List
#### Request
- Method: **POST**
- URL:  ```/rollcallbackend.herokuapp.com/list/insertnewdatatolist```
   
- Headers：
    ```Content-Type: application/json```
- Body:
example:
```
{
  "insert_type":"addnew",
  "account":"swshawnwu@gmail.com",
  "list_name": "日本團",
  "data_list":
  [
	  {
     "QW:ED:AA:1S:66:89":"Rollcall_01",
     "B4:SD:55:2S:00:45":"Rollcall_02"
    }
  ] 

}
```

insert_type choose:add_new,extra_add:
extra_add meaning won't delete earlier data

#### Response
```
Response: Signup insert Success or Signup insert Fail
```
