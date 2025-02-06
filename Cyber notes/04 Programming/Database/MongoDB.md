### Setup

Install community server: https://www.mongodb.com/try/download/community

Ensure .cfg file points to a path without spaces for log collection (`C:\Program Files\MongoDB\Server\8.0`)

Install MongoDB as a Microsoft service: 
```shell
mongod --config "C:\Program Files\MongoDB\Server\8.0\bin\mongod.cfg" --install
```

Start MongoDB server: `net start MongoDB`

___

