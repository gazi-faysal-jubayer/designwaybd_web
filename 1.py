import pyperclip

def generate_html(input_text):
    # Split the input into lines and parse fields
    lines = input_text.split('\n')
    project = ''
    client = ''
    details = ''
    location = ''
    
    for line in lines:
        if line.startswith('Project:'):
            project = line.replace('Project:', '').strip()
        elif line.startswith('Client:'):
            client = line.replace('Client:', '').strip()
        elif line.startswith('Details:'):
            details = line.replace('Details:', '').strip()
        elif line.startswith('Location:'):
            location = line.replace('Location:', '').strip()
    
    # Generate the HTML based on the presence of project
    if project:
        html = f"""
        <div class="card">
            <img src="../images/projects/duplex/{project}.jpg" alt="Project 1">
            <div class="card-title">{project}</div>
            <div class="card-description"><b>Client:</b> {client}<br>
                <b>Details:</b> {details}<br>
                <b>Location:</b> {location}</div>
        </div>
        """
    else:
        html = f"""
        <div class="card">
            <img src="../images/projects/duplex/{client}.jpg" alt="Project 1">
            <div class="card-title">{client}'s Apartment</div>
            <div class="card-description"><b>Client:</b> {client}<br>
                <b>Details:</b> {details}<br>
                <b>Location:</b> {location}</div>
        </div>
        """
    
    return html

# Example input
input_text = """Client: Zakaria Hossain
Details: 2 Storied, 2000 S.ft.
Location: Ullahpara, Sirajganj"""

# Generate HTML
html_output = generate_html(input_text)

# Copy the HTML to the clipboard
pyperclip.copy(html_output)

print(html_output)

print("The HTML output has been copied to your clipboard. You can paste it wherever needed.")
