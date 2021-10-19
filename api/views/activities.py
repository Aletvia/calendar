from datetime import datetime, timedelta, date
from django.http import JsonResponse
from rest_framework.views import APIView

from ..models import Activity, Property
from ..serializers import SerializedActivity, SerializedCreateActivity, SerializedCreateProperty
from ..services import ServiceActivities

class ActivitiesView(APIView):
    """
        View dedicated to:
            - List activities
            - Create a new activity
            - Update an existing activity
    """
    def get( self, arg1=None, arg2=None ):
        if arg1 and arg2:
            start_date = datetime.strptime(arg1, '%d-%m-%Y %H:%M:%S')
            end_date = datetime.strptime(arg2, '%d-%m-%Y %H:%M:%S')
            ativities = ServiceActivities().activities_list(None,start_date,end_date,None)
        elif arg1 is datetime.date:
            new_schedule= datetime.strptime(arg1, '%d-%m-%Y %H:%M:%S')
            ativities = ServiceActivities().activities_list(None,None,None,new_schedule)
        else:
            ativities = ServiceActivities().activities_list(arg1,None,None,None)
        serializer_ativities = SerializedActivity(ativities, many=True)
        return JsonResponse(serializer_ativities.data, status=200)

    def post( self, request ):
        try:
            serialized_ativity = ServiceActivities().new_activity(request.data)
            if serialized_ativity is not None:
                return JsonResponse(serialized_ativity.data, status=201)
            else:
                return JsonResponse(
                        {'Error':'It is not possible to schedule this activity'},
                        status=400)
        except Exception as e:
            return JsonResponse({'Error':e}, status=400)

    def put( self, id=None, schedule_or_cancel=None ):
        if schedule_or_cancel == 'cancel':
            canceled_activity = ServiceActivities().cancel_activity(id)
            return JsonResponse(
                                {'Canceled':'True',
                                'Activity':canceled_activity.title},
                                status=201)
        else:
            try:
                new_schedule = datetime.strptime(schedule_or_cancel, '%d-%m-%Y %H:%M:%S')
                activity_updated = ServiceActivities().update_activity(id, new_schedule)
                if activity_updated is None:
                    return JsonResponse(
                                    {'Updated':'True',
                                    'Activity':activity_updated.title},
                                    status=201)
                else:
                    return JsonResponse(
                                    {'Error':'It is not possible to schedule this activity'},
                                    status=400)

            except Exception as e:
                return JsonResponse(
                                    {'Error':'It is not possible to schedule this activity'},
                                    status=400)