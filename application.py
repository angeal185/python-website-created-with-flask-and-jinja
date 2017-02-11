import info
from flask import Flask
from flask import render_template

application = Flask(__name__)

layout_args = {
    "meta" : info.meta,
    "navigation" : info.navigation,
	"footer" : info.footerIcons,
	"contact" : info.contact
}

@application.route("/")	
@application.route("/index")
@application.route("/index.py")
def home():
    return render_template("index.py", gallery=info.gallery, filter=info.filter, portfolio=info.portfolio, clogo=info.clogo, team=info.team, carousel=info.carousel, headings=info.headings, lorem=info.lorem, service=info.service, **layout_args)


if __name__ == "__main__":
    application.debug = True
    application.run()
