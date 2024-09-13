from fastapi import FastAPI, UploadFile, File, HTTPException, Body
import csv
import sys


app = FastAPI()

csv_path = 'file.csv'
fieldnames = ['id','nome','cognome','codice_fiscale']


@app.post('/items/')
async def create(data: dict = Body()):

    with open('file.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerow(data)

    return data

@app.get('/items/')
async def read():

    result = []

    with open('file.csv', 'r', newline='') as csvfile: 
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            result.append(row)

    return result[1:]
