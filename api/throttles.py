from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class SongCreateRateThrottle(UserRateThrottle):
    rate = '5/hour'  # Limit to 5 song creations per hour

class SongListRateThrottle(AnonRateThrottle):
    rate = '20/minute'  # Limit to 20 list requests per minute for anonymous users

class SingerCreateRateThrottle(AnonRateThrottle):
    rate = '3/hour'  # Limit to 3 singer registrations per hour 