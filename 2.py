import pyperclip

def generate_team_member_html(input_text):
    # Split the input into lines
    lines = input_text.strip().split('\n')
    
    # Parse the lines
    name = lines[0].strip() if lines else ""
    title = lines[1].strip() if len(lines) > 1 else ""
    details = "<br>".join(line.strip() for line in lines[2:]) if len(lines) > 2 else ""
    
    # Generate the HTML
    html = f"""
    <div class="card">
        <img src="../images/Images-DW team" alt="Project 1">
        <div class="card-title">{name}</div>
        <div class="card-description">{title}<br>
            {details}
        </div>
    </div>
    """
    
    return html

# Example input
input_text = """Md. Sajib
Operator"""

# Generate HTML
html_output = generate_team_member_html(input_text)

# Copy the HTML to the clipboard
pyperclip.copy(html_output)

print("The HTML output has been copied to your clipboard. You can paste it wherever needed.")
