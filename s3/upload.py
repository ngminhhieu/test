import boto3
import json
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.encoders import jsonable_encoder
app = FastAPI()


class Description(BaseModel):
    x: float
    y: float
    w: float
    h: float
    label: str

class Label(BaseModel):
    img_path: str
    description: List[Description]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload")
def read_item(label: Label):
    label = jsonable_encoder(label)
    AWS_S3_BUCKET = "emed-pills"
    AWS_S3_KEY_ID = "AKIATRIFGFMDAAEWKHAY"
    AWS_S3_SECRET_KEY = "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"
    AWS_DEFAULT_ACL = "public-read"
    s3 = boto3.resource('s3',
        aws_access_key_id=AWS_S3_KEY_ID,
        aws_secret_access_key=AWS_S3_SECRET_KEY)
    file_json = "{}.json".format(label["img_path"])
    with open(file_json, 'w') as f:
        json.dump(label, f, ensure_ascii=False)
    return s3.meta.client.upload_file(file_json, AWS_S3_BUCKET, "labels/{}".format(file_json), ExtraArgs={'ACL':'public-read'})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)