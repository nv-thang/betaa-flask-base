from bson import ObjectId

class Movie:
    def __init__(self, title, description, duration, genres, poster_url, show_times):
        self._id = ObjectId()
        self.title = title
        self.description = description
        self.duration = duration
        self.genres = genres
        self.poster_url = poster_url
        self.show_times = show_times

    def to_dict(self):
        return {
            "_id": str(self._id),
            "title": self.title,
            "description": self.description,
            "duration": self.duration,
            "genres": self.genres,
            "poster_url": self.poster_url,
            "show_times": self.show_times
        }
