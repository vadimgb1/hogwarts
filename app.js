const express = require('express')
const bodyParser = require("body-parser")
const app = express()

app.use(express.static('public'))
app.use(bodyParser.urlencoded({extended: true}))
var indexRouter = require('./routes/index.js')

app.use('/', indexRouter)
module.exports = app
