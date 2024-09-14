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
async def read_all():

    result = []

    with open('file.csv', 'r', newline='') as csvfile: 
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            result.append(row)

    return result[1:]

@app.get('/items/{token}')
async def read_or_count(token: str):

    if token == 'count':

        data = []

        with open('file.csv', 'r', newline='') as csvfile: 
            reader = csv.DictReader(csvfile, fieldnames)
            for row in reader:
                data.append(row)

        return {"count" : len(data[1:])}

    else: 

        result = None

        with open('file.csv', 'r', newline='') as csvfile: 
            reader = csv.DictReader(csvfile, fieldnames)
            for row in reader:
                if row['id'] == token:
                    result = row

        return result if result != None else {"message" : "id not found"}

@app.put('/items/{id}')
async def update(id: str, data: dict=Body()):

    old_data = []

    with open('file.csv', 'r', newline='') as csvfile: 
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            old_data.append(row)

    with open('file.csv', 'w', newline='') as csvfile: 
         writer = csv.DictWriter(csvfile, fieldnames)
         writer.writeheader()

    with open('file.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)

        for row in old_data[1:]:

            if row['id'] == id:
                writer.writerow(data)
            else:
                writer.writerow(row)

    return data

@app.delete('/items/{id}')
async def delete(id: str):

    old_data = []

    with open('file.csv', 'r', newline='') as csvfile: 
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            old_data.append(row)

    with open('file.csv', 'w', newline='') as csvfile: 
         writer = csv.DictWriter(csvfile, fieldnames)
         writer.writeheader()

    with open('file.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)

        for row in old_data[1:]:

            if row['id'] != id:
                writer.writerow(row)

    return {"message" : "Item deleted succesfully"}
