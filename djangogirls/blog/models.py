from django.db import models
from django.utils import timezone

class Post(models.Model):
    #author is connected with auth.User model, 
    #auth.User is model's name which is automatically generated for admin account.
    #createsuperuser stores the generated account  which is generated command and etc.
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #제목을 나타내는 부분,There is a word limitation in CharField. maximum word length is 200.
    title=models.CharField(max_length=200)
    #본문을 나타내는 부분, there is no word limitation in Textfield.
    text = models.TextField()
    #when the text is written. Timezone is using django.utils.
    #글 최초 작성시간을 나타내는 부분, default는 미입력시 자동기입할 자료
    created_date=models.DateTimeField(default=timezone.now)
    #최종수정시간을 나타내는 부분.
    #blank는 공백으로 둬도 되는지, null은 입력을 안해도 되는지를 나타냄.
    published_date = models.DateTimeField(blank=True, null=True)
    
    #글을 수저할 때 실행할 함수. 사용자가 날짜를 기입하는게 아니라
    #수정시 매번 호출되어 최종 수정시각을 갱신한다.
    def publish(self):
        #published_date의 값만 수정 당시의 현재 시간으로 바꾸기
        self.published_date = timezone.now()
        #바꾼 시간은 저장까지 해 줘야 DB에 반영됨
        self.save()
    #if you are searching a Post model related context in admin page, the title appears
    def __str__(self):
        return self.title
    
# Create your models here.
