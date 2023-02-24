from datetime import datetime, timedelta, timezone


class NotificationActivities:
    def run():
        now = datetime.now(timezone.utc).astimezone()
        results = [{
            'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'handle':  'Smiley',
            'message': 'What a beatiful day?',
            'created_at': (now - timedelta(days=2)).isoformat(),
            'expires_at': (now + timedelta(days=5)).isoformat(),
            'likes_count': 5,
            'replies_count': 1,
            'reposts_count': 0,
            'replies': [{
                'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                'handle':  'Sunny',
                'message': 'Do you think it has something to do with me?',
                'likes_count': 0,
                'replies_count': 0,
                'reposts_count': 0,
                'created_at': (now - timedelta(days=2)).isoformat()
            }],
        },
            {
            'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
            'handle':  'Doggy',
            'message': 'Wolf wolf',
            'created_at': (now - timedelta(days=7)).isoformat(),
            'expires_at': (now + timedelta(days=9)).isoformat(),
            'likes': 0,
            'replies': []
        },
            {
            'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
            'handle':  'Sleeping Bear',
            'message': 'ZZZzzzzzzz.....',
            'created_at': (now - timedelta(hours=1)).isoformat(),
            'expires_at': (now + timedelta(hours=12)).isoformat(),
            'likes': 0,
            'replies': []
        }]
        return results
