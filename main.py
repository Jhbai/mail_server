import matplotlib.pyplot as plt
from mail import Mail
import numpy as np
from io import BytesIO

# 1. 產生matplotlib圖
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, label="sin(x)")
ax.legend()
buf = BytesIO()
plt.savefig(buf, format='png')
plt.close()
buf.seek(0)

# 2. 郵件內容
html_body = """
<h2>這是你的 Gmail 測試郵件</h2>
<p>下方是即時產生的數學圖表：</p>
<img src="cid:image">
"""

# 3. 請填入你的 Gmail 資訊
sender = "src@gmail.com" # 源gmail
sender_password = "code here"  # 不是一般密碼！gmail是應用密碼
receiver = ["trg@gmail.com"]  # 目標gmail

mail = Mail(sender=sender)
mail.select_post_office(ip="smtp.gmail.com", port=587)
mail.write_receiver(receiver=receiver)
mail.write_content(subject="Gmail 圖片測試", body=html_body, image=buf)
mail.send_mail(passward=sender_password)
