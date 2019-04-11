import web
from Models import RegisterModel

urls = { #Caminhos

    '/', 'Home',
    '/register', 'Register'
    '/login', 'Login',
    '/postregistration', 'PostRegistration'
}

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())

#Classes/Routes

class Home:
    def GET(self):
        return render.Home()

class Register:
    def GET(self):
        return render.Register()

class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input() #pega a data inserida
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


if __name__ == "__main__":
    app.run()
