from core import app, db
from core.models import ShortUrls
from random import choice
import string
from flask import render_template, request, redirect, url_for, flash

def generate_short_id(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']
        
        if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            flash('Short ID already exists!', 'danger')
            return redirect(url_for('index'))

        if not url: 
            flash('Please enter a valid URL!', 'danger')
            return redirect(url_for('index'))
        
        if not short_id:
            short_id = generate_short_id(8)
        
        new_link = ShortUrls(original_url=url, short_id=short_id)
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id
        
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


@app.route('/<short_id>')
def redirect_short_url(short_id):
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        # TODO: Add a counter to the link
        #link.visits = link.visits + 1
        #db.session.commit()
        return redirect(link.original_url)
    else:
        flash('Short URL does not exist!', 'danger')
        return redirect(url_for('index'))