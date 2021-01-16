import 'package:google_maps_flutter/google_maps_flutter.dart';

class Point {
  double lat;
  double lng;

  Map<String, dynamic> toJson() => {
        'lat': lat,
        'lng': lng,
      };

  LatLng toLatLong() => LatLng(lat, lng);

  Point.fromJson(Map<String, dynamic> json)
      : lat = json['lat'],
        lng = json['lng'];

  Point.fromLatLong(LatLng latLng)
      : lat = latLng.latitude,
        lng = latLng.longitude;
}
