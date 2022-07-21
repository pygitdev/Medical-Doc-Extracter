import re
from backend.src.parser_generic import MedicalDocParser


class PrescriptionParser(MedicalDocParser):
    def __int__(self, text):
        MedicalDocParser.__init__(text)
        self.text = text

    def parser(self):
        """
        :return: it returns the all parser of prescription
        """
        return {"patient_name": self.get_field('patient_name'),
                "patient_address": self.get_field('patient_address'),
                "medicines": self.get_field('medicines'),
                "directions": self.get_field('directions'),
                "refill": self.get_field('refill')
                }

    def get_field(self, field_name):
        """
        :return: extract the required field text by field_name
        """

        pattern_dict = {"patient_name": {'pattern': 'Name:(.*)Date:', 'flag': 0},
                        "patient_address": {'pattern': 'Address:(.*)\n', 'flag': 0},
                        "medicines": {'pattern': 'Address[^\n]*(.*)Directions', 'flag': re.DOTALL},
                        "directions": {'pattern': 'Directions:(.*)Refill:', 'flag': re.DOTALL},
                        "refill": {'pattern': 'Refill:(.*)', 'flag': 0}
                        }
        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'],
                                 self.text,
                                 flags=pattern_object['flag'])
            if len(matches) > 0:
                return matches[0].strip()
