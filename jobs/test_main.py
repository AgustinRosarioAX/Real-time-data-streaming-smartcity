# import unittest
# from main import generate_vehicle_data, generate_weather_data, simulate_vehicle_movement, generate_traffic_camera_data, \
#     generate_gps_data, generate_emergency_incident_data
# from datetime import datetime
#
# class TestDataGeneration(unittest.TestCase):
#
#     def test_generate_vehicle_data(self):
#         device_id = 'TestVehicle123'
#         vehicle_data = generate_vehicle_data(device_id)
#
#         self.assertEqual(vehicle_data['deviceId'], device_id)
#         self.assertIn('timestamp', vehicle_data)
#         self.assertTrue(10 <= vehicle_data['speed'] <= 40)
#
#     def test_generate_weather_data(self):
#         device_id = 'WeatherDevice123'
#         timestamp = datetime.now().isoformat()
#         location = {'latitude': 51.5074, 'longitude': -0.1278}
#
#         weather_data = generate_weather_data(device_id, timestamp, location)
#
#         self.assertEqual(weather_data['deviceId'], device_id)
#         self.assertIn('weatherCondition', weather_data)
#         self.assertTrue(-5 <= weather_data['temperature'] <= 26)
#
#     def test_generate_traffic_camera_data(self):
#         device_id = 'CameraDevice123'
#         timestamp = datetime.now().isoformat()
#         location = {'latitude': 51.5074, 'longitude': -0.1278}
#         camera_id = 'Camera123'
#
#         traffic_data = generate_traffic_camera_data(device_id, timestamp, location, camera_id)
#
#         self.assertEqual(traffic_data['deviceId'], device_id)
#         self.assertEqual(traffic_data['cameraId'], camera_id)
#         self.assertIn('snapshot', traffic_data)
#
#     def test_generate_gps_data(self):
#         device_id = 'GPSDevice123'
#         timestamp = datetime.now().isoformat()
#
#         gps_data = generate_gps_data(device_id, timestamp)
#
#         self.assertEqual(gps_data['deviceId'], device_id)
#         self.assertIn('speed', gps_data)
#         self.assertTrue(0 <= gps_data['speed'] <= 40)
#
#     def test_generate_emergency_incident_data(self):
#         device_id = 'EmergencyDevice123'
#         timestamp = datetime.now().isoformat()
#         location = {'latitude': 51.5074, 'longitude': -0.1278}
#
#         emergency_data = generate_emergency_incident_data(device_id, timestamp, location)
#
#         self.assertEqual(emergency_data['deviceId'], device_id)
#         self.assertIn('incidentId', emergency_data)
#         self.assertIn('type', emergency_data)
#         self.assertIn('status', emergency_data)
#
#     def test_vehicle_movement(self):
#         initial_location = {'latitude': 51.5074, 'longitude': -0.1278}
#         location_after_movement = simulate_vehicle_movement()
#
#         self.assertNotEqual(initial_location['latitude'], location_after_movement['latitude'])
#         self.assertNotEqual(initial_location['longitude'], location_after_movement['longitude'])
#
# if __name__ == '__main__':
#     unittest.main()