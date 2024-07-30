# jovian-careers
Website for Flask practice

---

# Flask

- Flask is a lightweight webapp framework in python
- You can use **render_template** class of Flask to create a webpage, whereas **jsonify** can be used to create api endpoints
- Standard flask app directory structure is to keep all the html templates under template directory.
- Any static objects can be placed under **static** directory.
- Routes for your webapp can be created using **@app.route('/')** decorators. this example will create a route for **/** uri. Following function of the decorator will contain the logic that will run when this route is called.
- You can create dynamic routes, like **@app.route('/jobs/<id>')** here, any uri like /jobs/* is valid, and the string following jobs slash, will be contained in the id variable which can then be used in the following function for these types of routes

# Sqlalchemy

- **sqlalchmeny** can be used to perform any database related operations.
- you need to import, create_engine, text for creating the engine, to which a connection has to be made, and text for parsing the queries to be executed
- conn(), method is used to make a connection to the engine
- con.execute() is used to execute a query in the DB

# HTML Templating

- **{% include bootstrap.html%}** this is used to include other helper templates in the parent template
- In the templates you can use loops like for **{% for job in jobs %}**
and end using **{% endfor %}**
- Same way you can use an if statement as well. **{% if salary in jobs}**. and you can end it like **{% endif %}**
- 

# Extras

**urlib.parse** module's quote_plus function can be used to parse the URL strings with special characters, for example if your password contains an `@` you can pass it via quote_plus function

**os** module is used to do any operations at the os level. For example, reading environment variables using _os.environ('ENV_VARIABLE')_

# Best practices

- It's a best practice to modularize your templates as well as your python code. For example, your app.py should not contain any logic related to your databases operations. For any DB operations you can create a dedicated db.py module
- Similarly, for html, you can decouple the common components like, headers, footers, meta elements etc in separate templates and include them in the main templates.
