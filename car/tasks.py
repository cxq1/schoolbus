from __future__ import absolute_import

from celery.task import task
from django.core.mail import EmailMessage



@task(bind=True,max_retries=3,default_retry_delay=10)
def send_email_by_celery(self,subject, html_content, send_from, to_list, fail_silently=False):
    try:
        msg = EmailMessage(subject, html_content, send_from, to_list)
        msg.content_subtype = "html"
        msg.send(fail_silently)
    except Exception as e:
        raise self.retry(exc=e)