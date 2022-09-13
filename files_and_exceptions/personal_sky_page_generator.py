# to open/create a new html file in the write mode
i = str(input("name: "))
g = str(input("pro seby: "))
f = open('autobiography.html', 'w')

# the html code which will go in the file GFG.html
fop=f"""
<html>
<head></head>
<body>
    <center>
    <hl>{i}</hl>
    </center>
    <hr />
    {g}
    <hr />
    </body>
    </html>
"""

# writing the code into the file
f.write(fop)

# close the file
f.close()
