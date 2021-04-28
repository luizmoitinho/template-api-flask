import abc

class IServoService(abc.ABC):

    @abc.abstractmethod
    def rotate(self, pan = 90, tilt = 90):
        pass
    
    @abc.abstractmethod
    def centralize_target(self, rect, dimensions_capture ):
        pass
    
    @abc.abstractmethod
    def time_trasition_servo(self, time):
        pass
    

