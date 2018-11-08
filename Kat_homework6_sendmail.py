import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as s:
    s.starttls()
    s.login('sender_email_address', 'password')
    s.sendmail(from_addr='sender_email_address',
               to_addrs='receiver_email_address',
               msg='Hello! I did it!')



