# Django quick contact form

A simple contact form that can save the messages to the db.

   ```bash
   pip install django-qcf
   ```

Add `'qcf',` to installed apps, migrate

Default settings: 

- SAVE_TO_DB = True

- RECIPIENTS_LIST = [settings.DEFAULT_FROM_EMAIL] # set your list of recipients in this setting

- EMAIL_SENT_MESSAGE = _(u'Your message has been sent')