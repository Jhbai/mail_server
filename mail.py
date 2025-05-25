import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class Mail:
    def __init__(self, sender: str):
        self.sender = sender

    def select_post_office(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def write_receiver(self, receiver: list, receiver_cc: list = None):
        self.receiver = receiver
        self.receiver_cc = receiver_cc

    def write_content(self, subject: str, body: str, image: io.BytesIO = None):
        # 創建 MIMEMultipart 對象
        message = MIMEMultipart('related')

        # 設置郵件的發件人、收件人
        message['From'] = ", ".join(self.sender)
        message['To'] = ", ".join(self.receiver)
        if self.receiver_cc:
            message['Cc'] = self.receiver_cc

        # 設置郵件的主題
        message['Subject'] = subject

        # 設置郵件的內容、編碼格式 
        message.attach(MIMEText(body, "html", 'utf-8'))

        # 
        if image is not None:
            # 將圖片轉換為 MIMEImage 對象
            image = MIMEImage(image.read(), _subtype='png')
            image.add_header('Content-ID', '<image>')
            image.add_header('Content-Disposition', 'inline', filename='image.jpg')
            message.attach(image)

        self.message = message

    def send_mail(self, passward: str = None):
        # 使用 SMTP 協議發送郵件
        try:
            with smtplib.SMTP(self.ip, self.port) as server:
                server.starttls()
                if passward:
                    server.login(self.sender, passward)
                server.sendmail(self.sender, self.receiver, self.message.as_string())
                server.quit()
                print("郵件發送成功")
        except Exception as e:
            print(f"郵件發送失敗: {e}")


