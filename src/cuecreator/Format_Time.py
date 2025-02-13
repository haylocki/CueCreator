class Format_Time:
    def track_format(self, time_secs: str) -> str:
        minutes = int(time_secs // 60)
        seconds = int(time_secs % 60)
        return f"{minutes:02d}:{seconds:02d}"

    def cue_format(self, seconds: str) -> str:
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes):02d}:{int(seconds):02d}:00"
