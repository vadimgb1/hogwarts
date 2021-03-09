exports.index = (req, res) => res.render('index/index.ejs')
exports.login = (req, res) => res.render('index/login.ejs')
exports.api_login = (req, res) =>
{
    let {username, password} = req.body
    console.log(username)
    console.log(password)
    res.redirect("/")
}