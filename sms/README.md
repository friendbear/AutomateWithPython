## SNS

Twilio
---
* [Create Account](https://twilio.kddi-web.com)
  * Get ACCOUNT SID, AUTH TOKEN
  
```python
from twilio.rest import Client
message = Client(SID,TOKEN).messages.create(body='', from_='', to='')
message.status # deliverd, queued, undeliverd, failed

```
