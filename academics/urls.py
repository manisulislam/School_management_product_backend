from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClassRoomViewSet, SubjectViewSet, AttendanceViewSet,
    ExamViewSet, ResultViewSet, AnnouncementViewSet,
    TimetableViewSet, EventViewSet
)

router = DefaultRouter()
router.register(r'classrooms', ClassRoomViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'results', ResultViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'timetables', TimetableViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
