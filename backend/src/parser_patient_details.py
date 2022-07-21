import re
from backend.src.parser_generic import MedicalDocParser


def remove_noise_from_text(field_name, text):
    if field_name == 'patient_name':
        text = text.replace("Birth Date", "")
        month = re.findall('((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)', text)[0]
        return text.replace(month[0], " ").strip()
    elif field_name == 'patient_phone_no':
        return text[1]
    elif field_name == 'medical_problems':
        return text[0].strip()
    else:
        return text.strip()


class PatientDetailsParser(MedicalDocParser):
    def __int__(self, text):
        # MedicalDocParser.__init__(text)
        self.text = text

    def parser(self):
        """
        :return: it returns the all parser of prescription
        """
        return {"patient_name": self.get_field('patient_name'),
                "patient_phone_no": self.get_field('patient_phone_no'),
                "medical_problems": self.get_field('medical_problems'),
                "vaccination": self.get_field('vaccination'),
                }

    def get_field(self, field_name):
        """
        :return: extract the required field text by field_name
        """

        pattern_dict = {
            "patient_name": {'pattern': 'Patient Information(.*?)\(\d{3}\)', 'flag': re.DOTALL},
            "patient_phone_no": {'pattern': 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})', 'flag': re.DOTALL},
            "medical_problems": {'pattern': 'List any Medical Problems .*?:((.*)|N\/A)', 'flag': re.DOTALL},
            "vaccination": {'pattern': 'Have you had the Hepatitis B vaccination\?.*(Yes|No|yes|no)', 'flag': re.DOTALL}
        }
        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'],
                                 self.text,
                                 flags=pattern_object['flag'])
            if len(matches) > 0:
                output = remove_noise_from_text(field_name, matches[0])
                return output


