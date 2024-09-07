from enum import Enum


class Transcriptions(Enum):
    load = "load_transcriptions"
    view = "my_transcriptions"
    page = "page:"
    item = "item:"
    back = "back"
    build_proto = "build_protocol"
    build_assignments = "build_assignments"