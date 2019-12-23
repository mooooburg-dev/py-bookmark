from django.db import models

# models.Model을 상속받는 Bookmark 클래스
# 모델 안에는 두 개의 클래스 변수가 있음. 이것을 필드라고 부름.
# Site_name과  url이라는 두 개의 필드를 만드는데 데이터베이스에 이 두가지의 정보를 저장하기 위함임.
# 이 정보가 기록되는 테이블의 이름이 bookmark.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # __str__ 메서드는 항상 문자열을 반환해야 함.
    # 어떤 연산을 수행해도 상관없지만 반환하는 값은 항상 문자열이 되도록.
    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url