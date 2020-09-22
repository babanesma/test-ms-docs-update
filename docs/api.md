# API documentation

## Create Item

```
POST /api/items
{
    "title": "item 1 title",
    "body": "item 1 description very long"
}
```

Response 

```
{
    "success": "true",
    "message": "item created successfully"
}
```

## Retrieve Item

```
GET /api/items/1
```

Response

```json
{
    "id": "123",
    "title": "item 123 title",
    "body": "item 123"
}
```