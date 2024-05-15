from abc import *
from typing import Any

"""
빌더
* 어떤 클래스들로 구성되는가?
* 클래스들은 어떤 역할을 하는가?
* 각 요소는 서로 어떻게 연관되는가?

빌더패턴 특이점 -> 공통 인터페이스를 요구하지 않는다.
"""

class Builder(ABC):
    """
    Builder 추상클래스는 Product 객체의 다양한 부분을 생성하기 위한 메서드를 명시한다.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass

class Product1():
    """
    매우 복잡하고 광범위한 구성이 필요한 경우에만 Builder 패턴을 사용하는 것이 좋다.
    다른 생성 패턴과 달리 서로 다른 ConcreteBuilder는 관련 없는 제품을 생성할 수 있다.
    즉, 다양한 빌더의 결과가 항상 동일한 인터페이스를 따르는 것은 아니다.
    """
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")

class ConcreteBuilder1(Builder):
    """
    ConcreteBuilder 클래스는 Builder를 따르며, 빌딩 단계에 대한 구체적인 구현을 제공.
    Builder의 여러 변형이 있을 수 있고, 각각 다르게 구현 될 수 있다.

    새로운 빌더 인스턴스는 추후 조립에 사용되는 비어있는 product 객체를 포함해야 한다.
    일반적으로 최종 결과를 클라이언트에 반환한 후에는 빌더 인스턴스가 다른 제품을 생성할 준비가 되어 있을 것으로 예상된다. 
    그래서 `getProduct` 메서드 본문 끝에서 reset 메서드를 호출하는 것이 일반적인 관행이다.
    필수는 아니며 클라이언트 코드에서 명시적인 reset 호출을 기다리도록 빌더를 만들 수도 있다.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property # getProduct
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product
    
    def produce_part_a(self) -> None:
        return self._product.add("PartA1")
    
    def produce_part_b(self) -> None:
        return self._product.add("PartB1")
    
    def produce_part_c(self) -> None:
        return self._product.add("PartC1")
    
class Director():
    """
    Director는 특정 순서에 따라 빌딩 단계를 실행하는 역할만 한다.
    특정 순서나 구성에 따라 제품을 생산할 때 유용하다.
    엄밀히 말하면 Director 클래스는 선택 사항이며, 클라이언트가 빌더를 직접 제어할 수 있다.
    """
    def __init__(self) -> None:
        self._builder  = None

    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    """
    director는 동일한 빌딩 단계를 통해 여러 product 변형을 구성할 수 있다.
    """
    def builder_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def builder_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")

    director.builder_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")

    director.builder_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()

"""
* Builder 패턴은 복잡한 객체의 생성 과정을 단계별로 분리하여 동일한 생성 절차에서 서로 다른 표현 결과를 만들 수 있게 해준다.
* 빌더 인터페이스(Builder 추상 클래스)는 각 부분을 생성하는 메서드를 정의하고, Concrete Builder는 이를 구현.
* Director는 빌더 객체를 사용하여 제품을 생성하는 과정을 캡슐화. 클라이언트는 Director에게 원하는 빌더를 전달하고, Director는 해당 빌더를 사용하여 product를 생성.

빌더 패턴의 강점
* 생성 코드와 표현 방식을 분리할 수 있어 코드의 유지보수성과 확장성이 향상.
* 객체 생성 과정을 세밀하게 제어할 수 있으므로, 객체 생성 시 필요한 초기화 작업이나 유효성 검사 등을 수행 가능.
"""
