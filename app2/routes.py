from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from app2 import app2_bp
from models import PageOperation
from app import db

@app2_bp.route('/')
@app2_bp.route('/index')
@login_required
def index():
    return redirect(url_for('app2.page1'))

@app2_bp.route('/page1')
@login_required
def page1():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app2',
        page_name='page1',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app2/page1.html', title='App2 - Page 1')

@app2_bp.route('/page2')
@login_required
def page2():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app2',
        page_name='page2',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app2/page2.html', title='App2 - Page 2')

@app2_bp.route('/page3')
@login_required
def page3():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app2',
        page_name='page3',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app2/page3.html', title='App2 - Page 3')

@app2_bp.route('/page4')
@login_required
def page4():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app2',
        page_name='page4',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app2/page4.html', title='App2 - Page 4')

@app2_bp.route('/page5')
@login_required
def page5():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app2',
        page_name='page5',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app2/page5.html', title='App2 - Page 5')
