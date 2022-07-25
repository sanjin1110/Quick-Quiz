from django.test import TestCase,SimpleTestCase,Client
from django.urls import resolve,reverse
from student.views import student_dashboard_view,student_signup_view,student_exam_view,view_result_view
from django.contrib.auth.models import User

# Create your tests here.
# class UrlTests(SimpleTestCase):

#     def test_signup_url(self):
#         url = reverse('studentsignup')
#         print(url)
#         self.assertEquals(resolve(url).func, student_signup_view)


#     def test_exam_url(self):
#         url=reverse('student-exam')   
#         print(url)
#         self.assertEquals(resolve(url).func, student_dashboard_view)

#     def test_dashboard_url(self):
#         url=reverse('student-dashboard')
#         print(url)
#         self.assertEquals(resolve(url).func, student_dashboard_view)

#     def test_view_result(self):
#         url = reverse('view-result')
#         print(url)
#         self.assertEquals(resolve(url).func,view_result_view)

class ViewTests(TestCase):

    def test_dashboard(self):
        user=User.objects.create(username='test_user')
        user.set_password('12345')
        user.save()
        client = Client()
        logged_in = client.login(username='test_user',password='12345')

        response = client.get(reverse('student-dashboard'))
        print(response)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response,'student/student_dashboard.html')

    def test_examview(self):
        user=User.objects.create(username='test_user')
        user.set_password('12345')
        user.save()
        client = Client()
        logged_in = client.login(username='test_user',password='12345')

        response=client.get(reverse('student-exam'))
        print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'student/student_exam.html')

    def test_resultview(self):
        user=User.objects.create(username='test_user')
        user.set_password('12345')
        user.save()
        client = Client()
        logged_in = client.login(username='test_user',password='12345')

        response=client.get(reverse('view-result'))
        print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'student/view_result.html')