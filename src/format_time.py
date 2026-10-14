class Format_Time:
    def track_format(self, time_secs: str) -> str:
        minutes, seconds, _ = self.format_time(time_secs)
        return f"{minutes:02d}:{seconds:02d}"

    def cue_format(self, time_secs: str) -> str:
        minutes, seconds, frames = self.format_time(time_secs)
        return f"{minutes:02d}:{seconds:02d}:{frames:02d}"

    def format_time(self, time_secs: str) -> tuple[int, int, int]:
        total_frames = round(float(time_secs) * 75)
        minutes, remaining_frames = divmod(total_frames, 60 * 75)
        seconds, frames = divmod(remaining_frames, 75)

        return minutes, seconds, frames
