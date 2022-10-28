from guizero import App, Text, TextBox, Box, PushButton
app = App(title="Log in", height=250, width=400)
open_message = Text(app, text="Welcome!", size=40, )
user_id = Text(app, text="User ID: ",align="left", grid=[3,3])
id_box = TextBox(app,text="Please enter your ID number", width=25, align="left", grid=[3,4])
app.display()
