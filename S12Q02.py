import sys
def webpage_data():
    title = input("Please enter the webpage title")
    main_header = input("Please enter the main header for your web page")
    sub_header = input("Please enter the sub header for your webpage")
    paragraph1 = input("Please enter the paragraph1 in your webpage")
    paragraph2 = input("Please enter the paragraph2 in your webpage")
    return title, main_header, sub_header, paragraph1, paragraph2


def create_webpage(FH):
    title, main_header, sub_header, paragraph1, paragraph2 = webpage_data()
    text=("""<u><center>Welcome to web page.html</center></u>""","""
           <html>
             <head>
                <title>
                """, title, """
                </title>
            </head>
            <body>
                <h1>""", main_header, """</h1>
                <h2>""", sub_header, """</h2>

                <p>""", paragraph1, """
                </p>
                <p>""", paragraph2, """
                </p>
             </body>
            </html>""")
    print(text)
    for i in text:
        FH.write(i)

def main():
    filename=sys.argv[1]
    with open(filename,'w') as FH:
        create_webpage(FH)

if __name__=="__main___":
    main()





