from abc import *

"""
추상 팩토리
"""

# ABCMeta, ABC 차이?
class AbstractProductA(ABC):
    """
    product 패밀리의 각 고유한 product는 기본 인터페이스를 가져야 한다. product의 모든 변형은 이 인터페이스를 구현해야 한다.
    """
    @abstractmethod
    def useful_funtion_a(self) -> str:
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def useful_funtion_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_funtion_b(self, collaborator: AbstractProductA) -> None:
        pass

class AbstractFactory(ABC):
    """
    추상 팩토리 인터페이스는 서로 다른 추상 product를 반환하는 일련의 메서드를 선언한다. 
    이 product들은 패밀리라고 불리며 상위 수준의 테마나 개념과 관련이 있다. 
    한 패밀리의 product들은 보통 서로 협력할 수 있다. 
    product 패밀리는 여러 변형을 가질 수 있지만, 한 변형의 제품은 다른 변형의 제품과 호환되지 않는다.

    * 집합(패밀리)을 생성하는 인터페이스를 제공하되, 구체적인 클래스는 지정하지 않는 디자인 패턴
    * 동일한 테마나 개념을 가진 객체
    * 서로 다른 변형의 객체들은 호환되지 않음
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    """
    구체적인 팩토리는 단일 변형에 속하는 제품 패밀리를 생성한다. 
    팩토리는 결과물이 호환됨을 보장한다. 
    구체적인 팩토리 메서드의 시그니처는 추상 product를 반환하지만, 메서드 내부에서는 구체적인 product가 인스턴스화 된다.

    구체적인 팩토리 클래스(ConcreteFactory1, ConcreteFactory2)는 추상 팩토리 인터페이스를 구현하며, 실제로 객체를 생성하는 역할을 한다. 
    각 구체적인 팩토리는 특정 변형의 제품 패밀리를 생성하며, 해당 변형 내에서는 product들이 서로 호환된다.
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()
    
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

"""
구체적인 product는 해당하는 구체적인 팩토리(ConcreteFactory)에 의해 생성된다.
"""
class ConcreteProductA1(AbstractProductA):
    def useful_funtion_a(self) -> str:
        return "The result of the product A1."
    
class ConcreteProductA2(AbstractProductA):
    def useful_funtion_a(self) -> str:
        return "The result of the product A2."
    
class ConcreteProductB1(AbstractProductB):
    def useful_funtion_b(self) -> str:
        return "The result of the product B1."
    
    def another_useful_funtion_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_funtion_a()
        return f"The result of the collaborating with the ({result})"
    
class ConcreteProductB2(AbstractProductB):
    def useful_funtion_b(self) -> str:
        return "The result of the product B2."
    
    def another_useful_funtion_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_funtion_a()
        return f"The result of the collaborating with the ({result})"
    
def client_code(factory: AbstractFactory) -> None:
    """
    클라이언트 코드는 추상 타입(AbstractFactory와 AbstractProduct)을 통해서만 팩토리와 제품을 다룬다. 
    이를 통해 클라이언트 코드를 깨뜨리지 않고도 모든 팩토리나 제품 하위 클래스를 클라이언트 코드에 전달할 수 있다.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_funtion_b()}")
    print(f"{product_b.another_useful_funtion_b(product_a)}", end="")

if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())

"""
추상 팩토리 패턴은 관련된 객체들의 생성을 캡슐화하고, 객체 생성의 구체적인 내용을 클라이언트 코드에서 분리하는 데 도움을 준다. 
이를 통해 코드의 의존성을 줄이고, 새로운 변형의 제품 패밀리를 쉽게 추가할 수 있게 된다.
"""
