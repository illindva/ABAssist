from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from app3 import app3_bp
from models import PageOperation
from app import db

@app3_bp.route('/')
@app3_bp.route('/index')
@login_required
def index():
    return redirect(url_for('app3.page1'))

@app3_bp.route('/page1')
@login_required
def page1():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app3',
        page_name='page1',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app3/page1.html', title='App3 - Page 1')

@app3_bp.route('/page2')
@login_required
def page2():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app3',
        page_name='page2',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app3/page2.html', title='App3 - Page 2')

@app3_bp.route('/page3')
@login_required
def page3():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app3',
        page_name='page3',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app3/page3.html', title='App3 - Page 3')

@app3_bp.route('/page4')
@login_required
def page4():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app3',
        page_name='page4',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app3/page4.html', title='App3 - Page 4')

@app3_bp.route('/page5')
@login_required
def page5():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app3',
        page_name='page5',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app3/page5.html', title='App3 - Page 5')
