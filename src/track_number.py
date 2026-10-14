from mutagen import File  # pyright: ignore[reportPrivateImportUsage]


class Track_Number:
    def format(self, track_num: str) -> int:
        track_num_parts = track_num.split("/")
        return int(track_num_parts[0])

    def get(self, file_path: str) -> int:
        audio_file = File(file_path, easy=True)

        if audio_file is None:
            return 0

        return int(audio_file.get("tracknumber", ["0/1"])[0].split("/")[0])
