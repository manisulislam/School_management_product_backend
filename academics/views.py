from rest_framework import viewsets
from .models import (
    ClassRoom, Subject, Attendance,
    Exam, Result, Announcement, Timetable, Event
)
from .serializers import (
    ClassRoomSerializer, SubjectSerializer, AttendanceSerializer,
    ExamSerializer, ResultSerializer, AnnouncementSerializer,
    TimetableSerializer, EventSerializer
)

# ------------------ CLASSROOM ------------------
class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer


# ------------------ SUBJECT ------------------
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# ------------------ ATTENDANCE ------------------
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


# ------------------ EXAM ------------------
class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


# ------------------ RESULT ------------------
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


# ------------------ ANNOUNCEMENT ------------------
class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


# ------------------ TIMETABLE ------------------
class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


# ------------------ EVENT ------------------
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
