from powerline.segments import Segment
from powerline.theme import requires_segment_info
from datetime import date


@requires_segment_info
class DDaySegment(Segment):

    def __call__(
            self,
            pl,
            segment_info,
            year,
            month,
            day,
            fmt='D-{days}'):
        today = date.today()
        dest_day = date(year, month, day)
        delta = (dest_day - today)
        return fmt.format(days=delta)
