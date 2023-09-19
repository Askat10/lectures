import smtplib
class EmailSender:
    __sender = smtplib.SMTP('smtp.gmail.com', 587)
    __host_email = 'amanturovaskatshakirovich@gmail.com'
    def send_mail(self, email):
        self.__sender.starttls()
        self.__sender.login(self.__host_email, 'wutfobclpebsirpz',)
        self.__sender.sendmail(self.__host_email, email, 'sha poreshaem nahui', 'yopta')
        self.__sender.quit()

# email_sender = EmailSender()
# email_sender.send_mail('amanturovaskatshakirovich@gmail.com')