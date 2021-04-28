import abc

class IHealthCheckService(abc.ABC):
    
    @abc.abstractmethod
    def test_connection(self):
        pass
    
    @abc.abstractmethod
    def test_servo(self):
        pass


