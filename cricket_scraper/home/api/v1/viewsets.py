from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .scraper import *
from cricket_scraper.helpers import *



class ScraperViewset(viewsets.ViewSet):
    @action(detail=False , methods=['get'], url_path='blogs')
    def get_blogs(self, request):
        try:
            print("Getting blogs")
            resp = get_t20_wc_blogs()
            return Response({
                "status": True,
                "data": resp
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception is : ", str(e))
            log_entry(
                message=f"Exception from get_blogs {str(e)}"
            )
            return Response({
                "status": False,
                "message": "Something went wrong"
            }, status=status.HTTP_200_OK)