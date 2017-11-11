# heroku-multiflask
Deploy multiple flask apps to single heroku dyno

Using [honcho](https://github.com/nickstenning/honcho) to deploy multiple flask apps to single heroku dyno.

The flask app "FlaskWrapper" isn't required to just have multiple apps running but, when deployed to heroku,
only the one app is ever exposed to the outside. 
The apps started with honcho don't have to be only flask apps, [here](https://medium.com/@nadayar/heroku-fu-multiple-servers-on-one-dyno-6fc68d57b373) is an example of a similar method being used to deploy a node and python app simultaneously.

I'm not really convinced FlaskWrapper will ever really be useful but it at least shows that two flask apps are running on one dyno.

## Demo
https://heroku-multiflask.herokuapp.com/


## Run Locally
```bash
git clone https://github.com/charlesastaylor/heroku-multiflask.git
cd heroku-multiflask
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
honcho start
```

FlaskWrapper @ [localhost:5000](localhost:5000)

Flask1 @ [localhost:5001](localhost:5001) or [localhost:5000/flask1](localhost:5000/flask1)

Flask2 @ [localhost:5002](localhost:5002) or [localhost:5000/flask2](localhost:5000/flask2)

## Deploy to heroku

### Using heroku.com and GitHub Integration

* Fork this repo
* Create new heroku app ([Getting started on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction))
* Deploy using [GitHub Integration](https://devcenter.heroku.com/articles/github-integration)
* "Open app" from apps dashboard


### Using heroku cli

Assuming the heroku cli is installed (see [here](https://devcenter.heroku.com/articles/heroku-cli) if not) and you
are [autheniticated](https://devcenter.heroku.com/articles/authentication) by using `heroku login`, the steps to create a new
heroku app and deploy this repo would be:
```bash
git clone https://github.com/charlesastaylor/heroku-multiflask.git
cd heroku-multiflask
heroku create
git push heroku master
```
The app will then be accessible at the url outputed in the `heroku create` step.
