from vehicle import vehicle_info

def test_vehicle_info():
    expected_output = (
        "Vehicle Number: AB12CD3456\n"
        "Owner Name: Nikhil\n"
        "Vehicle Type: Car\n"
        "Year of Manufacture: 2025"
    )

    result = vehicle_info("AB12CD3456", "Nikhil", "Car", 2025)
    assert result == expected_output
