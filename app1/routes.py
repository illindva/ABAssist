from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_required, current_user
from app1 import app1_bp
from models import PageOperation
from app import db
from forms import XMLTemplateForm, XMLInputsForm, PlaceholderValueForm
import re
from typing import Dict, List, Optional, cast

@app1_bp.route('/')
@app1_bp.route('/index')
@login_required
def index():
    return redirect(url_for('app1.page1'))

@app1_bp.route('/page1')
@login_required
def page1():
    # Log the page operation
    operation = PageOperation()
    operation.user_id = current_user.id
    operation.app_name = 'app1'
    operation.page_name = 'page1'
    operation.operation = 'view'
    db.session.add(operation)
    db.session.commit()
    
    # Initialize XML template form
    xml_form = XMLTemplateForm()
    
    return render_template('app1/page1.html', title='App1 - Page 1', xml_form=xml_form)

@app1_bp.route('/generate_xml_form', methods=['POST'])
@login_required
def generate_xml_form():
    # Log the page operation
    operation = PageOperation()
    operation.user_id = current_user.id
    operation.app_name = 'app1'
    operation.page_name = 'generate_xml_form'
    operation.operation = 'generate_input_form'
    db.session.add(operation)
    db.session.commit()
    
    form = XMLTemplateForm()
    
    if form.validate_on_submit():
        xml_template = form.template_content.data
        
        if xml_template is None:
            xml_template = ""  # Default to empty string if None
            
        # Extract placeholders using regex pattern
        # Looking for INPUT1, INPUT2, etc.
        placeholders = re.findall(r'INPUT\d+', xml_template)
        
        # Parse tag names for each placeholder
        tag_names: Dict[str, str] = {}
        for placeholder in placeholders:
            # Find tag that contains this placeholder - allowing whitespace in tags
            pattern = r'<([^\s>]+)[^>]*>\s*' + re.escape(placeholder) + r'\s*</\s*\1\s*>'
            tag_match = re.search(pattern, xml_template)
            if tag_match:
                tag_names[placeholder] = tag_match.group(1)
            else:
                # Try a simpler pattern as fallback
                simple_match = re.search(r'<([^>]+)>[^<]*' + re.escape(placeholder) + r'[^<]*</\1>', xml_template)
                if simple_match:
                    tag_names[placeholder] = simple_match.group(1)
                else:
                    tag_names[placeholder] = placeholder
                
            # Print for debugging
            print(f"Placeholder: {placeholder}, Tag name: {tag_names[placeholder]}")
        
        # Create a form with fields for each placeholder
        inputs_form = XMLInputsForm()
        
        # Remove any existing entries and add fresh ones
        while len(inputs_form.placeholder_values) > 0:
            inputs_form.placeholder_values.pop_entry()
        
        # Add an entry for each placeholder
        for placeholder in placeholders:
            # Create a subform for this placeholder
            entry = PlaceholderValueForm()
            entry.placeholder_name.data = placeholder
            inputs_form.placeholder_values.append_entry(entry)
        
        # Store the template in the form
        inputs_form.template_content.data = xml_template
        
        return render_template('app1/xml_inputs.html', 
                              form=inputs_form, 
                              placeholders=placeholders,
                              tag_names=tag_names,
                              title='Enter XML Values')
    
    flash('There was an issue with the form. Please check and try again.', 'danger')
    return redirect(url_for('app1.page1'))

@app1_bp.route('/generate_final_xml', methods=['POST'])
@login_required
def generate_final_xml():
    # Log the page operation
    operation = PageOperation()
    operation.user_id = current_user.id
    operation.app_name = 'app1'
    operation.page_name = 'generate_final_xml'
    operation.operation = 'generate_final_xml'
    db.session.add(operation)
    db.session.commit()
    
    form = XMLInputsForm()
    
    if form.validate_on_submit():
        # Get the original template
        xml_template = form.template_content.data
        
        if xml_template is None:
            xml_template = ""  # Default to empty string if None
            
        # Replace each placeholder with its value
        for entry in form.placeholder_values:
            placeholder = entry.placeholder_name.data
            value = entry.placeholder_value.data
            
            if placeholder is not None and value is not None:
                # Replace the placeholder with the value
                xml_template = xml_template.replace(placeholder, value)
        
        # Render the template with the final XML
        return render_template('app1/xml_result.html', 
                              xml_content=xml_template,
                              title='Generated XML')
    
    flash('There was an issue with the form. Please check and try again.', 'danger')
    return redirect(url_for('app1.page1'))

@app1_bp.route('/page2')
@login_required
def page2():
    # Log the page operation
    operation = PageOperation()
    operation.user_id = current_user.id
    operation.app_name = 'app1'
    operation.page_name = 'page2'
    operation.operation = 'view'
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app1/page2.html', title='App1 - Page 2')

@app1_bp.route('/page3')
@login_required
def page3():
    # Log the page operation
    operation = PageOperation()
    operation.user_id = current_user.id
    operation.app_name = 'app1'
    operation.page_name = 'page3'
    operation.operation = 'view'
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app1/page3.html', title='App1 - Page 3')

@app1_bp.route('/page4')
@login_required
def page4():
    # Log the page operation
    operation = PageOperation()
    operation.user_id = current_user.id
    operation.app_name = 'app1'
    operation.page_name = 'page4'
    operation.operation = 'view'
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app1/page4.html', title='App1 - Page 4')

@app1_bp.route('/page5')
@login_required
def page5():
    # Log the page operation
    operation = PageOperation(
        user_id=current_user.id,
        app_name='app1',
        page_name='page5',
        operation='view'
    )
    db.session.add(operation)
    db.session.commit()
    
    return render_template('app1/page5.html', title='App1 - Page 5')
