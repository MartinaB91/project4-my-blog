import pytest
from django.urls import reverse
from tests.tests_utils import TestPostUtils
from blog_post.tests.tests_models import TestCategory
from blog_post.models import Post
from datetime import date
from django.test import TestCase


class BlogPostDetailTestView(TestCase):
    @classmethod
    def setUp(post_class_item):
        """Set up test data for this test class."""
        post = TestPostUtils.get_test_post()
        post_class_item.slug = post.slug

# TODO: Failing test. Try to fix. 
# Tests that my blog list view return expected status code
    @pytest.mark.django_db
    def test_blog_post_view_response(self):
        url = reverse("blog_post", args=[self.slug])
        response = self.client.get(url)
        assert response.status_code == 200
    

