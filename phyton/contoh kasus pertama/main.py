from flask import Flask, redirect, url_for

app = Flask(__name__)

# Router Admin
@app.route('/admin')
def admin():
    return "Halo, Admin!"


# Router Tamu dengan parameter nama
@app.route('/guest/<guestname>')
def guest(guestname):
    return 'Accueillir nos hôtes, {}.'.format(guestname)

# Membuat router untuk mengalihkan router lainnya
@app.route('/user/<user>')
def user(user):
    if user == "Admin":
        return redirect(url_for("admin")) # paramater fungsi admin
    else:
        return redirect(url_for("guest", guestname = user)) # paramater fungsi guest

if __name__ == '__main__':
    app.run(debug=True)