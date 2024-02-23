from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = b'cxynbzgnrjzjss'

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "submit-name" in request.form:
            session["user"] = request.form["user-name"]
            return redirect(url_for('home'))
    session["user"] = session.get("user", "Anonymous_Duck")
    return render_template("home.html")

@app.route('/shopping', methods=["GET", "POST"])
def shopping_logic():

    session["your_cart"] = session.get("your_cart", []) 

    if request.method == "POST":

        if "add" in request.form:
            added = request.form["new_item"]
            temp = session["your_cart"]
            temp.append(added)
            session["your_cart"] = temp

        if "delete" in request.form:
            deleted = request.form["deleted_item"]
            temp = session["your_cart"]
            temp.remove(deleted)
            session["your_cart"] = temp
        
        return redirect(url_for('shopping_logic'))

    return render_template("shopping_page.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)