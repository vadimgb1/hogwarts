var express = require('express')
var router = express.Router()
var index_controller = require('../controllers/indexController.js')

router.get('/', index_controller.index)
router.get('/login', index_controller.login)
router.post('/login', index_controller.api_login)
module.exports =router