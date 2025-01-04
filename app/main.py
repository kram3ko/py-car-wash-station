class Car:
    cars_list = []

    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("Comfort class must be between 1 and 7.")
        if not (1 <= clean_mark <= 10):
            raise ValueError("Clean_mark must be between 1 and 10.")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        Car.cars_list.append(self)

    @property
    def show_cars_list(self) -> list:
        return Car.cars_list

    def __repr__(self) -> str:
        return ", ".join(f"{key}={value!r}" for key, value
                         in self.__dict__.items())


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        if not (1 <= distance_from_city_center <= 10):
            raise ValueError("distance_from_city_center")
        if not (1 <= average_rating <= 5):
            raise ValueError("average raiting")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, one_car: Car) -> Car:
        if self.clean_power > one_car.clean_mark:
            one_car.clean_mark = self.clean_power
            return one_car

    def serve_cars(self, car_list: list | Car) -> int:
        income = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                i = (car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center)
                income += round(float(f"{i: .2f}"), 1)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        income = 0
        formula = (car.comfort_class * (self.clean_power - car.clean_mark)
                   * self.average_rating / self.distance_from_city_center)
        income += round(float(f"{formula: .2f}"), 1)
        return income

    def rate_service(self, rate: int) -> float:

        formula = (((self.average_rating * self.count_of_ratings) + rate)
                   / (self.count_of_ratings + 1))
        self.average_rating = round(float(f"{formula}"), 1)
        self.count_of_ratings += 1
        return self.average_rating

    def __repr__(self) -> str:
        return ", ".join(f"{key}={value!r}" for key, value
                         in self.__dict__.items())
