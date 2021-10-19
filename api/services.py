from datetime import datetime, timedelta, date
import json

from django.db.models.fields import NullBooleanField

from api.serializers import SerializedActivity, SerializedCreateActivity, SerializedCreateActivity, SerializedCreateProperty
from .models import Property, Activity


class ActivityData:
    id: id
    schedule: date
    title: str
    created_at: date
    status: str
    condition: str
    property: json
    survey: str


class ServiceActivities:
    def new_activity(self, info):
        property_id = int(info['property'])
        schedule = info['schedule']
        property = Property.objects.filter(id=property_id)
        for prop in property:
            info['property']= property_id
            serialized_property = SerializedCreateProperty(prop, many = False)
        if serialized_property['disabled_at'].value is None or serialized_property['disabled_at'].value is not None and serialized_property['disabled_at'].value <= date.today():
            if self._activities_same_hour(schedule, property_id):
                serialized_ativity = SerializedCreateActivity(data = info)
                serialized_ativity.is_valid()
                serialized_ativity.save()
                return serialized_ativity
            else:
                return None
        else:
            return None

    @staticmethod
    def _activities_same_hour(schedule, property_id):
        schedule = datetime.strptime(schedule, '%Y-%m-%d %H:%M:%S')
        schedule_and_hour = schedule + timedelta(hours=1)
        activity_same_time = Activity.objects.filter(property=property_id,status='active'
                                                    ).exclude(schedule__lt=schedule
                                                    ).exclude(schedule__gt=schedule_and_hour
                                                    )
        if activity_same_time.exists():
            return False
        else:
            return True

    def activities_list(self, status=None, start_date=None, end_date=None, average_date=None):
        if status:
            return self._complete_list(Activity.objects.filter(status=status))
        elif start_date:
            return self._get_list_between_dates(start_date, end_date)
        elif average_date:
            start_date = average_date - timedelta(days=3)
            end_date = average_date + timedelta(days=14)
            return self._get_list_between_dates(start_date, end_date)
        else:
            return Activity.objects.all()

    @staticmethod
    def _get_list_between_dates(self, start_date=None, end_date=None):
        return self._complete_list(Activity.objects.exclude(schedule__gte=end_date
                                                            ).filter(schedule__gte=start_date))

    @staticmethod
    def _complete_list(activities_list):
        final_list = []
        condition = ''
        for activity in activities_list:
            if activity.status == 'active':
                if date.today() >= activity.schedule:
                    condition = 'Pendiente a realizar'
                else:
                    condition = 'Atrasada'
            elif activity.status == 'done':
                condition = 'Finalizada'
            elif activity.status == 'cancel':
                condition = 'Cancelada'
            property = Property.objects.get(id=activity.property)
            final_list.append(ActivityData(
                id=activity.id,
                schedule=activity.schedule,
                title=activity.title,
                created_at=activity.created_at,
                status=activity.status,
                condition=condition,
                property=property,
                survey='http://127.0.0.1:8000/api/v1/survey/'
            ))
        return final_list

    def update_activity(self, id, new_schedule):
        schedule_activity, activity = Activity.objects.get(id=id)
        its_possible = self._activities_same_hour(new_schedule, activity.property)
        if its_possible:
            schedule_activity.schedule = new_schedule
            return SerializedActivity(activity, schedule_activity)
        else:
            return None

    def cancel_activity(self, id):
        cancel_activity, activity = Activity.objects.get(id=id)
        cancel_activity.status = 'cancel'
        return SerializedActivity(activity, cancel_activity)