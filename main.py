from http.client import HTTPException
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel
from typing import Optional,List
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from database import Base, engine, SessionLocal
from geopy.distance import great_circle

#  Model

class Address(Base):
    __tablename__="address"
    id = Column(Integer,primary_key = True, index = True)
    latitude = Column(String)
    longitude = Column(String)


# schema

class AddressSchema(BaseModel):
    id:int
    latitude:str
    longitude:str

    class Config:
        orm_mode=True

# schema 
class DistanceSchema(BaseModel):
    
    latitude:str
    longitude:str
    distance:float
    class Config:
        orm_mode=True


def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/address",response_model = AddressSchema)
def insert_address(address:AddressSchema,db:Session=Depends(get_db)):
    # db work to put data into db
    A = Address(id=address.id, latitude=address.latitude, longitude=address.longitude)
    db.add(A)
    db.commit()
    return A




@app.post("/get_address",response_model = DistanceSchema)
def custom_address(request:DistanceSchema,db:Session=Depends(get_db)):
    latitude = request.latitude
    longitude = request.longitude
    distance = request.distance

    all_address_ = db.query(Address).all()
    all_address_srializer = []
    for ele in all_address_:
        eldict = {
            "latitude":ele.latitude,
            "longitude":ele.longitude
        }
        all_address_srializer.append(eldict)
        
    def count_distance(all_address,latitude,longitude,given_distance):
        result = []
        for list_ele in all_address:
            newport_ri = (latitude, longitude)
            cleveland_oh = (list_ele["latitude"],list_ele["longitude"])
            distance = great_circle(newport_ri, cleveland_oh).km
            if given_distance >= distance:
                result.append({"latitude":list_ele["latitude"],"longitude":list_ele["longitude"]})
        return result
    final_result = count_distance(all_address_srializer,latitude =latitude,longitude=longitude,given_distance =distance )
    return JSONResponse(final_result)



@app.get("/address",response_model = List[AddressSchema])
def insert_address(db:Session=Depends(get_db)):
    return db.query(Address).all()




@app.put("/address/{address_id}",response_model = AddressSchema)
def update_address(address_id:int,address:AddressSchema,db:Session=Depends(get_db)):
    try:
        A=db.query(Address).filter(Address.id==address_id).first()
        A.latitude=address.latitude
        A.longitude=address.longitude
        db.add(A)
        db.commit()
        return A
    except:
        return HTTPException(status_code=404,detail = 'address not found')



@app.delete("/address/{address_id}",response_class = JSONResponse)
def delete_address(address_id:int,db:Session=Depends(get_db)):
    try:
        A=db.query(Address).filter(Address.id==address_id).first()
        db.delete(A)
        db.commit()
        return {f"address of id {address_id} has been deleted":True}
    except:
        return HTTPException(status_code=404,detail = 'address not found')