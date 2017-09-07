import smtplib
from email.mime.text import MIMEText
user = '1916059613@qq.com'
to = '1916059613@qq.com'
invite_code = 'olcudzrffgvocead'
s=smtplib.SMTP_SSL('smtp.qq.com', 465)
s.login(user, invite_code)
msg = MIMEText("Test")
msg["Subject"] = "test"
msg["From"] = user
msg["to"] = to
s.sendmail(user, to, msg.as_string())
s.quit()
print "success"

-------------------------------------------------------------------------------

/home/whf/.viminfo: Access denied
/home/whf/.gksu.lock: Empty file
/home/whf/.scapy_history: Access denied

----------- SCAN SUMMARY -----------
Known viruses: 6300327
Engine version: 0.99.2
Scanned directories: 1
Scanned files: 67
Infected files: 0
Total errors: 2
Data scanned: 2.34 MB
Data read: 237.47 MB (ratio 0.01:1)
Time: 9.967 sec (0 m 9 s)
