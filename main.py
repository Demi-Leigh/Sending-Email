import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
sender = 'demijefferies@gmail.com'
receiver= 'biancabeedora999@gmail.com'
my_password = input("Enter Your Password Here: ")
s.starttls()
s.login(sender, my_password)
message = "Hey let me know if you've received this email"
s.sendmail(sender, receiver, message)
s.quit()
