## SMTP

smtp
---
```python
import smtplib
smtp_obj = smtplib.SMTP('smtp.example.com', 587)
smtp_obj = smtp_obj.ehlo()

try:
    smtp_obj = smtp_obj.login('bob@example.com', 'MY_SECRET_PASSWORD')
except smtplib.SMTPAuthenticationError: 
    None


smtp_obj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtp_obj.quit()
```

* Japanese
```python
from email.mime.text import MIMEText
from email.header import Header

charset = 'iso-2022-jp'

msg = MIMEText('nihongo', 'plain', charset)
msg['Subject'] = Header('kenmei'.decode(charset), charset)

semdmail(..., msg.as_string())

```
* TLS
  * smtp_obj.starttls()

imap
---

```bash
$ pip3 install imapclient, pyzmail
```

```python
import imapclient
from backports import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

imap_obj = imapclient.IMAPClient('imap.example.com', ssl=True, ssl_context=context)
imap_obj.login('my_email@example.com', 'MY_SECRET_PASSWORD')

imap_obj.select_folder('INBOX', readonly=True)

# IMAP Search keys
UIDs = imap_obj.search(['SINCE', '01-May-2019'])

raw_messages = imap_obj.fetch([UIDs[0], ['BODY[]', 'FLAGS']])

import pyzmail
message = pyzmail.PyzMessage.factory(raw_messages[UIDs[0]][b'BODY[]'])
message.get_subject()

message.get_addresses('from') # => [(Name, addr),...]
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')

message.text_part != None

message.text_part.get_payload().decode(message.text_part.charset)
message.html_part.get_payload().decode(message.html_part.charset)

```
