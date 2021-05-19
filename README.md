# Plovo
## API for Delivery Businesses

Plovo is a API made for Delivery companies also including restaraunts and cafes. It is a joke-copy project from Glovo. 

- Allow clients order dishes
- See the menus
- And many more (but not actually)

## API Specification

Для получения списка блюд необходимо отправить ```GET``` запрос на ```/dish/```:
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
Методы ``` POST, PUT, UPDATE, DELETE``` на ```/dish/``` вернут ошибку ```405```

