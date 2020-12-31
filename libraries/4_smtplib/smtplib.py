import smtplib

my_email = "enter ypur email. you want msg to sed from"
password = "your password"



#           class                             object created
with smtplib.SMTP("smtp-mail.outlook.com") as connection:  # <--outlook }service provider  -> hotmail ("smtp.live.com")
                                              # -> yahoo  ("smtp.mail.yahoo.com")

    connection.starttls()    # or making connection secure
    connection.login(user = my_email, password=password)   #for login
    connection.sendmail(from_addr=my_email, to_addrs="kushagratripathi7@gmail.com", msg="Subject: this is the heading\n\n hello0000000")
