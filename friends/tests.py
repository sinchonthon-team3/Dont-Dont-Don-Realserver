from rest_framework.test import APIClient, APITestCase

from weights.models import Weight


# Create your tests here.
#
#
# class TestFriends(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.friend_request = {
#             "total_price": 23000,
#             "user": [
#                 [1, 2],
#                 [3, 4],
#                 [5, 6]
#             ]
#         }
#
#         Weight(id=1, weight_name="술찌", is_travel=False, amount=-2).save()
#         Weight(id=2, weight_name="멸치", is_travel=False, amount=-2).save()
#         Weight(id=3, weight_name="술고래", is_travel=False, amount=2).save()
#         Weight(id=4, weight_name="돼지", is_travel=False, amount=2).save()
#         Weight(id=5, weight_name="늦참", is_travel=False, amount=-2).save()
#         Weight(id=6, weight_name="노잼", is_travel=False, amount=1).save()
#
#     def setUp(self):
#         self.client = APIClient()
#
#     def test_get_distribution_view(self):
#         request_url = '/friend/'
#
#         self.client.post(path=request_url, data=self.friend_request)