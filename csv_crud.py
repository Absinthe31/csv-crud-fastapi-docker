from fastapi import FastAPI, UploadFile, File, HTTPException, Body
import csv
import sys


app = FastAPI()

csv_path = 'file.csv'
fieldnames = ['id','nome','cognome','codice_fiscale']


@app.post('/items/')
async def insert(data: dict = Body()):

    with open('file.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerow(data)

    return data

