const express = require('express')
const mongoose = require('mongoose');
const env = require('dotenv')
const userRoutes = require('./routes/user')

env.config();

const app = express()

app.use(express.json()) //body parser
app.use('/api', userRoutes)

mongoose.connect(process.env.DB_URL).then(
    console.log('connected to database')
);

app.listen(process.env.PORT, () => {
    console.log(`Server is running on port ${process.env.PORT}`)
})