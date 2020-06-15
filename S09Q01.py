def webpage_data():
    title=input("Please enter the webpage title")
    main_header=input("Please enter the main header for your web page")
    sub_header=input("Please enter the sub header for your webpage")
    paragraph1=input("Please enter the paragraph1 in your webpage")
    paragraph2=input("Please enter the paragraph2 in your webpage")
    return title,main_header,sub_header,paragraph1,paragraph2
def create_webpage():
    title, main_header, sub_header, paragraph1, paragraph2=webpage_data()
    print("""  """,(("\u0332").join("Welcome to web page.html")),"""
           <html>
             <head>
                <title>
                """,title,"""
                </title>
            </head>
            <body>
                <h1>""",main_header,"""</h1>
                <h2>""",sub_header,"""</h2>
                
                <p1>""",paragraph1,"""
                </p1>
                <p2>""",paragraph2,"""
                </p2>
             </body>
            </html>""")
create_webpage()
