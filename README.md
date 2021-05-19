# Plovo
## API for Delivery Businesses

Plovo is a API made for Delivery companies also including restaraunts and cafes. It is a joke-copy project from Glovo. 

- Allow clients order dishes
- See the menus
- And many more (but not actually)

## API Specification

To view DISH LIST make ```GET``` request to this url: ```/dish/```:
```json
[
    {
    "id": 7,
    "name": "Fish with lemon",
    "price": 200
    },
    {
        "id": 5,
        "name": "Балбан самсасы",
        "price": 155
    },
] 
```
Following methods ```diff  -POST, PUT, UPDATE, DELETE``` requested to this url: ```/dish/```  will reuturn following error: ```405``` .

