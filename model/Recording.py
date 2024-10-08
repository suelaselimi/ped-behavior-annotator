from dataclasses import dataclass, field
import enum
from typing import *
import json

from model.MultiFrameAnnotation import MultiFrameAnnotation
from model.SingleFrameAnnotation import SingleFrameAnnotation

@dataclass
class Recording:
    name: str
    fps: float
    annotation_path: str # ./annotations/recording0001.json
    video_path: str # https://www.youtube.com/watch?v=kljhas3
    
    multiFrameAnnotations: Set[MultiFrameAnnotation] = field(default_factory = set)
    singleFrameAnnotations: Set[SingleFrameAnnotation] = field(default_factory = set)

    def toJSON(self) -> str:
        """A valid JSON representation of the object
        Returns:
            str: _description_
        """
        raise Exception("Use the EnumEncoder to convert the object to JSON")
        # return (
        # "{" + \
        # f'"name": "{self.name}",' + \
        # f'"fps": "{self.fps}",' + \
        # f'"annotation_path": "{self.annotation_path}",' + \
        # f'"video_path": "{self.video_path}",' + \
        # f'"multiFrameAnnotations": "{self.multiFrameAnnotations}",' + \
        # f'"singleFrameAnnotation":"{self.singleFrameAnnotation}"' + \
        # "}")

    def fromJSON(self, json: str) -> 'Recording':
        # read the json string and convert it to a Recording object
        return None


    
# def _sanitizeForJson(o):
#     if isinstance(o, dict):
#         return {_sanitizeForJson(k): _sanitizeForJson(v) for k, v in o.items()}
#     elif isinstance(o, (set, tuple, list)):
#         return type(o)(_sanitizeForJson(x) for x in o)
#     elif isinstance(o, enum.Enum):
#         return o.value
#     return o