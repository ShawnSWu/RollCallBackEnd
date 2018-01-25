# API
 http://rollcallbackend.herokuapp.com/

## Insert new data to List
#### Request
- Method: **POST**
- URL:  ```/rollcallbackend.herokuapp.com/list/insertnewdatatolist```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "insert_type":"add_new",
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
| insert_type | Meaning |
| ------| ------ | 
| add_new | add a few new data | 
| extra_add | won't delete earlier data | 


#### Response
```
Response: Signup insert Success or Signup insert Fail
```







## Get List Data
#### Request
- Method: **POST**
- URL:  ```/rollcallbackend.herokuapp.com/list/getlistdata```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "account":"swshawnwu@gmail.com",
  "list_name": "日本團"
}
```
#### Response
```
Data list(Json)
```


## Get All List name in account
#### Request
- Method: **POST**
- URL:  ```/rollcallbackend.herokuapp.com/list/getalllistdata```
   
- Headers：
    ```Content-Type: application/json```
- Body:
```
example:

{
  "account":"swshawnwu@gmail.com"
}
```
#### Response
```
 list Data(Json)
```
