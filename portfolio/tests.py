from django.test import TestCase
from portfolio.models import Blog,Category,Skill,Project,News
from django.contrib.auth.models import User


class PortfolioTestCase(TestCase):
    def setUp(self):
    	# create cat 
        cat1 = Category.objects.create(title="test cat",description="test")
        cat2 = Category.objects.create(title="test lion",description="test")
        # project and skills
        skill1 = Skill.objects.create(title="android",related_projects="cat",term="2 years")
        skill2 = Skill.objects.create(title="ios",related_projects="catios",term="1 years")
        u = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        u.is_staff = True
        u.save()
        project1 = Project.objects.create(title="title lion", description="roar",github_link="http://github.com", android="http://google.com", ios="google.com",web="apple.com",writer=u)
        project1.skills.add(skill1)
        project1.skills.add(skill2)
        project2 = Project.objects.create(title="tiger", description="roar",writer=u)
        project2.skills.add(skill2)

        # blog
        post1 = Blog.objects.create(post_title="apple",post_content="mango")


    def test_project_has_title(self):
        p1 = Project.objects.get(title="title lion")
        p2 = Project.objects.get(title="tiger")
        s1 = p1.skills.all()[0]
        s2 = p1.skills.all()[1]
        self.assertEqual(p1.title, 'title lion')
        self.assertEqual(s1.title, "android")
        self.assertEqual(s2.title, "ios")
        self.assertEqual(p2.title, "tiger")
        self.assertEqual(p2.writer.username,"john")

    def test_blog_has_field(self):
    	post1 = Blog.objects.get(post_title="apple")
    	# cat1 = post1.category.all()[0]

    	self.assertEqual(post1.post_title, "apple")
    	self.assertEqual(post1.post_content,"mango")
    	# self.assertEqual(cat1.title,"test cat")



