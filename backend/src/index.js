const express = require('express')
const mongoose = require('mongoose');
const env = require('dotenv')

env.config();

const app = express()

app.use(express.json()) //body parser

mongoose.connect(process.env.DB_URL);

const Cat = mongoose.model('Cat', {
    name: String
});

const kitty = new Cat({
    name: 'Zildjian'
});
kitty.save().then(() => console.log('meow'));

app.get('/', (req, res, next) => {
    res.status(200).json({
        message: 'Hello from server'
    })
})

app.post('/data', (req, res, next) => {
    res.status(200).json({
        message: req.body
    })
})

app.listen(process.env.PORT, () => {
    console.log(`Server is running on port ${process.env.PORT}`)
})