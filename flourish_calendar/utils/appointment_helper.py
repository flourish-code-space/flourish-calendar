
from ..models import AppointmentStatus

class AppointmentHelper:
    
    @staticmethod
    def change_color(subject_identifier, visit_code, color):
        
        if subject_identifier and visit_code and color:
            
            try:
                
                appt = AppointmentStatus.objects.get(
                    subject_identifier=subject_identifier,
                    visit_code = visit_code,
                )
                
            except AppointmentStatus.DoesNotExist:
                
                AppointmentStatus.objects.create(
                    subject_identifier=subject_identifier,
                    visit_code = visit_code,
                    color = color
                )
                
            else:
                appt.color = color
                appt.save()