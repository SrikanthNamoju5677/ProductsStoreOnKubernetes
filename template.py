import sys

currentrelease = sys.argv[1]
currentreleaseyear = sys.argv[2]

print (currentrelease , currentreleaseyear)

default_template_content = """
<hr>
<h3><font face="Times New Roman">This release document contains updates for the currentrelease release w.r.t. currentreleaseyear release.</font></h3>
<hr>
<h2><font face="Times New Roman" color="#FF0000">Red Card</h2>
    <ul class="red_card">
	<li>None</li>	
    </ul>

<h2><font face="Times New Roman">Highlights</h2>

<h3><font face="Times New Roman">Infrastructure</h3>
    <ul class="highlights_infrastructure">
	<li>None</li>	
    </ul>

<h3><font face="Times New Roman">New Functionality</h3>
    <ul class="new_functionality">
	<li>None</li>	
    </ul>

<h3><font face="Times New Roman">Modified Functionality</h3>
    <ul class="modified_functionality">
	<li>None</li>	
    </ul>

<h3><font face="Times New Roman">Bug fixes</h3>
    <ul class="bug_fixes">
	<li>None</li>	
    </ul>

<h3><font face="Times New Roman">Graveyard applications, macros and sequences</h3>
    <ul class="graveyard">
	<li>None</li>	
    </ul>

<h2><font face="Times New Roman">What is new and what has changed</h2>

<h3><font face="Times New Roman">Infrastructure</h3>
    <ul class="new_changed_infrastructure">
	<li>None</li>	
    </ul>

<h3><font face="Times New Roman">User Interface</h3>
    <ul class="user_interface">
	<li>None</li>	
    </ul>

<h3>Macros</h3>
    <ul class="macros">
	<li>None</li>	
    </ul>

<h3>Applications</h3>
    <ul class="applications">
	<li>None</li>	
    </ul>
"""
with open("current_release.html", "w") as file:
  file.write(default_template_content)
print("default template created")
