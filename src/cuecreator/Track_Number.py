import mutagen


class Track_Number:
    def format(self, track_num: str) -> str:
        track_num_parts = track_num.split("/")
        return int(track_num_parts[0])

    def get(self, file_path: str) -> int:
        return int(
            mutagen.File(file_path, easy=True)
            .get("tracknumber", ["0/1"])[0]
            .split("/")[0]
        )
