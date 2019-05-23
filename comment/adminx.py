import xadmin
from .models import Comment
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side, Field
class CommentAdmin(object):

    list_display=['user','status','content','create_time','target']
    search_fields=['user','status','create_time','target']
    list_filter=['user','status','create_time','target']
    form_layout=(
        Main(
            Fieldset('信息',
                     Row('user', 'status')
                     ),
            Fieldset(
                '评论内容',
                'content',
            ),
        )

    )

xadmin.site.register(Comment,CommentAdmin)