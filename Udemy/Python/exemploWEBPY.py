import web

urls = {
    '/(.*)/(.*)', 'index'
}

render = web.template.render("resources/")
app = web.application(urls, globals())

class index:
    def GET(self, nome, idade):
        return render.main(nome, idade)

if __name__ == "__main__":
    app.run()
