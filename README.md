# Django quick contact form

A simple contact form that can save the messages to the db.

   ```bash
   pip install django-qcf
   ```

Add `'qcf',` to installed apps, migrate

Set urls:

   ```python
   url(r'^contact/', include('qcf.urls')),
   ```

## Settings

```python
   SAVE_TO_DB = True

   RECIPIENTS_LIST = [settings.DEFAULT_FROM_EMAIL] # set your list of recipients in this setting

   EMAIL_SENT_MESSAGE = _(u'Your message has been sent')
   ```

## Templates

To use the bootstrap templates install `django-bootstrap-form` and in settings:

   ```python
   QCF_TEMPLATES = "bootstrap"
   ```