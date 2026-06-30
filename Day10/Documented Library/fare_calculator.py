"""
Transport Fare Calculator

A simple command-line application to calculate transport fares,
estimate travel time, apply discounts, and generate trip summaries.


"""

# python -m doctest -v fare_calculator.py

class TransportCalculator:
    """
    A utility class for fare calculation and trip-related operations.
    """

    # Fare charged per kilometer for each vehicle
    FARE_RATES = {
        "car": 20.0,
        "bike": 10.0,
        "auto": 15.0,
    }

    # Minimum fare for each vehicle
    BASE_FARES = {
        "car": 50.0,
        "bike": 25.0,
        "auto": 30.0,
    }

    # Average speed (km/hr)
    AVERAGE_SPEED = {
        "car": 40.0,
        "bike": 35.0,
        "auto": 25.0,
    }

    def __init__(self):
        """
        Initialize the Transport Calculator.

        Raises:
            None

        Example:
            >>> calc = TransportCalculator()
            >>> isinstance(calc, TransportCalculator)
            True
        """


    def calculate_fare(self, distance: float, vehicle: str) -> float:
        """
        Calculate fare based on distance and vehicle.

        Args:
            distance (float): Distance travelled.
            vehicle (str): Vehicle type.

        Returns:
            float: Total fare.

        Raises:
            ValueError: If vehicle is not one of "car", "bike", or "auto".
            ValueError: If distance is zero or negative.

        Example:
            >>> calc = TransportCalculator()
            >>> calc.calculate_fare(10.0, "car")
            250.0
            >>> calc.calculate_fare(5.0, "bike")
            75.0
            >>> calc.calculate_fare(8.0, "auto")
            150.0
            >>> calc.calculate_fare(0.0, "auto")
            Traceback (most recent call last):
                ...
            ValueError: Distance must be greater than 0.
            >>> calc.calculate_fare(8.0, "helicopter")
            Traceback (most recent call last):
                ...
            ValueError: Invalid vehicle. Choose from car, bike, auto.
        """

        vehicle = vehicle.lower()

        if vehicle not in self.FARE_RATES:
            supported = ", ".join(self.FARE_RATES.keys())
            raise ValueError(
                f"Invalid vehicle. Choose from {supported}."
            )

        if distance <= 0:
            raise ValueError(
                "Distance must be greater than 0."
            )

        fare = (
            self.BASE_FARES[vehicle]
            + self.FARE_RATES[vehicle] * distance
        )

        return round(fare, 2)


    def estimate_eta(self, distance: float, vehicle: str) -> float:
        """
        Estimate travel time.

        Args:
            distance (float): Distance travelled.
            vehicle (str): Vehicle type.

        Returns:
            float: ETA in minutes.

        Raises:
            ValueError: If vehicle is not one of "car", "bike", or "auto".
            ValueError: If distance is zero or negative.

        Example:
            >>> calc = TransportCalculator()
            >>> calc.estimate_eta(20.0, "car")
            30.0
            >>> calc.estimate_eta(10.0, "bike")
            17.1
            >>> calc.estimate_eta(5.0, "auto")
            12.0
            >>> calc.estimate_eta(-5.0, "auto")
            Traceback (most recent call last):
                ...
            ValueError: Distance must be greater than 0.
            >>> calc.estimate_eta(10.0, "bus")
            Traceback (most recent call last):
                ...
            ValueError: Invalid vehicle. Choose from car, bike, auto.
        """

        vehicle = vehicle.lower()

        if vehicle not in self.AVERAGE_SPEED:
            supported = ", ".join(self.AVERAGE_SPEED.keys())
            raise ValueError(
                f"Invalid vehicle. Choose from {supported}."
            )

        if distance <= 0:
            raise ValueError(
                "Distance must be greater than 0."
            )

        hours = distance / self.AVERAGE_SPEED[vehicle]

        minutes = hours * 60

        return round(minutes, 1)



    def apply_discount(self, fare: float, discount: float) -> float:
        """
        Apply a percentage discount to the fare.

        Args:
            fare (float): Original fare.
            discount (float): Discount percentage.

        Returns:
            float: Discounted fare.

        Raises:
            ValueError: If fare is negative.
            ValueError: If discount is outside the range 0-100.

        Example:
            >>> calc = TransportCalculator()
            >>> calc.apply_discount(250.0, 10.0)
            225.0
            >>> calc.apply_discount(100.0, 0.0)
            100.0
            >>> calc.apply_discount(-50.0, 10.0)
            Traceback (most recent call last):
                ...
            ValueError: Fare cannot be negative.
            >>> calc.apply_discount(100.0, 150.0)
            Traceback (most recent call last):
                ...
            ValueError: Discount should be between 0 and 100.
        """

        if fare < 0:
            raise ValueError("Fare cannot be negative.")

        if not 0 <= discount <= 100:
            raise ValueError(
                "Discount should be between 0 and 100."
            )

        discounted_fare = fare * (1 - discount / 100)

        return round(discounted_fare, 2)

    # Trip Summary


    def trip_summary(
        self,
        distance: float,
        vehicle: str,
        discount: float = 0.0
    ) -> dict:
        """
        Generate a trip summary.

        Args:
            distance (float): Distance travelled.
            vehicle (str): Vehicle type.
            discount (float): Discount percentage.

        Returns:
            dict: Trip details.

        Raises:
            ValueError: Propagated from calculate_fare or estimate_eta if
                distance or vehicle are invalid.
            ValueError: Propagated from apply_discount if discount is
                outside the range 0-100.

        Example:
            >>> calc = TransportCalculator()
            >>> summary = calc.trip_summary(10.0, "auto", discount=10.0)
            >>> summary["vehicle"]
            'auto'
            >>> summary["final_fare"]
            162.0
            >>> summary["eta"]
            24.0
        """

        vehicle = vehicle.lower()

        fare = self.calculate_fare(distance, vehicle)

        eta = self.estimate_eta(distance, vehicle)

        final_fare = self.apply_discount(fare, discount)

        return {
            "vehicle": vehicle,
            "distance": distance,
            "fare": fare,
            "discount": discount,
            "final_fare": final_fare,
            "eta": eta,
        }

    # Surge Pricing

    def surge_multiplier(
        self,
        hour: int,
        day_type: str = "weekday"
    ) -> float:
        """
        Calculate the surge multiplier.

        Args:
            hour (int): Current hour (0-23).
            day_type (str): weekday or weekend.

        Returns:
            float: Surge multiplier.

        Raises:
            ValueError: If hour is outside the range 0-23.
            ValueError: If day_type is not "weekday" or "weekend".

        Example:
            >>> calc = TransportCalculator()
            >>> calc.surge_multiplier(9, "weekday")
            1.5
            >>> calc.surge_multiplier(14, "weekday")
            1.0
            >>> calc.surge_multiplier(18, "weekend")
            1.3
            >>> calc.surge_multiplier(25)
            Traceback (most recent call last):
                ...
            ValueError: Hour must be between 0 and 23.
        """

        if not 0 <= hour <= 23:
            raise ValueError(
                "Hour must be between 0 and 23."
            )

        day_type = day_type.lower()

        if day_type not in ("weekday", "weekend"):
            raise ValueError(
                "Day type must be weekday or weekend."
            )

        if day_type == "weekday":

            if 8 <= hour <= 10 or 17 <= hour <= 20:
                return 1.5

        else:

            if 17 <= hour <= 21:
                return 1.3

        return 1.0

    # Distance Converter

    def km_to_miles(self, km: float) -> float:
        """
        Convert kilometers to miles.

        Args:
            km (float): Distance in kilometers.

        Returns:
            float: Distance in miles.

        Raises:
            ValueError: If km is negative.

        Example:
            >>> calc = TransportCalculator()
            >>> calc.km_to_miles(1.0)
            0.6214
            >>> calc.km_to_miles(0.0)
            0.0
            >>> calc.km_to_miles(-3.0)
            Traceback (most recent call last):
                ...
            ValueError: Distance cannot be negative.
        """

        if km < 0:
            raise ValueError(
                "Distance cannot be negative."
            )

        return round(km * 0.621371, 4)

    # Validation Methods

    def validate_distance(self, distance):
        """Validate distance.

        Args:
            distance (float): Distance to validate.

        Returns:
            None

        Raises:
            ValueError: If distance is zero or negative.

        Example:
            >>> calc = TransportCalculator()
            >>> calc.validate_distance(10.0)
            >>> calc.validate_distance(0)
            Traceback (most recent call last):
                ...
            ValueError: Distance must be greater than 0.
        """

        if distance <= 0:
            raise ValueError("Distance must be greater than 0.")

    def validate_vehicle(self, vehicle):
        """Validate vehicle type.

        Args:
            vehicle (str): Vehicle type to validate.

        Returns:
            None

        Raises:
            ValueError: If vehicle is not "car", "bike", or "auto".

        Example:
            >>> calc = TransportCalculator()
            >>> calc.validate_vehicle("car")
            >>> calc.validate_vehicle("taxi")
            Traceback (most recent call last):
                ...
            ValueError: Invalid vehicle. Choose car, bike or auto.
        """

        vehicle = vehicle.lower()

        if vehicle not in self.FARE_RATES:
            raise ValueError("Invalid vehicle. Choose car, bike or auto.")

    def validate_hour(self, hour):
        """Validate hour.

        Args:
            hour (int): Hour to validate (0-23).

        Returns:
            None

        Raises:
            ValueError: If hour is outside the range 0-23.

        Example:
            >>> calc = TransportCalculator()
            >>> calc.validate_hour(12)
            >>> calc.validate_hour(24)
            Traceback (most recent call last):
                ...
            ValueError: Hour must be between 0 and 23.
        """

        if hour < 0 or hour > 23:
            raise ValueError("Hour must be between 0 and 23.")

    def validate_day_type(self, day_type):
        """Validate day type.

        Args:
            day_type (str): Day type to validate.

        Returns:
            None

        Raises:
            ValueError: If day_type is not "weekday" or "weekend".

        Example:
            >>> calc = TransportCalculator()
            >>> calc.validate_day_type("weekday")
            >>> calc.validate_day_type("someday")
            Traceback (most recent call last):
                ...
            ValueError: Day type must be weekday or weekend.
        """

        day_type = day_type.lower()

        if day_type not in ("weekday", "weekend"):
            raise ValueError("Day type must be weekday or weekend.")

    def validate_discount(self, discount):
        """Validate discount percentage.

        Args:
            discount (float): Discount percentage to validate.

        Returns:
            None

        Raises:
            ValueError: If discount is outside the range 0-100.

        Example:
            >>> calc = TransportCalculator()
            >>> calc.validate_discount(20)
            >>> calc.validate_discount(150)
            Traceback (most recent call last):
                ...
            ValueError: Discount must be between 0 and 100.
        """

        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100.")


    def get_valid_input(self, prompt, data_type=str, validator=None):
        """
        Read and validate user input.

        Args:
            prompt (str): Text shown to the user when requesting input.
            data_type (type): Type to cast the raw input string to.
                Defaults to str.
            validator (callable): Optional function that raises
                ValueError if the cast value is invalid. Defaults to None.

        Returns:
            The validated, type-cast user input.

        Raises:
            None: Invalid input is caught internally and re-prompted;
                no exception propagates to the caller.

        Example:
            >>> callable(TransportCalculator().get_valid_input)
            True
        """

        while True:

            try:
                value = data_type(input(prompt).strip())

                if validator:
                    validator(value)

                return value

            except ValueError as error:
                print(error)


    def run(self):
        """
        Start the Transport Fare Calculator.

        Args:
            None

        Returns:
            None

        Raises:
            None: User-facing errors are caught and re-prompted via
                get_valid_input; no exception propagates to the caller.

        Example:
            >>> callable(TransportCalculator().run)
            True
        """

        print("\n" + "=" * 50)
        print("        Transport Fare Calculator")
        print("=" * 50)

        # Get distance
        distance = self.get_valid_input(
            "\nEnter distance (km): ",
            float,
            self.validate_distance,
        )

        # Get vehicle
        vehicle = self.get_valid_input(
            "Enter vehicle (car/bike/auto): ",str,self.validate_vehicle,).lower()

        # Surge pricing
        multiplier = 1.0

        choice = input("\nApply surge pricing? (y/n): ").strip().lower()

        if choice == "y":

            hour = self.get_valid_input(
                "Current hour (0-23): ",
                int,
                self.validate_hour,
            )

            day_type = self.get_valid_input(
                "Day type (weekday/weekend): ",
                str,
                self.validate_day_type,
            ).lower()

            multiplier = self.surge_multiplier(hour, day_type)

        # Discount
        discount = 0.0

        choice = input("\nApply discount? (y/n): ").strip().lower()

        if choice == "y":

            discount = self.get_valid_input(
                "Discount (%): ",
                float,
                self.validate_discount,
            )

        # Generate summary
        summary = self.trip_summary(
            distance,
            vehicle,
            discount,
        )

        total_fare = round(summary["final_fare"] * multiplier, 2,)

        # Display result
        print("\n" + "=" * 50)
        print("                 Trip Summary")
        print("=" * 50)

        print(f"Vehicle              : {summary['vehicle'].title()}")
        print(f"Distance             : {summary['distance']} km")
        print(f"Base Fare            : ₹{summary['fare']:.2f}")
        print(f"Discount             : {summary['discount']}%")
        print(f"Fare After Discount  : ₹{summary['final_fare']:.2f}")

        if multiplier > 1:
            print(f"Surge Multiplier     : {multiplier}x")

        print(f"Total Fare           : ₹{total_fare:.2f}")
        print(f"Estimated Time       : {summary['eta']} minutes")

        # Convert to miles
        choice = input("\nConvert distance to miles? (y/n): ").strip().lower()

        if choice == "y":
            miles = self.km_to_miles(distance)
            print(f"{distance} km = {miles} miles")

        print("\nThank you for using Transport Fare Calculator!")


if __name__ == "__main__":
    calculator = TransportCalculator()
    calculator.run()
