# destarinc_project

# Setup project
```
git clone https://github.com/vikashkumarsaini9815/car_rental_company.git
```
#  installation
``` 
pip install -r requairments.txt
```
# Setup DB migration
```
connect sqllite
```
# Runserver 
```
uvicorn main:app --reload
```
# fast api for get address near by 
```
http://127.0.0.1:8000/docs#/default/fatch_address_address_get
Request Body :
        
Response Body :
        [{"id":1, "latitude":"42.3456", "longitude":"78.4567"},
        {"id":2, "latitude":"12.3456", "longitude":"82.4567"},
        {"id":3, "latitude":"17.3456", "longitude":"84.4567"}]


# fast api for create_address
```
127.0.0.1:8000/docs#/default/insert_address
Request Body :
  {"id":1, "latitude":"12.3456", "longitude":"88.4567"}
Response Body :
  {"id":1, "latitude":"12.3456", "longitude":"88.4567"}
```
# fast api for update_address
```
http://127.0.0.1:8000/docs#/default/update_address_address__address_id__put
Request Body : 
       {"id":1, "latitude":"12.3456", "longitude":"88.4567"}
Response Body :
       {"id":1, "latitude":"12.3456", "longitude":"88.4567"}
```
# fast api for delete
```
http://127.0.0.1:8000/docs#/default/delete_address_address__address_id__delete
Request Body :
        {"id":1}
Response Body :
        {"address of id 1 has been deleted":True}
```

# fast api for get address near by 
```
http://127.0.0.1:8000/docs#/default/custom_address_get_address_post
Request Body :
        {"latitude":"12.3456", "longitude":"88.4567", "distance":2}
Response Body :
        [{"latitude":"42.3456", "longitude":"78.4567"},
        {"latitude":"12.3456", "longitude":"82.4567"},
        {"latitude":"17.3456", "longitude":"84.4567"}]
        
        
```
